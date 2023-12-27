# En app/services/scheduler_service.py

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app.services.twilio_services import send_registration_message
from app.schemas.register_form import RegisterForm

scheduler = BackgroundScheduler()
scheduler.start()

def programar_recordatorios(form_data: RegisterForm, evento_hora: datetime):
    horarios_recordatorios = [
        evento_hora - timedelta(minutes=1),
        evento_hora - timedelta(minutes=2),
        evento_hora - timedelta(minutes=3)
    ]

    print(scheduler)

    for horario in horarios_recordatorios:
        scheduler.add_job(
            enviar_recordatorio,
            'date',
            run_date=horario,
            args=[form_data, "Your package has been shipped. It will be delivered in 1 business days."]
        )

def enviar_recordatorio(form_data: RegisterForm, mensaje: str):
    # Reutiliza la función de enviar mensajes de Twilio
    try:
        send_registration_message(form_data, mensaje)
    except Exception as e:
        # Aquí puedes manejar los errores o registrarlos
        print(f"Error al enviar el recordatorio: {e}")
