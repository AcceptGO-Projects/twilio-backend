from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.lead_event import LeadEvent

class LeadEventRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_lead_event(self, new_lead_event: LeadEvent) -> LeadEvent:
        self.db.add(new_lead_event)
        await self.db.commit()
        await self.db.refresh(new_lead_event)
        return new_lead_event