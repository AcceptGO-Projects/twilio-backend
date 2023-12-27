from fastapi import HTTPException
from app.dependencies import get_twilio_client, get_twilio_number

from app.schemas.register_form import RegisterForm

def send_registration_message(form_data: RegisterForm):
    client = get_twilio_client()
    twilio_number = get_twilio_number()
    try:
        message = client.messages.create(
            body=f"Gracias por registrarte, {form_data.nombre}.",
            from_=f'whatsapp:{twilio_number}',
            to=f'whatsapp:{form_data.telefono}'
        )
        return message.sid
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))