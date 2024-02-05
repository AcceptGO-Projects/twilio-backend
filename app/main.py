from fastapi import FastAPI
from app.api.router import _SETTINGS, router as api_router
from fastapi.middleware.cors import CORSMiddleware

from app.config.data_source import create_tables


app = FastAPI(
    title=_SETTINGS.service_name,
    version=_SETTINGS.k_revision
)

@app.on_event("startup")
async def startup_event():
    await create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
