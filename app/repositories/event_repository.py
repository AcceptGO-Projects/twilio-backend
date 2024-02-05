from datetime import datetime
from sqlalchemy import select
from app.models.event import Event

class EventRepository:
    def __init__(self, get_db):
        self.get_db = get_db

    async def get_event_by_name_and_date(self, name: str, event_date: datetime):
        async for db in self.get_db():
            result = await db.execute(
                select(Event).filter(
                    Event.name == name,
                    Event.event_date == event_date
                )
            )
            return result.scalars().first()
            break  # Asegura salir después de la primera iteración.

    async def add_event(self, new_event: Event):
        async for db in self.get_db():
            db.add(new_event)
            await db.commit()
            await db.refresh(new_event)
            return new_event
            break  # Asegura salir después de la primera iteración.
