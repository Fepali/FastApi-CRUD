import email
from mailbox import NoSuchMailboxError
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    contraseña: str