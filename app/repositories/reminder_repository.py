from sqlalchemy.orm import Session
from app.models.reminder import Reminder
from app.models.lead_event import LeadEvent
from datetime import datetime

class ReminderRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_reminder(self, lead_event_id: int,to_number:str, content: str, reminder_date: datetime):
        new_reminder = Reminder(
            lead_event_id=lead_event_id,
            content=content,
            reminder_date=reminder_date,
            to_number=to_number
        )
        self.db_session.add(new_reminder)
        self.db_session.commit()
        return new_reminder

    def update_reminder(self, reminder_id: int, new_content: str, new_reminder_date: datetime):
        reminder = self.db_session.query(Reminder).filter(Reminder.id == reminder_id).first()
        if reminder:
            reminder.content = new_content
            reminder.reminder_date = new_reminder_date
            self.db_session.commit()
        return reminder

    def get_reminders_by_lead_event(self, lead_event_id: int):
        return self.db_session.query(Reminder).filter(Reminder.lead_event_id == lead_event_id).all()

    def get_pending_reminders(self):
        return self.db_session.query(Reminder).filter(
            Reminder.sent == False,
            Reminder.reminder_date > datetime.utcnow()
        ).all()

    def mark_reminder_as_sent(self, reminder_id: int):
        reminder = self.db_session.query(Reminder).filter(Reminder.id == reminder_id).first()
        if reminder:
            reminder.sent = True
            self.db_session.commit()
        return reminder
