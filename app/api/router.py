import datetime
from fastapi import APIRouter, Depends, Form

from app.schemas.register_form import RegisterForm
from app.services.scheduler_service import programar_recordatorios
from app.services.twilio_services import send_registration_message



router = APIRouter()

@router.post("/register/", status_code=201)
def register_user(form_data: RegisterForm):
    message_sid = send_registration_message(form_data, "Your package has been shipped. It will be delivered in 1 business days.")
    evento_hora = datetime.datetime(2023, 12, 27, 17, 51)
    programar_recordatorios(form_data, evento_hora)

    return {"status": "success", "message_sid": message_sid}
