from app.models.lead import Lead
from app.models.message import Message
from app.models.event import Event
from app.models.lead_event import LeadEvent
from app.models.reminder import Reminder 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker

from app.config.config import get_settings
from app.models.base import Base

DATABASE_URL = get_settings().database_url

engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = sessionmaker(
    engine, # type: ignore
    expire_on_commit=False,
    class_=AsyncSession
)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as session: # type: ignore
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()


    


