# Notepad Tracking Script

This project is a Python script that monitors **Notepad** usage on your computer and logs the open and close times as events in **Google Calendar** via the Google Calendar API. It's especially useful for **time management, productivity tracking**, and **automation** enthusiasts who want to log time on specific tasks.

## How It Works
The script:
1. Continuously monitors if Notepad is open using process tracking.
2. Logs the exact times when Notepad opens and closes.
3. Automatically creates a calendar event on Google Calendar marking the open and close times of each Notepad session.

## Technologies Used

This project is written in Python and uses the following libraries:

- **psutil**: To track when Notepad opens and closes by checking all running processes.
- **google-auth** and **google-auth-oauthlib**: For secure authentication and OAuth2 authorization with Google Calendar API.
- **google-api-python-client**: The core library for interacting with Google APIs, enabling event creation in Google Calendar.
- **datetime**: To capture and format the exact times of Notepad opening and closing.
- **os**: To check for local credential files (e.g., `token.json`) for storing authentication tokens.

## Installation

### Prerequisites
1. **Python 3.7 or higher**: Make sure Python is installed.
2. **Google Cloud Project**: Set up a Google Cloud Project to enable the Google Calendar API and obtain your `creds.json` file.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/BahaRiahi3/Python-Automation-Projects
   cd notepad-tracking-script
