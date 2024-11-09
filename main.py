import psutil
import time
from datetime import datetime, timezone, timedelta

import datetime as dt
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

APP_NAME = "notepad.exe"

def is_app_running(app_name):
    for proc in psutil.process_iter(attrs=['name']):
        if proc.info['name'] == app_name:
            return True
    return False

def format_datetime(dt):
    return dt.astimezone(timezone(timedelta(hours=1))).isoformat()

def track_app_open_close(app_name,creds):
    app_open = False
    start_time = None
    
    while True:
        if is_app_running(app_name):
            if not app_open:  # Detect app opening
                start_time = datetime.now(timezone.utc)
                app_open = True
                print(f"{app_name} opened at {format_datetime(start_time)}")
        else:
            if app_open:  # Detect app closing
                end_time = datetime.now(timezone.utc)
                print(f"{app_name} closed at {format_datetime(end_time)}")
                print(f"Duration open: {end_time - start_time}")
                service = build("calendar", "v3", credentials=creds)
                event = {
                        "summary": "started coding using VScode",
                        "location" : "my own house",
                        "description": "the user has used VScode in this time chunk to code",
                        "colorId": 6,
                        "start" : { "dateTime": format_datetime(start_time), "timeZone" : "Africa/Tunis"},
                        "end":{"dateTime": format_datetime(end_time), "timeZone" : "Africa/Tunis"},
                        "recurrence":"RRULE:freq=DAILY;COUNT=1"
                    }
                event = service.events().insert(calendarId="primary",body=event).execute()
                app_open = False
                start_time = None  # Reset start time
        time.sleep(10)
    

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json",SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("creds.json", SCOPES)
            creds = flow.run_local_server(port = 0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        track_app_open_close(APP_NAME,creds)
    except HttpError as error:
        print("there was an error", error)


if __name__ == "__main__":
    main()

