from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.message import MessageSchema
from app.repositories.message_repository import MessageRepository
from app.services.message_service import MessageService

class MessageController:
    def __init__(self, message_service: MessageService):
        self.router = APIRouter()
        self.message_service = message_service
        self.register_routes()

    def register_routes(self):
        @self.router.get("", response_model=List[MessageSchema])
        async def get_messages():
            return await self.message_service.get_all_messages()

        @self.router.get("/{message_id}", response_model=MessageSchema)
        async def get_message(message_id: int):
            return await self.message_service.get_message_by_id(message_id)
