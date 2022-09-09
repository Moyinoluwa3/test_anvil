from typing import Any,Optional
from datetime import datetime
from pydantic import BaseModel,EmailStr,validator
from enum import Enum

from sqlalchemy import VARCHAR


class Gender(str,Enum):
    MALE = "Male"
    FEMALE = "Female"

class TeacherIn(BaseModel):
    first_name : str
    last_name : str
    name : str
    gender : Gender
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
    gender: Gender
    Class : str
    Date_of_birth : str
    password : str
    subject_1 : str
    subject_2: str
    subject_3: str
    subject_4: str
    subject_5: str
    subject_6: str
    subject_7: str  
    subject_8: str
    subject_9: str
    subject_10: str


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
    gender: Gender
    Date_of_birth : str
    Class : str
    admission_no : int

    
    class Config:
        orm_mode = True

class ResultIn(BaseModel):
    admission_no :int
    name : str
    gender : Gender
    Date_of_birth : str
    Class : str
    email: EmailStr

    Mathematics_test : int
    Mathematics_exams: int
    Mathematics_total : int
    M_Remarks  : str
    M_Grade : str
    English_test : int
    English_exams : int
    English_total : int
    E_Remarks: str
    E_Grade: str
    physics_test : int
    physics_exams : int
    physics_total : int
    P_Remarks : str
    P_Grade : str
    biology_test : int
    biology_exams: int
    biology_total: int
    B_Remarks : str
    B_Grade : str
    geography_test: int
    geography_exams : int
    geography_total : int
    G_Remarks : str 
    G_Grade : str
    chemistry_text: int
    chemistry_exams : int
    chemistry_total : int
    C_Remarks: str
    C_Grade : str
    furthermaths_test : int
    furthermaths_exams: int
    furthermaths_total: int
    F_Remarks : str
    F_Grade : str
    yoruba_test : int
    yoruba_exams : int
    youruba_total : int
    Y_Remarks : str
    Y_Grade : str
    civic_test : int
    civic_exams : int
    civic_total : int
    CI_Remarks : str
    CI_Grade : str
    dp_test : int
    dp_exams : int
    dp_total : int
    D_Remarks : str
    D_Grade : str
    term : str
    Class: str
    average : int
    position : str
    overall_position : str
    resumption: str
    
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
