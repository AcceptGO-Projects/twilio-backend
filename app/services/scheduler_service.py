import logging as logger
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app.schemas.register_form import RegisterForm
from app.services.twilio_service import TwilioService
from app.templates.messages_templates import get_24_hour_reminder
from app.templates.messages_templates import get_12_hour_reminder
from app.templates.messages_templates import get_beginning_reminder



class SchedulerService:
    def __init__(self, twilio_service: TwilioService):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.twilio_service = twilio_service

    def schedule_reminders(self, form_data: RegisterForm, event_time: datetime):

        EVENT_HOUR = "20:00 hrs 🇧🇴"

        reminder_times = [
            (event_time - timedelta(minutes=3), get_24_hour_reminder(EVENT_HOUR)),
            (event_time - timedelta(minutes=2), get_12_hour_reminder(EVENT_HOUR, "https://zoom.link")),
            (event_time - timedelta(minutes=1), get_beginning_reminder(EVENT_HOUR, "https://zoom.link"))
        ]

        logger.info(f"Programando recordatorios para {form_data.phone}")

        for reminder_time, message in reminder_times:
            try:
                self.scheduler.add_job(
                    self.send_reminder,
                    'date',
                    run_date=reminder_time,
                    args=[form_data, message]
                )
                logger.info(f"Recordatorio programado para {form_data.phone} en {reminder_time}")
            except Exception as e:
                logger.error(f"Error al programar recordatorio: {str(e)}")

    def send_reminder(self, form_data: RegisterForm, message: str):
        try:
            self.twilio_service.send_message(form_data, message)
            logger.info(f"Recordatorio enviado a {form_data.phone}")
        except Exception as e:
            logger.error(f"Error al enviar recordatorio: {str(e)}")