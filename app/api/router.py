from fastapi import APIRouter, Depends, Form

from app.schemas.register_form import RegisterForm
from app.services.twilio_services import send_registration_message



router = APIRouter()

@router.post("/register/", status_code=201)
def register_user(form_data: RegisterForm):
    message_sid = send_registration_message(form_data)
    return {"status": "success", "message_sid": message_sid}
