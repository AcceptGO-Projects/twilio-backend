import os
from twilio.rest import Client
from fastapi import HTTPException
from app.config.config import get_settings
from fastapi import FastAPI
from app.api.router import router as api_router
from fastapi.middleware.cors import CORSMiddleware

_SETTINGS = get_settings()

app = FastAPI(
    title=_SETTINGS.service_name,
    version=_SETTINGS.k_revision
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(api_router)

def get_twilio_credentials():
    account_sid = _SETTINGS.twilio_account_ssid
    auth_token = _SETTINGS.twilio_auth_token
    twilio_number = _SETTINGS.twilio_number
    print(account_sid,auth_token, twilio_number)
    if not all([account_sid, auth_token, twilio_number]):
        raise HTTPException(status_code=500, detail="Twilio credentials are not set")
    return account_sid, auth_token, twilio_number

def get_twilio_client():
    account_sid, auth_token, _ = get_twilio_credentials()
    return Client(account_sid, auth_token)

def get_twilio_number() -> str:
    _, _, twilio_number = get_twilio_credentials()
    return twilio_number

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)