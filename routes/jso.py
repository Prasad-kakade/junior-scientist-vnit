from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging

router = APIRouter()
logger = logging.getLogger(__name__)




@router.post("/api/JSO/register")
def register_student(
    full_name: str = Form(...),
    phone: str = Form(...),
    alt_phone: str = Form(default=""),
    email: str = Form(...),
    school: str = Form(...),
    city: str = Form(...),
    student_class: str = Form(...)
):
    try:
        sheet = get_sheet_connection("JSO")
        new_row = [
                full_name,
                phone,
                alt_phone,
                email,
                school,
                city,
                student_class
            ]
        
        sheet.append_row(new_row)
        
        return {
                "status": "success",
                "message": "Saved Successfully!"
        }
    except Exception as e:
        logger.exception("JSO registration failed")

        raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")

    

    