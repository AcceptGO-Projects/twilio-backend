from pydantic import BaseModel, EmailStr, StringConstraints
import datetime as dt
from typing_extensions import Annotated

class Lead(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    email: EmailStr
    country: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2)]
    phone: Annotated[str, StringConstraints(strip_whitespace=True, min_length=8, max_length=15, pattern=r'^\+\d+$')]
    event_date: dt.datetime

    class Config:
        orm_mode = True