
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import TIMESTAMP, Column,Integer, String , Boolean,VARCHAR
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class Teachers(Base):
    __tablename__ = "Teachers"
    id = Column(Integer, primary_key= True , nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    name = Column(String,nullable=False,unique=True)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    Class = Column(String,nullable=False,unique=True)
    subject = Column(String,nullable= False,unique=True)
    image = Column(String)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) 


class Classes(Base):
    __tablename__ = "Classes"
    id = Column(Integer, primary_key= True , nullable=False)
    name = Column(String,nullable=False,unique=True)
    class_teacher = Column(String,nullable=False)

class Students(Base):
    __tablename__ = "Students"
    id = Column(Integer, primary_key= True , nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String,nullable=False,unique=True)
    gender = Column(String, nullable=False)
    admission_no = Column(Integer,nullable=False,unique = True)
    Date_of_birth = Column(String,nullable=False)
    Class = Column(String,nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) 


class Subjects(Base):
    __tablename__ = "Subjects"
    id = Column(Integer, primary_key=True,nullable=False)
    subject = Column(String,nullable=False,unique=True)
    subject_teacher = Column(String,nullable=False)

    

class Admin(Base):
    __tablename__= "admins"
    id = Column(Integer, primary_key= True , nullable=False)
    name = Column(String, nullable=False)
    password= Column(String, nullable=False)

class Results(Base):
    __tablename__= "results"
    id = Column(Integer, primary_key=True,nullable=False)
    admission_no = Column(Integer,ForeignKey("Students.admission_no", ondelete="CASCADE"))
    email = Column(String,nullable=False)
    Mathematics_test = Column(Integer)
    Mathematics_exams = Column(Integer)
    Mathematics_total =  Column(Integer)
    English_test = Column(Integer)
    English_exams = Column(Integer)
    English_total =  Column(Integer)
    physics_test = Column(Integer)
    physics_exams =Column(Integer)
    physics_total =  Column(Integer)
    biology_test = Column(Integer)
    biology_exams = Column(Integer)
    biology_total =  Column(Integer)
    geography_test = Column(Integer)
    geography_exams = Column(Integer)
    geography_total =  Column(Integer)
    chemistry_text = Column(Integer)
    chemistry_exams = Column(Integer)
    chemistry_total =  Column(Integer)
    furthermaths_test = Column(Integer)
    furthermaths_exams = Column(Integer)
    furthermaths_total =  Column(Integer)
    yoruba_test = Column(Integer)
    yoruba_exams = Column(Integer)
    youruba_total =  Column(Integer)
    civic_test = Column(Integer)
    civic_exams = Column(Integer)
    civic_total =  Column(Integer)
    dp_test = Column(Integer)
    dp_exams = Column(Integer)
    dp_total = Column(Integer)
    term = Column(String)
    Class = Column(String)
    average = Column(Integer)