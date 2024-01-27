from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from app.models.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    lead_event_id = Column(Integer, ForeignKey('lead_events.id'))
    content = Column(String(1024))
    reminder_date = Column(DateTime)
    sent = Column(Boolean, default=False)

    lead_event = relationship("LeadEvent", back_populates="reminders")
