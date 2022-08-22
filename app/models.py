
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

