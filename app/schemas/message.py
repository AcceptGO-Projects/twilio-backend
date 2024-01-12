from pydantic import BaseModel
from datetime import datetime

class MessageSchema(BaseModel):
    id: int
    recipient: str
    content: str
    sent_at: datetime
    is_successful: bool
    error_message: str = ""

    class Config:
        orm_mode = True
