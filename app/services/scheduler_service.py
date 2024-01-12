import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

from fastapi import HTTPException
from app.schemas.lead import Lead
from app.services.twilio_service import TwilioService
from app.templates.messages_templates import get_24_hour_reminder
from app.templates.messages_templates import get_12_hour_reminder
from app.templates.messages_templates import get_beginning_reminder



class SchedulerService:
    def __init__(self, twilio_service: TwilioService):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.twilio_service = twilio_service

    def schedule_reminders(self, form_data: Lead, event_time: datetime):

        EVENT_HOUR = "20:00 hrs 🇧🇴"

        reminder_times = [
            (event_time - timedelta(minutes=3), get_24_hour_reminder(EVENT_HOUR)),
            (event_time - timedelta(minutes=2), get_12_hour_reminder(EVENT_HOUR, "https://zoom.link")),
            (event_time - timedelta(minutes=1), get_beginning_reminder(EVENT_HOUR, "https://zoom.link"))
        ]

        for reminder_time, message in reminder_times:
            self.scheduler.add_job(
                self.send_reminder,
                'date',
                run_date=reminder_time,
                args=[form_data, message]
            )

    def send_reminder(self, form_data: Lead, message: str):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.twilio_service.send_message(form_data, message)
                break
            except HTTPException:
                if attempt == max_retries - 1:
                    raise
                time.sleep(5)
