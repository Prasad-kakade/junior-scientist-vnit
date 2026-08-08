from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection

router = APIRouter()




@router.post("/catapultikon/register")
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
    member_3_class: str = Form(default="")
):
    try:
        sheet = get_sheet_connection("Catapultikon")
        new_row = [
                team_name, team_size,
        
                member_1_name, member_1_phone, member_1_alt_phone,
                member_1_email, member_1_school, member_1_city, member_1_class,
        
                member_2_name, member_2_phone, member_2_alt_phone,
                member_2_email, member_2_school, member_2_city, member_2_class,
        
                member_3_name, member_3_phone, member_3_alt_phone,
                member_3_email, member_3_school, member_3_city, member_3_class
            ]
        
        
        sheet.append_row(new_row)
        
        return {
                "status": "success",
                "message": "Saved to Google Cloud!"
            }
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    