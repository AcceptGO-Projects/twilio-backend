from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.models.event_reminder import EventReminder  # Adjust the import path as needed

class EventReminderRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_welcome_message_by_event_id(self, event_id: int) -> EventReminder:
        """
        Fetch the welcome message for a given event ID.
        """
        query = select(EventReminder).where(
            EventReminder.event_id == event_id,
            EventReminder.index == 0  # Assuming index 0 for welcome messages
        )
        result = await self.db.execute(query)
        return result.scalars().first()

    async def get_reminders_by_event_id(self, event_id: int) -> List[EventReminder]:
        """
        Fetch all reminders for a given event ID, excluding the welcome message.
        """
        query = select(EventReminder).where(
            EventReminder.event_id == event_id,
            EventReminder.index > 0  
        ).order_by(EventReminder.index)
        result = await self.db.execute(query)
        return result.scalars().all() # type: ignore
