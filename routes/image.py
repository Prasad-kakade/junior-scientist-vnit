import io
import json
import logging
import os
import re
import time
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload

router = APIRouter()
logger = logging.getLogger(__name__)

SCOPES = ["https://www.googleapis.com/auth/drive"]
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024


def get_drive_service():
    """Build a Drive client for the personal Google account stored in Vercel."""
    token_json = os.environ.get("GOOGLE_DRIVE_OAUTH_TOKEN_JSON")
    if not token_json:
        raise RuntimeError("GOOGLE_DRIVE_OAUTH_TOKEN_JSON is not configured.")

    credentials = Credentials.from_authorized_user_info(json.loads(token_json), SCOPES)
    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    if not credentials.valid:
        raise RuntimeError("Google Drive OAuth credentials are invalid or expired.")

    return build("drive", "v3", credentials=credentials, cache_discovery=False)


def sanitize_filename_part(text: str) -> str:
    """Removes special characters and spaces for safe filenames."""
    # Replace anything that isn't alphanumeric with a hyphen
    cleaned = re.sub(r'[^a-zA-Z0-9]+', '-', text.strip())
    return cleaned.strip('-').lower()


@router.post("/api/upload")
async def upload_image(
    image: UploadFile = File(...),
    applicant_name: str = Form(...),
    event_name: str = Form(...)
):
    """Upload a payment screenshot to the configured private Google Drive folder."""
    if image.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Only JPEG, PNG, and WebP images are accepted.",
        )

    contents = await image.read()
    await image.close()

    if not contents:
        raise HTTPException(status_code=400, detail="The selected image is empty.")
    if len(contents) > MAX_IMAGE_SIZE_BYTES:
        raise HTTPException(status_code=413, detail="Image must be 10 MB or smaller.")

    folder_id = os.environ.get("GOOGLE_DRIVE_FOLDER_ID")
    if not folder_id:
        logger.error("GOOGLE_DRIVE_FOLDER_ID is not configured.")
        raise HTTPException(status_code=500, detail="Image upload is not configured.")

    # --- NEW FILENAME GENERATION LOGIC ---
    original_ext = Path(image.filename).suffix if image.filename else ""
    clean_name = sanitize_filename_part(applicant_name)
    clean_event = sanitize_filename_part(event_name)
    timestamp = int(time.time())
    
    # Example: modelothon_john-doe_1716345600.png
    new_filename = f"{clean_event}_{clean_name}_{timestamp}{original_ext}"

    try:
        drive_service = get_drive_service()
        uploaded_file = drive_service.files().create(
            body={"name": new_filename, "parents": [folder_id]},
            media_body=MediaIoBaseUpload(
                io.BytesIO(contents), mimetype=image.content_type, resumable=False
            ),
            fields="id",
        ).execute()
    except (HttpError, RuntimeError, ValueError, json.JSONDecodeError):
        logger.exception("Google Drive image upload failed")
        raise HTTPException(
            status_code=500, detail="Unable to upload the image. Please try again."
        )

    return {
        "message": "Payment screenshot uploaded successfully.",
        "drive_file_id": uploaded_file.get("id"),
        "filename": new_filename
    }