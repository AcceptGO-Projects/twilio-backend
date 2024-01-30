from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.helpers.date_formater import format_date_to_spanish_utc4
from app.schemas.lead import Lead
from app.schemas.lead_reminder_response import LeadReminderResponse
from app.schemas.lead_response import LeadResponse
from app.services.lead_service import LeadService
from app.services.twilio_service import TwilioService
from app.services.scheduler_service import SchedulerService
from app.config.config import get_settings
from app.templates.messages_templates import get_welcome_message

class LeadController:
    def __init__(self, get_db, lead_service: LeadService, twilio_service:TwilioService, scheduler_service:SchedulerService):
        self.router = APIRouter()
        self.get_db = get_db
        self.lead_service = lead_service
        self.twilio_service = twilio_service
        self.scheduler_service = scheduler_service
        self.register_routes()

    def register_routes(self):
        @self.router.post("/register", status_code=201)
        async def register_lead(lead_data: Lead, db: Session = Depends(self.get_db)):
            lead, event, lead_event = self.lead_service.register_lead(lead_data)
            self.twilio_service.send_message(lead_data.phone, get_welcome_message(lead_data.first_name, format_date_to_spanish_utc4(lead_data.event_date)))
            self.scheduler_service.schedule_reminders(lead_data, lead_data.event_date, lead_event.id)

            return {"status": "success", "lead_id": lead.id, "event_id": event.id}
        
        @self.router.get("", response_model=List[LeadResponse])
        async def get_all_leads(db: Session = Depends(self.get_db)):
            leads = self.lead_service.get_all_leads_with_events()
            return leads

        @self.router.get("/event/{event_id}", response_model=List[LeadResponse])
        async def get_leads_for_event(event_id: int, db: Session = Depends(self.get_db)):
            leads = self.lead_service.get_leads_by_event(event_id)
            return leads
        
        @self.router.get("/reminders/status", response_model=List[LeadReminderResponse])
        async def get_lead_reminder_statuses(db: Session = Depends(self.get_db)):
            return self.lead_service.get_lead_reminder_statuses()
