from datetime import datetime
from sqlalchemy.orm import Session
from app.models.event import Event

class EventRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_event_by_name_and_date(self, name: str, event_date: datetime):
        return self.db_session.query(Event).filter(
            Event.name == name,
            Event.event_date == event_date
        ).first()
    
    def add_event(self, new_event: Event):
        self.db_session.add(new_event)
        self.db_session.commit()
        return new_event
