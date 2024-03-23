from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from app.models.base import Base

class EventReminder(Base):
    __tablename__ = 'event_reminders'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    index = Column(Integer)
    message = Column(String(1024))
    reminder_time = Column(DateTime)
    
    event = relationship("Event", back_populates="reminders")