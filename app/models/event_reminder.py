from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, DateTime, false
from sqlalchemy.orm import relationship

from app.models.base import Base

class EventReminder(Base):
    __tablename__ = 'event_reminders'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    index = Column(Integer)
    message = Column(String(1024))
    reminder_time = Column(DateTime)
    is_welcome = Column(Boolean, default=false)
    
    event = relationship("Event", back_populates="reminders")