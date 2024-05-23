from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.data_source import get_db

from app.models.event import Event
from app.models.event_reminder import EventReminder

from sqlalchemy.orm import Session

from app.schemas.event_reminder_schema import CreateEventRequest

router = APIRouter()

@router.post("", response_model=CreateEventRequest, status_code=status.HTTP_201_CREATED)
async def create_event(event_request: CreateEventRequest, db: Session = Depends(get_db)):
    new_event = Event(
        name=event_request.name,
        description=event_request.description,
        event_date=event_request.event_date
    )
    db.add(new_event)
    await db.commit()
    await db.refresh(new_event)

    for reminder in event_request.reminders:
        new_reminder = EventReminder(
            event_id=new_event.id,
            index=reminder.index,
            message=reminder.message,
            reminder_time=reminder.reminder_time,
            is_welcome=reminder.is_welcome
        )
        db.add(new_reminder)
    await db.commit()

    return event_request
