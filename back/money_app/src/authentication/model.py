import orjson
from pydantic import BaseModel, ValidationError

def validate_dict(response: bytes, Model: type[BaseModel]):
    try:
        data = Model(**orjson.loads(response))
        return data
    except ValidationError as e:
        return None

class AuthLogin(BaseModel):
    username: str 
    password: str

class AuthRegister(AuthLogin):
    email: str

class AuthRefresh(BaseModel):
    refresh: str

class AuthAccess(BaseModel):
    access: str
