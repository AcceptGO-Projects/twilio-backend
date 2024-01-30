from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base

class LeadEvent(Base):
    __tablename__ = 'lead_events'

    id = Column(Integer, primary_key=True)
    lead_id = Column(Integer, ForeignKey('leads.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    registered_at = Column(DateTime, default=datetime.utcnow)

    lead = relationship("Lead", back_populates="events")
    event = relationship("Event", back_populates="leads")

    reminders = relationship("Reminder", back_populates="lead_event")
