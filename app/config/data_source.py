from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.api.router import _SETTINGS

from app.models.lead import Lead
from app.models.message import Message
from app.models.event import Event
from app.models.lead_event import LeadEvent

from app.models.base import Base


engine = create_engine(_SETTINGS.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()