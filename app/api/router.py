from fastapi import APIRouter
from fastapi.params import Depends
from requests import Session
from app.api.lead_controller import LeadController
from app.api.message_controller import MessageController
from app.config.config import get_settings
from app.models.base import Base

from app.models.lead import Lead
from app.models.message import Message
from app.models.event import Event
from app.models.lead_event import LeadEvent
from app.models.reminder import Reminder 

from app.repositories.event_repository import EventRepository
from app.repositories.lead_event_repository import LeadEventRepository
from app.repositories.lead_repository import LeadRepository
from app.repositories.message_repository import MessageRepository
from app.repositories.reminder_repository import ReminderRepository
from app.services.lead_service import LeadService
from app.services.message_service import MessageService


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.services.scheduler_service import SchedulerService

from app.services.twilio_service import TwilioService

from sqlalchemy.orm import Session


router = APIRouter()

_SETTINGS = get_settings()

engine = create_engine(_SETTINGS.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db = SessionLocal()

lead_repo = LeadRepository(db)
event_repo = EventRepository(db)
lead_event_repo = LeadEventRepository(db)
reminder_repo = ReminderRepository(db)
message_repo = MessageRepository(db)


lead_service = LeadService(lead_repo, event_repo, lead_event_repo)
message_service = MessageService(message_repo)
twilio_service = TwilioService(_SETTINGS,message_repo)
scheduler_service = SchedulerService(twilio_service,reminder_repo)

lead_controller = LeadController(get_db, lead_service, twilio_service,scheduler_service)
message_controller = MessageController(get_db, message_service)


router.include_router(lead_controller.router, tags=["leads"], prefix='/leads')
router.include_router(message_controller.router, tags=["messages"],prefix='/messages')