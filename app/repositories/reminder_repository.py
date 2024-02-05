from app.models.reminder import Reminder
from sqlalchemy.future import select
from datetime import datetime

class ReminderRepository:
    def __init__(self, get_db):
        self.get_db = get_db

    async def add_reminder(self, lead_event_id: int, to_number: str, content: str, reminder_date: datetime):
        async for db in self.get_db():
            new_reminder = Reminder(
                lead_event_id=lead_event_id,
                to_number=to_number,
                content=content,
                reminder_date=reminder_date
            )
            db.add(new_reminder)
            await db.commit()
            await db.refresh(new_reminder)
            return new_reminder
            break

    async def update_reminder(self, reminder_id: int, new_content: str, new_reminder_date: datetime):
        async for db in self.get_db():
            result = await db.execute(
                select(Reminder).filter(Reminder.id == reminder_id)
            )
            reminder = result.scalars().first()
            if reminder:
                reminder.content = new_content
                reminder.reminder_date = new_reminder_date
                await db.commit()
                return reminder
            break

    async def get_reminders_by_lead_event(self, lead_event_id: int):
        async for db in self.get_db():
            result = await db.execute(
                select(Reminder).filter(Reminder.lead_event_id == lead_event_id)
            )
            return result.scalars().all()
            break

    async def get_pending_reminders(self):
        async for db in self.get_db():
            current_time = datetime.utcnow()
            result = await db.execute(
                select(Reminder).filter(
                    Reminder.sent == False,
                    Reminder.reminder_date > current_time
                )
            )
            return result.scalars().all()
            break

    async def mark_reminder_as_sent(self, reminder_id: int):
        async for db in self.get_db():
            result = await db.execute(
                select(Reminder).filter(Reminder.id == reminder_id)
            )
            reminder = result.scalars().first()
            if reminder:
                reminder.sent = True
                await db.commit()
                return reminder
            break
