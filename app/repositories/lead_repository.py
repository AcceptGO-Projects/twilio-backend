from sqlalchemy.orm import Session
from app.models.event import Event
from app.models.lead import Lead
from app.models.lead_event import LeadEvent
from sqlalchemy.orm import joinedload

class LeadRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_lead(self, new_lead: Lead):
        self.db_session.add(new_lead)
        self.db_session.commit()
        return new_lead

    def find_lead_by_email_or_phone(self, email: str, phone: str):
        return self.db_session.query(Lead).filter(
            (Lead.email == email) | (Lead.phone == phone)
        ).first()
    
    def get_all_leads_with_events(self):
        return self.db_session.query(Lead).options(
            joinedload(Lead.events).joinedload(LeadEvent.event)
        ).all()

    def get_leads_by_event(self, event_id: int):
        return self.db_session.query(
            Lead.first_name, 
            Lead.last_name, 
            Lead.email, 
            Lead.country, 
            Lead.phone,
            Event.name.label("event_name"),
            LeadEvent.registered_at
        ).select_from(Lead).join(LeadEvent).join(Event).filter(LeadEvent.event_id == event_id).distinct().all()