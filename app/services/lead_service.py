from typing import List
from app.models.event import Event
from app.models.lead import Lead
from app.models.lead_event import LeadEvent
from app.repositories.event_repository import EventRepository
from app.repositories.lead_event_repository import LeadEventRepository
from app.repositories.lead_repository import LeadRepository
from app.schemas.lead import Lead as LeadSchema
from app.schemas.lead_response import LeadResponse

class LeadService:
    def __init__(self, lead_repo: LeadRepository, event_repo: EventRepository, lead_event_repo: LeadEventRepository):
        self.lead_repo = lead_repo
        self.event_repo = event_repo
        self.lead_event_repo = lead_event_repo

    def register_lead(self, lead_data: LeadSchema):
        lead = self.lead_repo.find_lead_by_email_or_phone(
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
            lead = self.lead_repo.add_lead(new_lead)

        event = self.event_repo.get_event_by_name_and_date(
            name=lead_data.event_name, event_date=lead_data.event_date
        )
        
        if not event:
            new_event = Event(
                name=lead_data.event_name,
                description=lead_data.event_description,
                event_date=lead_data.event_date
            )
            event = self.event_repo.add_event(new_event)

        lead_event = self.lead_event_repo.add_lead_event(
            LeadEvent(lead_id=lead.id, event_id=event.id)
        )

        return lead, event, lead_event

    
    def get_leads_by_event(self, event_id: int):
        leads = self.lead_repo.get_leads_by_event(event_id)
        return [self._convert_lead_to_response_by_event(lead) for lead in leads]
    
    def get_all_leads_with_events(self) -> List[LeadResponse]:
        leads = self.lead_repo.get_all_leads_with_events()
        return [self._convert_lead_to_response(lead) for lead in leads]

    def _convert_lead_to_response(self, lead) -> LeadResponse:
        return LeadResponse(
            first_name=lead.first_name,
            last_name=lead.last_name,
            email=lead.email,
            country=lead.country,
            phone=lead.phone,
            event_name=lead.events[0].event.name if lead.events else "",
            registered_at=lead.events[0].registered_at if lead.events else None # type: ignore
        )
    
    def _convert_lead_to_response_by_event(self, lead_tuple) -> LeadResponse:
        first_name, last_name, email, country, phone, event_name, registered_at = lead_tuple
        return LeadResponse(
            first_name=first_name,
            last_name=last_name,
            email=email,
            country=country,
            phone=phone,
            event_name=event_name,
            registered_at=registered_at
        )
