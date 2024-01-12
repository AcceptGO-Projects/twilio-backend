from sqlalchemy.orm import Session
from app.models.message import Message

class MessageRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_message(self, recipient: str, content: str, is_successful: bool, error_message: str = ""):
        new_message = Message(recipient=recipient, content=content, is_successful=is_successful, error_message=error_message)
        self.db_session.add(new_message)
        self.db_session.commit()
        return new_message

    def get_messages(self):
        return self.db_session.query(Message).all()
    
    def get_message_by_id(self, message_id: int):
        return self.db_session.query(Message).filter(Message.id == message_id).first()
