from sqlalchemy import true
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.models.event_reminder import EventReminder  # Adjust the import path as needed

class EventReminderRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_welcome_messages_by_event_id(self, event_id: int) -> list[EventReminder]:
        """
        Fetch the welcome message for a given event ID.
        """
        query = select(EventReminder).where(
            EventReminder.event_id == event_id,
            EventReminder.is_welcome == True,
        ).order_by(EventReminder.index)
        result = await self.db.execute(query)
        return result.scalars().all()  # type: ignore

    async def get_reminders_by_event_id(self, event_id: int) -> list[EventReminder]:
        """
        Fetch all reminders for a given event ID, excluding the welcome message.
        """
        query = select(EventReminder).where(
            EventReminder.event_id == event_id,
            EventReminder.is_welcome == False, 
        ).order_by(EventReminder.index)
        result = await self.db.execute(query)
        return result.scalars().all() # type: ignore
