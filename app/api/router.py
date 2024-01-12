from typing import List
from fastapi import APIRouter, Depends
from app.config.config import get_settings
from app.repositories.lead_repository import LeadRepository
from app.schemas.message import MessageSchema
from app.schemas.lead import Lead
from app.services.lead_service import LeadService
from app.services.message_service import MessageService
from app.services.scheduler_service import SchedulerService
from app.services.twilio_service import TwilioService
from app.templates.messages_templates import get_welcome_message

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.repositories.message_repository import MessageRepository
from app.models.message import Base
from app.models.lead import Base as LeadBase

from sqlalchemy.orm import Session


router = APIRouter()

_SETTINGS = get_settings()

engine = create_engine(_SETTINGS.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
LeadBase.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/register", status_code=201)
async def register_user(lead_data: Lead, db: Session = Depends(get_db)):
    lead_repo = LeadRepository(db)
    lead_service = LeadService(lead_repo)
    lead = lead_service.register_lead(lead_data)
    
    message_repo = MessageRepository(db)
    twilio_service = TwilioService(_SETTINGS, message_repo)
    scheduler_service = SchedulerService(twilio_service)
    twilio_service.send_message(lead_data, get_welcome_message(lead_data.name))
    scheduler_service.schedule_reminders(lead_data, lead_data.event_date)
    return {"status": "success", "lead_id": lead.id}

@router.get("/messages", response_model=List[MessageSchema])  # Ajusta MessageSchema según tu modelo
async def get_messages(db: Session = Depends(get_db)):
    message_repo = MessageRepository(db)
    message_service = MessageService(message_repo)
    return message_service.get_all_messages()


@router.get("/messages/{message_id}", response_model=MessageSchema)  # Ajusta MessageSchema según tu modelo
async def get_message(message_id: int, db: Session = Depends(get_db)):
    message_repo = MessageRepository(db)
    message_service = MessageService(message_repo)
    return message_service.get_message_by_id(message_id)