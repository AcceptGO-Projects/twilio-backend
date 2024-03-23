from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeadResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    country: str
    phone: str
    event_name: str
    registered_at: Optional[datetime] = None

    @classmethod
    def from_model(cls, lead, lead_event=None):
        return cls(
            first_name=lead.first_name,
            last_name=lead.last_name,
            email=lead.email,
            country=lead.country,
            phone=lead.phone,
            event_name=lead_event.event.name if lead_event and lead_event.event else "",
            registered_at=lead_event.registered_at if lead_event else None
        )
