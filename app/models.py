
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
    subject_1 = Column(String)
    subject_2 = Column(String)
    subject_3 = Column(String)
    subject_4 = Column(String)
    subject_5 = Column(String)
    subject_6 = Column(String)
    subject_7 = Column(String)
    subject_8 = Column(String)
    subject_9 = Column(String)
    subject_10 = Column(String)



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
    admission_no = Column(Integer,nullable=False)
    name = Column(String,nullable=False)
    gender = Column(String, nullable=False)
    Date_of_birth = Column(String,nullable=False)
    Class = Column(String,nullable=False)
    email = Column(String,nullable=False)
    Mathematics_test = Column(String)
    Mathematics_exams = Column(String)
    Mathematics_total =  Column(String)
    M_Remarks = Column(String)
    M_Grade = Column(String)
    English_test = Column(String)
    English_exams = Column(String)
    English_total =  Column(String)
    E_Remarks = Column(String)
    E_Grade = Column(String)
    physics_test = Column(String)
    physics_exams =Column(String)
    physics_total =  Column(String)
    P_Remarks = Column(String)
    P_Grade = Column(String)
    biology_test = Column(String)
    biology_exams = Column(String)
    biology_total =  Column(String)
    B_Remarks = Column(String)
    B_Grade = Column(String)
    geography_test = Column(String)
    geography_exams = Column(String)
    geography_total =  Column(String)
    G_Remarks = Column(String)
    G_Grade = Column(String)
    chemistry_text = Column(String)
    chemistry_exams = Column(String)
    chemistry_total =  Column(String)
    C_Remarks = Column(String)
    C_Grade = Column(String)
    furthermaths_test = Column(String)
    furthermaths_exams = Column(String)
    furthermaths_total =  Column(String)
    F_Remarks = Column(String)
    F_Grade = Column(String)
    yoruba_test = Column(String)
    yoruba_exams = Column(String)
    youruba_total =  Column(String)
    Y_Remarks = Column(String)
    Y_Grade = Column(String)
    civic_test = Column(String)
    civic_exams = Column(String)
    civic_total =  Column(String)
    CI_Remarks = Column(String)
    CI_Grade = Column(String)
    dp_test = Column(String)
    dp_exams = Column(String)
    dp_total = Column(String)
    D_Remarks = Column(String)
    D_Grade = Column(String)
    term = Column(String)
    Class = Column(String)
    average = Column(String)
    position = Column(String)
    overall_position  = Column(String)
    resumption = Column(String)