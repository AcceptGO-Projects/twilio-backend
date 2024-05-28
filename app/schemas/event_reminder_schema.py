from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class EventReminderSchema(BaseModel):
    index: int
    message: str
    reminder_time: datetime
    is_welcome: bool

class CreateEventRequest(BaseModel):
    name: str
    description: str
    event_date: datetime
    reminders: List[EventReminderSchema]
