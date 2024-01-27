from pydantic import BaseModel
from datetime import datetime

class LeadResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    country: str
    phone: str
    event_name: str
    registered_at: datetime

    class Config:
        from_attributes = True