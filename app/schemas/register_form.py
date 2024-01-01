from pydantic import BaseModel, EmailStr, constr
import datetime as dt

class RegisterForm(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    email: EmailStr
    country: constr(strip_whitespace=True, min_length=2)
    phone: constr(strip_whitespace=True, min_length=1)
    experience: constr(strip_whitespace=True)
    search: constr(strip_whitespace=True)
    career: constr(strip_whitespace=True)
    message: constr(strip_whitespace=True, min_length=1)
    accept_notifications: bool
    event_date: dt.datetime
