from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from app.models.reminder import Reminder

class ReminderRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_reminder(self, lead_event_id: int, to_number: str, content: str, reminder_date: datetime) -> Reminder:
        new_reminder = Reminder(
            lead_event_id=lead_event_id,
            to_number=to_number,
            content=content,
            reminder_date=reminder_date
        )
        self.db.add(new_reminder)
        await self.db.commit()
        await self.db.refresh(new_reminder)
        return new_reminder

    async def mark_reminder_as_sent(self, reminder_id: int) -> None:
        result = await self.db.execute(
            select(Reminder).filter(Reminder.id == reminder_id)
        )
        reminder = result.scalars().first()
        if reminder:
            reminder.sent = True # type: ignore
            await self.db.commit()

    async def get_pending_reminders(self):
        current_time = datetime.utcnow()
        result = await self.db.execute(
            select(Reminder).filter(
                Reminder.sent == False,
                Reminder.reminder_date > current_time
            )
        )
        return result.scalars().all()
