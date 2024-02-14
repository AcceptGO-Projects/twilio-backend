from pydantic import BaseModel, EmailStr, StringConstraints
import datetime as dt
from typing_extensions import Annotated

class Lead(BaseModel):
    first_name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    last_name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    email: EmailStr
    country: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2)]
    phone: Annotated[str, StringConstraints(strip_whitespace=True, min_length=8, max_length=15, pattern=r'^\+\d+$')]
    event_id: int 
    # event_name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    event_date: dt.datetime
    # event_description: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    class Config:
        from_attributes = True