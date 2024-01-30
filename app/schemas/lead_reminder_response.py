from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LeadReminderResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    country: str
    phone: str
    event_name: str
    event_date: datetime
    reminder_1_status: Optional[bool]
    reminder_2_status: Optional[bool]
    reminder_3_status: Optional[bool]

    class Config:
        from_attributes = True