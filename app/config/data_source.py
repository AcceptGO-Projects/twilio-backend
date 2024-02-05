from typing import AsyncGenerator
from sqlalchemy import create_engine

from app.models.lead import Lead
from app.models.message import Message
from app.models.event import Event
from app.models.lead_event import LeadEvent
from app.models.reminder import Reminder 

from app.config.config import get_settings
from app.models.base import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = get_settings().database_url

engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


