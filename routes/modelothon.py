from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def generate_registration_id(sheet, prefix: str = "MOD") -> str:
    # Note: If adding multiple rows per team, you might want to base the ID 
    # on unique teams rather than total rows, or use a UUID/timestamp.
    # But sticking to your logic:
    existing_rows = sheet.get_all_values()
    # Assuming row 1 is headers, we just use the length to increment
    next_number = max(len(existing_rows), 1) 
    return f"{prefix}{next_number:03d}"

@router.post("/api/modelothon/register")
def register_student(
    # Team Info
    team_name: str = Form(...),
    team_size: str = Form(...),
    
    # Member 1 (Required)
    member_1_name: str = Form(...),
    member_1_phone: str = Form(...),
    member_1_alt_phone: str = Form(default=""),
    member_1_email: str = Form(...),
    member_1_school: str = Form(default=""),
    member_1_city: str = Form(default=""),
    member_1_class: str = Form(default=""),
    
    # Member 2 (Optional)
    member_2_name: str = Form(default=""),
    member_2_phone: str = Form(default=""),
    member_2_alt_phone: str = Form(default=""),
    member_2_email: str = Form(default=""),
    member_2_school: str = Form(default=""),
    member_2_city: str = Form(default=""),
    member_2_class: str = Form(default=""),

    # Member 3 (Optional)
    member_3_name: str = Form(default=""),
    member_3_phone: str = Form(default=""),
    member_3_alt_phone: str = Form(default=""),
    member_3_email: str = Form(default=""),
    member_3_school: str = Form(default=""),
    member_3_city: str = Form(default=""),
    member_3_class: str = Form(default=""),

    payment_screenshot_url: str = Form(default="")
):
    try:
        sheet = get_sheet_connection("Modelothon")
        registration_id = generate_registration_id(sheet) 
        
        # We will build a list of rows to insert
        rows_to_insert = []

        # 1. Add Member 1 (Always exists)
        rows_to_insert.append([
            registration_id, team_name, team_size,
            member_1_name, member_1_phone, member_1_alt_phone, 
            member_1_email, member_1_school, member_1_city, member_1_class,
            payment_screenshot_url
        ])
        
        # 2. Add Member 2 (If provided)
        if member_2_name.strip():
            rows_to_insert.append([
                registration_id, team_name, team_size,
                member_2_name, member_2_phone, member_2_alt_phone, 
                member_2_email, member_2_school, member_2_city, member_2_class,
                payment_screenshot_url
            ])

        # 3. Add Member 3 (If provided)
        if member_3_name.strip():
            rows_to_insert.append([
                registration_id, team_name, team_size,
                member_3_name, member_3_phone, member_3_alt_phone, 
                member_3_email, member_3_school, member_3_city, member_3_class,
                payment_screenshot_url
            ])
            
        # Insert all rows into the Google Sheet automatically at the next available space
        # Using append_rows (plural) is faster and requires only 1 API call to Google
        sheet.append_rows(rows_to_insert)
            
        return {"status": "success", "message": "Saved to Google Cloud!", "registration_id": registration_id}
        
    except Exception as e:
         logger.exception("Modelothon registration failed")
         raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")