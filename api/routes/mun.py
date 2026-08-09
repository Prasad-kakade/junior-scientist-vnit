from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging

router = APIRouter()
logger = logging.getLogger(__name__)




@router.post("/mun/register")
def register_student(

    # Team Info
    team_name: str = Form(...),
    team_size: str = Form(...),

    # Member 1
    member_1_name: str = Form(...),
    member_1_phone: str = Form(...),
    member_1_alt_phone: str = Form(default=""),
    member_1_email: str = Form(...),
    member_1_school: str = Form(default=""),
    member_1_city: str = Form(default=""),
    member_1_class: str = Form(default=""),

    # Member 2
    member_2_name: str = Form(default=""),
    member_2_phone: str = Form(default=""),
    member_2_alt_phone: str = Form(default=""),
    member_2_email: str = Form(default=""),
    member_2_school: str = Form(default=""),
    member_2_city: str = Form(default=""),
    member_2_class: str = Form(default=""),

    # Member 3
    member_3_name: str = Form(default=""),
    member_3_phone: str = Form(default=""),
    member_3_alt_phone: str = Form(default=""),
    member_3_email: str = Form(default=""),
    member_3_school: str = Form(default=""),
    member_3_city: str = Form(default=""),
    member_3_class: str = Form(default=""),

    # Member 4
    member_4_name: str = Form(default=""),
    member_4_phone: str = Form(default=""),
    member_4_alt_phone: str = Form(default=""),
    member_4_email: str = Form(default=""),
    member_4_school: str = Form(default=""),
    member_4_city: str = Form(default=""),
    member_4_class: str = Form(default="")
):
    try:
        sheet = get_sheet_connection("MUN")

        new_row = [
        
                team_name,
                team_size,
        
                member_1_name, member_1_phone, member_1_alt_phone,
                member_1_email, member_1_school, member_1_city, member_1_class,
        
                member_2_name, member_2_phone, member_2_alt_phone,
                member_2_email, member_2_school, member_2_city, member_2_class,
        
                member_3_name, member_3_phone, member_3_alt_phone,
                member_3_email, member_3_school, member_3_city, member_3_class,
        
                member_4_name, member_4_phone, member_4_alt_phone,
                member_4_email, member_4_school, member_4_city, member_4_class
        
            ]
        
        sheet.append_row(new_row)
        
        return {
                "status": "success",
                "message": "Saved Successfully!"
        }
    except Exception as e:
        logger.exception("MUN registration failed")

        raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")



    