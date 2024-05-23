from typing import List, Tuple
from app.helpers.reminder_factory import replace_message_with_name
from app.models.lead import Lead
from app.models.lead_event import LeadEvent
from app.repositories.event_repository import EventRepository
from app.repositories.evente_reminder_repository import EventReminderRepository
from app.repositories.lead_event_repository import LeadEventRepository
from app.repositories.lead_repository import LeadRepository
from app.schemas.lead import Lead as LeadSchema
from app.schemas.lead_response import LeadResponse
from app.schemas.lead_reminder_response import LeadReminderResponse
from app.services.scheduler_service import SchedulerService
from app.services.twilio_service import TwilioService

class LeadService:
    def __init__(
        self, 
        lead_repo: LeadRepository, 
        event_repo: EventRepository, 
        lead_event_repo: LeadEventRepository, 
        event_reminder_repo: EventReminderRepository,
        twilio_service: TwilioService, 
        scheduler_service: SchedulerService,
    ):
        self.lead_repo = lead_repo
        self.event_repo = event_repo
        self.lead_event_repo = lead_event_repo
        self.twilio_service = twilio_service
        self.scheduler_service = scheduler_service
        self.event_reminder_repo = event_reminder_repo 

    async def register_lead(self, lead_data: LeadSchema) -> Lead:
        lead = await self.lead_repo.find_lead_by_email_or_phone(
            email=lead_data.email, phone=lead_data.phone
        )
        
        if not lead:
            new_lead = Lead(
                first_name=lead_data.first_name,
                last_name=lead_data.last_name,
                email=lead_data.email,
                country=lead_data.country,
                phone=lead_data.phone
            )
            lead =await self.lead_repo.add_lead(new_lead)

        lead_event = await self.lead_event_repo.add_lead_event(
            LeadEvent(lead_id=lead.id, event_id=lead_data.event_id)
        )
        
        welcome_messages_record = await self.event_reminder_repo.get_welcome_messages_by_event_id(lead_data.event_id)

        for welcome_message_record in welcome_messages_record:
            welcome_message = replace_message_with_name(welcome_message_record.message,lead_data.first_name) # type: ignore
            await self.twilio_service.send_message(lead_data.phone, welcome_message)
        
        reminders_record = await self.event_reminder_repo.get_reminders_by_event_id(lead_data.event_id)

        await self.scheduler_service.schedule_reminders(lead_name=lead_data.first_name, lead_phone=lead_data.phone, lead_event_id= lead_event.id ,event_reminders= reminders_record) # type: ignore

        return lead

    
    async def get_all_leads_with_events(self) -> List[LeadResponse]:
        leads = await self.lead_repo.get_all_leads_with_events()
        return [LeadResponse.from_model(lead) for lead in leads]

    async def get_leads_by_event(self, event_id: int) -> List[LeadResponse]:
        leads = await self.lead_repo.get_leads_by_event(event_id)
        return [LeadResponse.from_model(lead_tuple) for lead_tuple in leads]

    async def get_lead_reminder_statuses(self) -> List[LeadReminderResponse]:
        lead_reminder_statuses = await self.lead_repo.get_lead_reminder_status()
        return [LeadReminderResponse.from_model(lead_status_tuple) for lead_status_tuple in lead_reminder_statuses]