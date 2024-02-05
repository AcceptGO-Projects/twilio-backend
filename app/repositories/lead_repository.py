from sqlalchemy import case, func, select
from sqlalchemy.orm import joinedload
from app.models.event import Event
from app.models.lead import Lead
from app.models.lead_event import LeadEvent
from app.models.reminder import Reminder

class LeadRepository:
    def __init__(self, get_db):
        self.get_db = get_db

    async def add_lead(self, new_lead: Lead):
        async for db in self.get_db():
            db.add(new_lead)
            await db.commit()
            await db.refresh(new_lead)
            return new_lead

    async def find_lead_by_email_or_phone(self, email: str, phone: str):
        async for db in self.get_db():
            result = await db.execute(
                select(Lead).filter(
                    (Lead.email == email) | (Lead.phone == phone)
                )
            )
            return result.scalars().first()
            

    async def get_all_leads_with_events(self):
        async for db in self.get_db():
            result = await db.execute(
                select(Lead).options(joinedload(Lead.events).joinedload(LeadEvent.event))
            )
            return result.scalars().all()
            

    async def get_leads_by_event(self, event_id: int):
        async for db in self.get_db():
            result = await db.execute(
                select(
                    Lead.first_name, 
                    Lead.last_name, 
                    Lead.email, 
                    Lead.country, 
                    Lead.phone,
                    Event.name.label("event_name"),
                    LeadEvent.registered_at
                ).select_from(Lead).join(LeadEvent).join(Event).filter(LeadEvent.event_id == event_id).distinct()
            )
            return result.all()


    async def get_lead_reminder_status(self):
        async for db in self.get_db():
            subquery = select(
                Reminder.lead_event_id,
                func.row_number().over(
                    partition_by=Reminder.lead_event_id,
                    order_by=Reminder.reminder_date
                ).label('reminder_order'),
                Reminder.sent
            ).subquery()

            result = await db.execute(
                select(
                    Lead.first_name,
                    Lead.last_name,
                    Lead.email,
                    Lead.country,
                    Lead.phone,
                    Event.name.label('event_name'),
                    LeadEvent.registered_at,
                    func.max(case((subquery.c.reminder_order == 1, subquery.c.sent), else_=False)).label("reminder_1_status"),
                    func.max(case((subquery.c.reminder_order == 2, subquery.c.sent), else_=False)).label("reminder_2_status"),
                    func.max(case((subquery.c.reminder_order == 3, subquery.c.sent), else_=False)).label("reminder_3_status")
                ).select_from(LeadEvent).join(
                    Lead, LeadEvent.lead_id == Lead.id
                ).join(
                    Event, LeadEvent.event_id == Event.id
                ).join(
                    subquery, subquery.c.lead_event_id == LeadEvent.id, isouter=True
                ).group_by(
                    Lead.id, Event.id, LeadEvent.id
                )
            )
            return result.all()
            
