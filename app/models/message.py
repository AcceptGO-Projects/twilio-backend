from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from app.models.base import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(String(255), index=True)
    content = Column(String(1024))
    sent_at = Column(DateTime, default=datetime.utcnow)
    is_successful = Column(Boolean)
    error_message = Column(String(1024), nullable=True)
