import io
import json
import logging
import os
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload

router = APIRouter()
logger = logging.getLogger(__name__)

SCOPES = ["https://www.googleapis.com/auth/drive"]
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024


def get_drive_service():
    """Build a Drive client from the service-account JSON stored in Vercel."""
    credentials_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not credentials_json:
        raise RuntimeError("GOOGLE_SERVICE_ACCOUNT_JSON is not configured.")

    credentials = service_account.Credentials.from_service_account_info(
        json.loads(credentials_json), scopes=SCOPES
    )
    return build("drive", "v3", credentials=credentials, cache_discovery=False)


@router.post("/api/upload")
async def upload_image(image: UploadFile = File(...)):
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

    filename = Path(image.filename or "payment-receipt").name
    try:
        drive_service = get_drive_service()
        uploaded_file = drive_service.files().create(
            body={"name": filename, "parents": [folder_id]},
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
    }
