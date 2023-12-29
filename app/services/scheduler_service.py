from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app.schemas.register_form import RegisterForm
from app.services.twilio_service import TwilioService
from app.templates.messages_templates import get_24_hour_reminder


class SchedulerService:
    def __init__(self, twilio_service: TwilioService):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.twilio_service = twilio_service

    def programar_recordatorios(self, form_data: RegisterForm, evento_hora: datetime):
        horarios_recordatorios = [
            evento_hora - timedelta(minutes=1),
            evento_hora - timedelta(minutes=2),
            evento_hora - timedelta(minutes=3)
        ]

        for horario in horarios_recordatorios:
            self.scheduler.add_job(
                self.enviar_recordatorio,
                'date',
                run_date=horario,
                args=[form_data, get_24_hour_reminder("20:00 hrs 🇧🇴")]
            )

    def enviar_recordatorio(self, form_data: RegisterForm, mensaje: str):
        self.twilio_service.send_message(form_data, mensaje)
