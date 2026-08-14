from fastapi import APIRouter, Form, HTTPException
from api.google_sheet import get_sheet_connection
import logging


router = APIRouter()
logger = logging.getLogger(__name__)

def generate_registration_id(sheet, prefix: str = "MOD") -> str: # ID generator
    existing_rows = sheet.get_all_values()
    next_number = max(len(existing_rows) - 1, 0) + 1
    return f"{prefix}{next_number:03d}"

@router.post("/api/modelothon/register")
def register_student(
    # Team Info
    team_name: str = Form(...),
    team_size: str = Form(...),
    
    # Member 1 (Always required since min team size is 1)
    member_1_name: str = Form(...),
    member_1_phone: str = Form(...),
    member_1_alt_phone: str = Form(default=""),
    member_1_email: str = Form(...),
    member_1_school: str = Form(default=""),
    member_1_city: str = Form(default=""),
    member_1_class: str = Form(default=""),
    
    # Member 2 (Optional: default="" prevents errors if team size is 1)
    member_2_name: str = Form(default=""),
    member_2_phone: str = Form(default=""),
    member_2_alt_phone: str = Form(default=""),
    member_2_email: str = Form(default=""),
    member_2_school: str = Form(default=""),
    member_2_city: str = Form(default=""),
    member_2_class: str = Form(default=""),

    # Member 3 (Optional: default="" prevents errors if team size is 1 or 2)
    member_3_name: str = Form(default=""),
    member_3_phone: str = Form(default=""),
    member_3_alt_phone: str = Form(default=""),
    member_3_email: str = Form(default=""),
    member_3_school: str = Form(default=""),
    member_3_city: str = Form(default=""),
    member_3_class: str = Form(default="")
):
    try:
        sheet = get_sheet_connection("Modelothon")
        registration_id = generate_registration_id(sheet) # add this
        new_row = [
                registration_id,    # add this
                team_name, team_size,
                
                # Member 1
                member_1_name, member_1_phone, member_1_alt_phone, 
                member_1_email, member_1_school, member_1_city, member_1_class,
                
                # Member 2
                member_2_name, member_2_phone, member_2_alt_phone, 
                member_2_email, member_2_school, member_2_city, member_2_class,
                
                # Member 3
                member_3_name, member_3_phone, member_3_alt_phone, 
                member_3_email, member_3_school, member_3_city, member_3_class
            ]
            
            # Insert the row into the Google Sheet automatically at the next available space
        sheet.append_row(new_row)
            
        return {"status": "success", "message": "Saved to Google Cloud!","registration_id": registration_id}
    except Exception as e:
         logger.exception("Modelothon registration failed")

         raise HTTPException(status_code=500, detail="Registration failed. Please try again later.")

    
    # Package the new data as a list (representing a row)
    # The columns in your Google Sheet should match this exact order
         