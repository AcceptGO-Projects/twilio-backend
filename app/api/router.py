import datetime
from fastapi import APIRouter, Depends
from app.config.config import get_settings
from app.schemas.register_form import RegisterForm
from app.services.scheduler_service import SchedulerService
from app.services.twilio_service import TwilioService
from app.templates.messages_templates import get_welcome_message

router = APIRouter()

_SETTINGS = get_settings()


@router.post("/register/", status_code=201)
def register_user(form_data: RegisterForm):
    twilio_service = TwilioService(_SETTINGS)
    scheduler_service = SchedulerService(twilio_service)
    twilio_service.send_message(form_data, get_welcome_message(form_data.name))
    scheduler_service.programar_recordatorios(form_data, form_data.event_date)
    return {"status": "success"}
