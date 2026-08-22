from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


def generate_registration_id(sheet, prefix: str = "JSO") -> str: # ID generator
    existing_rows = sheet.get_all_values()
    next_number = max(len(existing_rows) - 1, 0) + 1
    return f"{prefix}{next_number:03d}"

@router.post("/api/JSO/register")
def register_student(
    full_name: str = Form(...),
    phone: str = Form(...),
    alt_phone: str = Form(default=""),
    email: str = Form(...),
    school: str = Form(...),
    city: str = Form(...),
    student_class: str = Form(...),

    # Payment screenshot (uploaded separately to Drive via /api/upload,
    # the resulting shareable link is passed along with the registration)
    payment_screenshot_url: str = Form(default="")
):
    try:
        sheet = get_sheet_connection("JSO")
        registration_id = generate_registration_id(sheet) # add this
        new_row = [
                registration_id,
                full_name,
                phone,
                alt_phone,
                email,
                school,
                city,
                student_class,
                payment_screenshot_url
            ]
        
        sheet.append_row(new_row)
        
        return {
                "status": "success",
                "message": "Saved Successfully!",
                "registration_id": registration_id
        }
    except Exception as e:
        logger.exception("JSO registration failed")

        raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")

    

    