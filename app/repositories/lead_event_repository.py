from sqlalchemy.future import select
from app.models.lead_event import LeadEvent

class LeadEventRepository:
    def __init__(self, get_db):
        self.get_db = get_db

    async def add_lead_event(self, new_lead_event: LeadEvent):
        async for db in self.get_db():
            db.add(new_lead_event)
            await db.commit()
            await db.refresh(new_lead_event)
            return new_lead_event
            break  # Asegura salir después de la primera iteración.
