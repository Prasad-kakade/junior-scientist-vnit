
import os
import json
import gspread
from google.oauth2.service_account import Credentials

def get_sheet_connection(sheet_name):
    try:
        # 1. Load credentials from the environment variable
        creds_raw = os.environ.get("GOOGLE_CREDENTIALS_JSON")
        creds_dict = json.loads(creds_raw)
        
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        client = gspread.authorize(creds)
        
        # 2. Load the Google Workspace Sheet ID from the environment variable
        workspace_id = os.environ.get("GOOGLE_WORKSPACE_ID")
        
        # 3. Open spreadsheet and specific tab
        spreadsheet = client.open_by_key(workspace_id)
        return spreadsheet.worksheet(sheet_name)
        
    except Exception as e:
        print(f"Error connecting to Google Sheet: {e}")
        raise e