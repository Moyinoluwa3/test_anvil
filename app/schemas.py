from typing import Any,Optional
from datetime import datetime
from pydantic import BaseModel,EmailStr,validator
from enum import Enum

from sqlalchemy import VARCHAR




class TeacherIn(BaseModel):
    first_name : str
    last_name : str
    name : str
    gender : str
    email : EmailStr
    Class: str
    subject: str
    password: str

class TeacherOut(BaseModel):
    id : int
    name : str
    Class: str
    email : str
    subject: str
    class Config:
        orm_mode = True


class ClassIn(BaseModel):
    name : str
    class_teacher : str


class Student_In(BaseModel):
    first_name : str
    last_name: str
    email : EmailStr
    gender: str
    Class : str
    Date_of_birth : str
    password : str


class SubjectIn(BaseModel):
   subject : str
   subject_teacher : str


class SubjectOut(BaseModel):
    id : int
    subject : str
    subject_teacher : str
    class Config:
        orm_mode = True
    
class StudentOut(BaseModel):
    first_name : str
    last_name: str
    email: EmailStr
    gender: str
    Date_of_birth : str
    Class : str
    admission_no : int
    
    class Config:
        orm_mode = True

    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[str] = None
class Email(BaseModel):
    email: EmailStr

class Password(BaseModel):
    password: str


class Admin(BaseModel):
    name : str
    password: str

class AdminOut(BaseModel):
    id : int
    name : str
    class Config:
        orm_mode = True
