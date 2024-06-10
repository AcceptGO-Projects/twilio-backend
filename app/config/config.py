from functools import cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "Backend Python FastAPI and Twilio"
    k_revision: str = "local"
    log_level: str = "DEBUG"
    twilio_auth_token: str
    twilio_account_ssid: str
    twilio_number: str

    database_url: str = 'mysql://root:root@localhost:3306/leads_db'

    class Config:
        env_file = ".env"

@cache
def get_settings():
    return Settings() 