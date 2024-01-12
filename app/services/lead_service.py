from app.models.lead import Lead
from app.repositories.lead_repository import LeadRepository
from app.schemas.lead import Lead as LeadSchema

class LeadService:
    def __init__(self, lead_repo: LeadRepository):
        self.lead_repo = lead_repo

    def register_lead(self, lead_data: LeadSchema):
        new_lead = Lead(
            name=lead_data.name,
            email=lead_data.email,
            country=lead_data.country,
            phone=lead_data.phone,
            event_date=lead_data.event_date
        )
        return self.lead_repo.add_lead(new_lead)

