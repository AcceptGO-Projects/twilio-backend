from twilio.rest import Client
from fastapi import HTTPException
from app.config.config import Settings, get_settings
from app.schemas.lead import Lead
from app.repositories.message_repository import MessageRepository

class TwilioService:
    def __init__(self, settings: Settings, message_repo: MessageRepository):
        self.client = self.get_twilio_client(settings)
        self.twilio_number = settings.twilio_number
        self.message_repo = message_repo        

    def get_twilio_client(self, settings):
        if not all([settings.twilio_account_ssid, settings.twilio_auth_token]):
            raise HTTPException(status_code=500, detail="Twilio credentials are not set")
        return Client(settings.twilio_account_ssid, settings.twilio_auth_token)

    def send_message(self, form_data: Lead, message: str):
        try:
            message_response = self.client.messages.create(
                body=message,
                from_=f'whatsapp:{self.twilio_number}',
                to=f'whatsapp:{form_data.phone}'
            )
            self.message_repo.add_message(form_data.phone, message, True)
            return message_response.sid
        except Exception as e:
            self.message_repo.add_message(form_data.phone, message, False, str(e))
            raise HTTPException(status_code=400, detail=str(e))
