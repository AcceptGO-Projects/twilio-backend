from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class EventReminderSchema(BaseModel):
    index: int
    message: str
    reminder_time: datetime

class CreateEventRequest(BaseModel):
    name: str
    description: str
    event_date: datetime
    reminders: List[EventReminderSchema] = Field(default=[])
