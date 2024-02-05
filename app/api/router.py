from fastapi import APIRouter

from app.api.lead_controller import LeadController
from app.api.message_controller import MessageController
from app.config.config import get_settings
from app.config.data_source import get_db

from app.repositories.event_repository import EventRepository
from app.repositories.lead_event_repository import LeadEventRepository
from app.repositories.lead_repository import LeadRepository
from app.repositories.message_repository import MessageRepository
from app.repositories.reminder_repository import ReminderRepository
from app.services.lead_service import LeadService
from app.services.message_service import MessageService
from app.services.scheduler_service import SchedulerService
from app.services.twilio_service import TwilioService

router = APIRouter()

_SETTINGS = get_settings()



event_repo = EventRepository(get_db)
lead_event_repo = LeadEventRepository(get_db)
lead_repo = LeadRepository(get_db)
message_repo = MessageRepository(get_db)
reminder_repo = ReminderRepository(get_db)

lead_service = LeadService(lead_repo,event_repo,lead_event_repo)
message_service = MessageService(message_repo)
twilio_service = TwilioService(_SETTINGS, message_repo)
scheduler_service = SchedulerService(twilio_service,reminder_repo)

lead_controller = LeadController( lead_service, twilio_service,scheduler_service)
message_controller = MessageController( message_service)


router.include_router(lead_controller.router, tags=["leads"], prefix='/leads')
router.include_router(message_controller.router, tags=["messages"],prefix='/messages')