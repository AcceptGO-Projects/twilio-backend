from fastapi import HTTPException
from app.schemas.register_form import RegisterForm
from app.config.config import get_settings

def send_registration_message(form_data: RegisterForm, mensaje: str):
    from app.main import get_twilio_client, get_twilio_number

    client = get_twilio_client()
    twilio_number = get_twilio_number()
    try:
        message = client.messages.create(
            body=mensaje,
            from_=f'whatsapp:{twilio_number}',
            to=f'whatsapp:{form_data.telefono}'
        )
        return message.sid
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def send_custom_message(telefono, message):
    settings = get_settings()
    from twilio.rest import Client
    client = Client(settings.twilio_account_ssid, settings.twilio_auth_token)

    try:
        message = client.messages.create(
            body=f"{message}",
            from_=f'whatsapp:{settings.twilio_number}',
            to=f'whatsapp:{telefono}'
        )
        return message.sid
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))