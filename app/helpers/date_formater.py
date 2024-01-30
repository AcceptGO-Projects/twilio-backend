from datetime import datetime
from datetime import datetime,timedelta,timezone
from babel.dates import format_datetime

def format_date_to_spanish_utc4(date_utc0: datetime) -> str:
    date_utc4 = date_utc0.astimezone(timezone(timedelta(hours=-4)))
    
    formatted_date = format_datetime(date_utc4, "EEEE d 'de' MMMM", locale='es')

    return formatted_date.capitalize()