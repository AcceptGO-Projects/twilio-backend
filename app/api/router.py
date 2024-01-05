import logging as logger
import datetime
from fastapi import APIRouter, Depends, HTTPException
from app.config.config import get_settings
from app.schemas.register_form import RegisterForm
from app.services.scheduler_service import SchedulerService
from app.services.twilio_service import TwilioService
from app.templates.messages_templates import get_welcome_message

router = APIRouter()
_SETTINGS = get_settings()

@router.post("/register/", status_code=201)
def register_user(form_data: RegisterForm):
    try:
        twilio_service = TwilioService(_SETTINGS)
        scheduler_service = SchedulerService(twilio_service)
        message_status = twilio_service.send_message(form_data, get_welcome_message(form_data.name))
        scheduler_service.schedule_reminders(form_data, form_data.event_date)

        logger.info(f"Usuario {form_data.name} registrado con éxito. SID del mensaje: {message_status}")
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error al registrar al usuario {form_data.name}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
