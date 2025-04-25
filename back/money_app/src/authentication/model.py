import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class AuthLogin(BaseModel):
    username: str 
    password: str

class AuthRegister(AuthLogin):
    email: str

class AuthRefresh(BaseModel):
    refresh: str

class AuthAccess(BaseModel):
    access: str
