from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from app.models.base import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(1024))
    event_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    leads = relationship("LeadEvent", back_populates="event")