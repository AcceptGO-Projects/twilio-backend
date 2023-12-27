from fastapi import HTTPException
from app.schemas.register_form import RegisterForm

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