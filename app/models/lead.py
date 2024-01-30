from sqlalchemy import Column,Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from app.models.base import Base

class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    country = Column(String(255))
    phone = Column(String(15))

    events = relationship("LeadEvent", back_populates="lead")