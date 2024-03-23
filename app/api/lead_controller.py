from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.data_source import get_db
from app.repositories.evente_reminder_repository import EventReminderRepository
from app.repositories.lead_repository import LeadRepository
from app.repositories.event_repository import EventRepository
from app.repositories.lead_event_repository import LeadEventRepository
from app.repositories.reminder_repository import ReminderRepository
from app.services.lead_service import LeadService
from app.schemas.lead import Lead
from app.schemas.lead_response import LeadResponse
from app.schemas.lead_reminder_response import LeadReminderResponse
from app.services.scheduler_service import SchedulerService
from app.services.twilio_service import TwilioService



router = APIRouter()

async def get_lead_service(db: AsyncSession = Depends(get_db)) -> LeadService:
    lead_repo = LeadRepository(db)
    event_repo = EventRepository(db)
    lead_event_repo = LeadEventRepository(db)
    reminder_repo = ReminderRepository(db)
    event_reminder_repo = EventReminderRepository(db)
    

    twilio_service = TwilioService() 
    scheduler_service = SchedulerService(twilio_service=twilio_service, reminder_repo=reminder_repo)
    
    await scheduler_service.start()

    return LeadService(
        lead_repo=lead_repo, 
        event_repo=event_repo, 
        lead_event_repo=lead_event_repo, 
        event_reminder_repo=event_reminder_repo,
        twilio_service=twilio_service, 
        scheduler_service=scheduler_service
    )

@router.post("/register", status_code=201)
async def register_lead(lead_data: Lead, lead_service: LeadService = Depends(get_lead_service)):
    lead = await lead_service.register_lead(lead_data)
    return {"status": "success", "lead_id": lead.id}

@router.get("", response_model=list[LeadResponse])
async def get_all_leads(lead_service: LeadService = Depends(get_lead_service)):
    leads = await lead_service.get_all_leads_with_events()
    return [LeadResponse.from_model(lead) for lead in leads]


@router.get("/event/{event_id}", response_model=list[LeadResponse])
async def get_leads_for_event(event_id: int, lead_service: LeadService = Depends(get_lead_service)):
    leads = await lead_service.get_leads_by_event(event_id)
    return leads
        
@router.get("/reminders/status", response_model=list[LeadReminderResponse])
async def get_lead_reminder_statuses(lead_service: LeadService = Depends(get_lead_service)):
    return await lead_service.get_lead_reminder_statuses()