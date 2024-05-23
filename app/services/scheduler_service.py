from datetime import timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import HTTPException
from app.helpers.reminder_factory import replace_message_with_name
from app.models.event_reminder import EventReminder
from app.repositories.reminder_repository import ReminderRepository
from app.services.twilio_service import TwilioService
from pytz import utc
import asyncio

class SchedulerService:        
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, twilio_service: TwilioService, reminder_repo: ReminderRepository):
        if not hasattr(self, 'initialized'):
            self.scheduler = AsyncIOScheduler()
            self.twilio_service = twilio_service
            self.reminder_repo = reminder_repo
            self.initialized = True

    async def start(self):
        if not self.scheduler.running:
            self.scheduler.start()
            await self.load_pending_reminders()

    async def schedule_reminders(
        self,
        lead_name: str,
        lead_phone: str,
        lead_event_id: int,
        event_reminders: list[EventReminder],
    ):
        for reminder in event_reminders:
            reminder_message = replace_message_with_name(reminder.message, lead_name)  # type: ignore
            reminder_time = reminder.reminder_time
            reminder_save = await self.reminder_repo.add_reminder(lead_event_id=lead_event_id, to_number=lead_phone, content=reminder_message, reminder_date=reminder_time)  # type: ignore
            print(
                self.scheduler.add_job(
                    self.send_reminder,
                    "date",
                    run_date= reminder_time  + timedelta(hours=4),  # type: ignore
                    args=[lead_phone, reminder_message, reminder_save.id],
                )
            )

    async def send_reminder(self, lead_phone: str, message: str, reminder_id: int):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                await self.twilio_service.send_message(lead_phone, message)
                await self.reminder_repo.mark_reminder_as_sent(reminder_id) 
                break
            except HTTPException:
                if attempt == max_retries - 1:
                    raise
                await asyncio.sleep(5)

    async def load_pending_reminders(self):
        pending_reminders = await self.reminder_repo.get_pending_reminders()
        for reminder in pending_reminders:
            utc_reminder_date = reminder.reminder_date.astimezone(utc)

            print(
                self.scheduler.add_job(
                    self.send_reminder,
                    trigger="date",
                    next_run_time=utc_reminder_date + timedelta(hours=4),
                    args=[reminder.to_number, reminder.content, reminder],
                )
            )
