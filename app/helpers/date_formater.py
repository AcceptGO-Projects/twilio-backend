from datetime import datetime
import pytz
import locale
from datetime import datetime,timedelta,timezone
from babel.dates import format_date

def format_date_to_spanish_utc4(date_utc0: datetime) -> str:
    # Configurar locale a español
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    
    # Convertir la fecha de UTC-0 a UTC-4
    date_utc4 = date_utc0.astimezone(timezone(timedelta(hours=-4)))
    
    # Formatear la fecha
    formatted_date = format_date(date_utc4, "EEEE d 'de' MMMM", locale='es_ES')

    # Asegurar que el día de la semana comience con mayúscula
    return formatted_date.capitalize()