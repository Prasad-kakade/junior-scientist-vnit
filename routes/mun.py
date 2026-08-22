from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


def generate_registration_id(sheet, prefix: str = "MUN") -> str:  # ID generator
    existing_rows = sheet.get_all_values()
    next_number = max(len(existing_rows) - 1, 0) + 1
    return f"{prefix}{next_number:03d}"


@router.post("/api/mun/register")
def register_student(

    # Delegate Info (single participation)
    delegate_name: str = Form(...),
    delegate_school: str = Form(...),
    delegate_email: str = Form(...),
    delegate_phone: str = Form(...),

    # Compulsory Questionnaire
    q1: str = Form(...),
    q2: str = Form(...),
    q3: str = Form(...),
    q4: str = Form(...),
    q5: str = Form(...),
    q6: str = Form(...),

    # Payment screenshot (uploaded separately to Drive via /api/upload,
    # the resulting shareable link is passed along with the registration)
    payment_screenshot_url: str = Form(default=""),
):
    try:
        sheet = get_sheet_connection("MUN")
        registration_id = generate_registration_id(sheet)  # add this
        new_row = [
            registration_id,  # add this
            delegate_name,
            delegate_school,
            delegate_email,
            delegate_phone,

            q1,
            q2,
            q3,
            q4,
            q5,
            q6,

            payment_screenshot_url,
        ]

        sheet.append_row(new_row)

        return {
            "status": "success",
            "message": "Saved Successfully!",
            "registration_id": registration_id
        }
    except Exception as e:
        logger.exception("MUN registration failed")

        raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


def generate_registration_id(sheet, prefix: str = "MUN") -> str:  # ID generator
    existing_rows = sheet.get_all_values()
    next_number = max(len(existing_rows) - 1, 0) + 1
    return f"{prefix}{next_number:03d}"


@router.post("/api/mun/register")
def register_student(

    # Delegate Info (single participation)
    delegate_name: str = Form(...),
    delegate_school: str = Form(...),
    delegate_email: str = Form(...),
    delegate_phone: str = Form(...),

    # Compulsory Questionnaire
    q1: str = Form(...),
    q2: str = Form(...),
    q3: str = Form(...),
    q4: str = Form(...),
    q5: str = Form(...),
    q6: str = Form(...),
):
    try:
        sheet = get_sheet_connection("MUN")
        registration_id = generate_registration_id(sheet)  # add this
        new_row = [
            registration_id,  # add this
            delegate_name,
            delegate_school,
            delegate_email,
            delegate_phone,

            q1,
            q2,
            q3,
            q4,
            q5,
            q6,
        ]

        sheet.append_row(new_row)

        return {
            "status": "success",
            "message": "Saved Successfully!",
            "registration_id": registration_id
        }
    except Exception as e:
        logger.exception("MUN registration failed")

        raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")