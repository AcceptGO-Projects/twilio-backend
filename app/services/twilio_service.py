from twilio.rest import Client
from fastapi import HTTPException
from app.config.config import Settings, get_settings
from app.schemas.register_form import RegisterForm

class TwilioService:
    def __init__(self, settings: Settings):
        self.client = self.get_twilio_client(settings)
        self.twilio_number = settings.twilio_number

    def get_twilio_client(self, settings):
        if not all([settings.twilio_account_ssid, settings.twilio_auth_token]):
            raise HTTPException(status_code=500, detail="Twilio credentials are not set")
        return Client(settings.twilio_account_ssid, settings.twilio_auth_token)

    def send_message(self, form_data: RegisterForm, message: str):
        try:
            message = self.client.messages.create(
                body=message,
                from_=f'whatsapp:{self.twilio_number}',
                to=f'whatsapp:{form_data.phone}'
            )
            return message.sid
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
