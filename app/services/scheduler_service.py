import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

from fastapi import HTTPException
from app.models.reminder import Reminder
from app.repositories.reminder_repository import ReminderRepository
from app.schemas.lead import Lead
from app.services.twilio_service import TwilioService
from app.templates.messages_templates import get_24_hour_reminder
from app.templates.messages_templates import get_12_hour_reminder
from app.templates.messages_templates import get_beginning_reminder
from pytz import utc



class SchedulerService:
    def __init__(self, twilio_service: TwilioService, reminder_repo:ReminderRepository):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.twilio_service = twilio_service
        self.reminder_repo = reminder_repo
        self.load_pending_reminder()

    def schedule_reminders(self, form_data: Lead, event_time: datetime, lead_event_id: int):

        EVENT_HOUR = "20:00 hrs 🇧🇴"

        reminder_times = [
            (event_time - timedelta(hours=24), get_24_hour_reminder(EVENT_HOUR)),
            (event_time - timedelta(hours=1), get_12_hour_reminder(EVENT_HOUR, "https://zoom.link")),
            (event_time - timedelta(minutes=5), get_beginning_reminder(EVENT_HOUR, "https://zoom.link"))
        ]

        for reminder_time, message in reminder_times:
            reminder = self.reminder_repo.add_reminder(lead_event_id, form_data.phone, message, reminder_time)
            self.scheduler.add_job(
                self.send_reminder,
                'date',
                run_date=reminder_time,
                args=[form_data.phone, message, reminder]
            )

    def send_reminder(self, lead_phone: str, message: str, reminder:Reminder):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.twilio_service.send_message(lead_phone, message)
                self.reminder_repo.mark_reminder_as_sent(reminder.id)
                break
            except HTTPException:
                if attempt == max_retries - 1:
                    raise
                time.sleep(5)
    

    def load_pending_reminder(self):
        pending_reminders = self.reminder_repo.get_pending_reminders()
        for reminder in pending_reminders:
            utc_reminder_date = reminder.reminder_date.astimezone(utc) - timedelta(hours=4)
            self.scheduler.add_job(
                self.send_reminder,
                'date',
                run_date=utc_reminder_date,
                args=[reminder.to_number, reminder.content, reminder]
            )



