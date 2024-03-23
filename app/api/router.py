from fastapi import APIRouter
from app.api.lead_controller import router as lead_router
from app.api.message_controller import router as message_router
from app.api.event_controller import router as event_router


api_router = APIRouter()

api_router.include_router(lead_router, tags=["leads"], prefix="/leads")
api_router.include_router(message_router, tags=["messages"], prefix="/messages")
api_router.include_router(event_router, tags=["events"], prefix="/events")

