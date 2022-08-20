from datetime import datetime
from typing import Optional,List
from unicodedata import category
from pydantic import BaseModel, EmailStr
from enum import Enum
from pydantic.types import conint

class Gender(str,Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOutput(BaseModel):
    id : int
    email : EmailStr
    account_number:  Optional[int] = None
    created_at: datetime
    class Config:
        orm_mode = True   

class UserLogin(BaseModel):
    email: EmailStr 
    password: str

class Email(BaseModel):
    email: EmailStr

class Password(BaseModel):
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[str] = None
