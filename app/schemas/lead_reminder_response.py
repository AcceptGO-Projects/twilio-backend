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
    reminder_1_status: Optional[bool] = None
    reminder_2_status: Optional[bool] = None
    reminder_3_status: Optional[bool] = None

    @classmethod
    def from_model(cls, lead_status_tuple):
        (
            first_name, last_name, email, country, phone,
            event_name, event_date,
            reminder_1_status, reminder_2_status, reminder_3_status
        ) = lead_status_tuple
        return cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            country=country,
            phone=phone,
            event_name=event_name,
            event_date=event_date,
            reminder_1_status=reminder_1_status,
            reminder_2_status=reminder_2_status,
            reminder_3_status=reminder_3_status
        )