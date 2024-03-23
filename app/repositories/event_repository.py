from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.event import Event

class EventRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_event(self, new_event: Event) -> Event:
        self.db.add(new_event)
        await self.db.commit()
        await self.db.refresh(new_event)
        return new_event

    async def get_event_by_id(self, event_id: int) -> Event:
        result = await self.db.execute(
            select(Event).filter(Event.id == event_id)
        )
        return result.scalars().first()