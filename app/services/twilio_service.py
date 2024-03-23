import logging
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from fastapi import HTTPException
from app.config.config import get_settings

from starlette.concurrency import run_in_threadpool

class TwilioService:
    def __init__(self):
        settings = get_settings()
        self.client = Client(settings.twilio_account_ssid, settings.twilio_auth_token)
        self.twilio_number = settings.twilio_number
        self.logger = logging.getLogger("twilio_service")

    async def send_message(self, number: str, message: str):
        try:
            # Execute the synchronous Twilio API call in a threadpool
            message_response = await run_in_threadpool(
                self.client.messages.create,
                body=message,
                from_=f'whatsapp:{self.twilio_number}',
                to=f'whatsapp:{number}'
            )
            self.logger.info(f"Message sent to {number}: {message_response.sid}")
            return message_response.sid
        except TwilioRestException as e:
            self.logger.error(f"Error sending message to {number}: {e}")
            raise HTTPException(status_code=400, detail=f"Error sending message: {str(e)}")

