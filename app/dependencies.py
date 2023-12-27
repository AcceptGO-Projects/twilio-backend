from twilio.rest import Client
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

def get_twilio_credentials():
    account_sid = os.getenv('TWILIO_ACCOUNT_SSID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')
    print(account_sid,auth_token, twilio_number)
    if not all([account_sid, auth_token, twilio_number]):
        raise HTTPException(status_code=500, detail="Twilio credentials are not set")
    return account_sid, auth_token, twilio_number

def get_twilio_client():
    account_sid, auth_token, _ = get_twilio_credentials()
    return Client(account_sid, auth_token)

def get_twilio_number() -> str:
    _, _, twilio_number = get_twilio_credentials()
    return twilio_number