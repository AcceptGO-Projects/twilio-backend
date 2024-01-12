from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    country = Column(String(255))
    phone = Column(String(15))
    event_date = Column(DateTime)
    registered_at = Column(DateTime, default=datetime.utcnow)