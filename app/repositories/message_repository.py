from sqlalchemy import select
from app.models.message import Message

class MessageRepository:
    def __init__(self, get_db):
        self.get_db = get_db

    async def add_message(self, recipient: str, content: str, is_successful: bool, error_message: str = ""):
        async with self.get_db() as db:
            new_message = Message(recipient=recipient, content=content, is_successful=is_successful, error_message=error_message)
            db.add(new_message)
            await db.commit()
            await db.refresh(new_message)
            return new_message

    async def get_messages(self):
        async with self.get_db() as db:
            result = await db.execute(
                select(Message)
            )
            return result.scalars().all()
    
    async def get_message_by_id(self, message_id: int):
        async with self.get_db() as db:
            result = await db.execute(
                select(Message).filter(Message.id == message_id)
            )
            return result.scalars().first()