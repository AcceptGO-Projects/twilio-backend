import os
from twilio.rest import Client
from fastapi import HTTPException
from app.config.config import get_settings
from fastapi import FastAPI
from app.api.router import router as api_router
from fastapi.middleware.cors import CORSMiddleware

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from app.services.send_messages import send_messages_from_csv  # Asegúrate de que esta es la ruta correcta


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
scheduler = AsyncIOScheduler()


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

@app.on_event("startup")
async def start_scheduler():
    custom_message = (
        '"¡Mañana es el día! 🥳\n'
        "Evaluación de potencial - Webinar AcceptGO 🚀\n\n"
        "¿Estás listo para conocer cómo sobresalir profesionalmente? 😃🙌🏻\n\n"
        "🗓 Te esperamos mañana a las 20:00 hrs 🇧🇴\n\n"
        "🔗 Te enviaremos el enlace de Zoom una hora antes del evento\n\n"
        "👉 Si deseas una evaluación personalizada en vivo para trabajos y becas internacionales 🌎, ten lista una oración de tu Currículum de la que te sientas orgulloso.\n\n"
        "Te esperamos con tu café online ☕ y tus mejores preguntas 😉.\n"
        "_____\n"
        "Ingresa con tu cámara encendida 📸 y tu nombre.\n"
        '"\n'
    )

    scheduler.add_job(
        send_messages_from_csv,
        trigger=CronTrigger(hour=17, minute=12),
        args=['trucho.csv', custom_message]
    )
    scheduler.start()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)