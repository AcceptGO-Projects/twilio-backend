from sqlalchemy.orm import Session
from app.models.lead_event import LeadEvent

class LeadEventRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def add_lead_event(self, new_lead_event: LeadEvent):
        self.db_session.add(new_lead_event)
        self.db_session.commit()
        return new_lead_event
