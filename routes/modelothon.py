from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def generate_registration_id(sheet, prefix: str = "MOD") -> str:
    # Look ONLY at Column A to count rows, avoiding the "invisible data" bug
    col_a_values = sheet.col_values(1)
    
    # Subtract 1 for the header row. Use max to ensure it doesn't drop below 1
    next_number = max(len(col_a_values) - 1, 0) + 1
    return f"{prefix}{next_number:03d}"

@router.post("/api/modelothon/register")
def register_student(
    # Team Info
    team_name: str = Form(...),
    team_size: str = Form(...),
    
    # Member 1 (Always required)
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

    payment_screenshot_url: str = Form(default="")
):
    try:
        sheet = get_sheet_connection("Modelothon")
        registration_id = generate_registration_id(sheet) 
        
        # Original single-row structure
        new_row = [
            registration_id,    
            team_name, team_size,
            
            member_1_name, member_1_phone, member_1_alt_phone, 
            member_1_email, member_1_school, member_1_city, member_1_class,
            
            member_2_name, member_2_phone, member_2_alt_phone, 
            member_2_email, member_2_school, member_2_city, member_2_class,
            
            member_3_name, member_3_phone, member_3_alt_phone, 
            member_3_email, member_3_school, member_3_city, member_3_class,

            payment_screenshot_url
        ]
            
        # FIX: Find the exact next empty row by checking the length of Column A
        col_a_values = sheet.col_values(1)
        next_row_index = len(col_a_values) + 1 
        
        # FIX: Force the data to paste starting exactly at Column A of the next row.
        # [new_row] is nested in a list because sheet.update expects a 2D array (list of lists).
        sheet.update(f"A{next_row_index}", [new_row])
            
        return {"status": "success", "message": "Saved to Google Cloud!", "registration_id": registration_id}
    except Exception as e:
         logger.exception("Modelothon registration failed")
         raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")