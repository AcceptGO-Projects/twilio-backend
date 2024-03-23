# app/api/message_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.data_source import get_db
from app.repositories.message_repository import MessageRepository
from app.services.message_service import MessageService
from app.schemas.message import MessageSchema

router = APIRouter()

def get_message_service(db: AsyncSession = Depends(get_db)) -> MessageService:
    message_repo = MessageRepository(db)
    return MessageService(message_repo)

@router.get("", response_model=list[MessageSchema])
async def get_messages(message_service: MessageService = Depends(get_message_service)):
    return await message_service.get_all_messages()

@router.get("/{message_id}", response_model=MessageSchema)
async def get_message(message_id: int, message_service: MessageService = Depends(get_message_service)):
    return await message_service.get_message_by_id(message_id)

