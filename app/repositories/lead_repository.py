from sqlalchemy.orm import Session
from app.models.lead import Lead

class LeadRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_lead(self, new_lead: Lead):
        self.db_session.add(new_lead)
        self.db_session.commit()
        return new_lead
