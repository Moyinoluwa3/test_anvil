
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
    Mathematics_test = Column(Integer)
    Mathematics_exams = Column(Integer)
    Mathematics_total =  Column(Integer)
    M_Remarks = Column(String)
    M_Grade = Column(String)
    English_test = Column(Integer)
    English_exams = Column(Integer)
    English_total =  Column(Integer)
    E_Remarks = Column(String)
    E_Grade = Column(String)
    physics_test = Column(Integer)
    physics_exams =Column(Integer)
    physics_total =  Column(Integer)
    P_Remarks = Column(String)
    P_Grade = Column(String)
    biology_test = Column(Integer)
    biology_exams = Column(Integer)
    biology_total =  Column(Integer)
    B_Remarks = Column(String)
    B_Grade = Column(String)
    geography_test = Column(Integer)
    geography_exams = Column(Integer)
    geography_total =  Column(Integer)
    G_Remarks = Column(String)
    G_Grade = Column(String)
    chemistry_text = Column(Integer)
    chemistry_exams = Column(Integer)
    chemistry_total =  Column(Integer)
    C_Remarks = Column(String)
    C_Grade = Column(String)
    furthermaths_test = Column(Integer)
    furthermaths_exams = Column(Integer)
    furthermaths_total =  Column(Integer)
    F_Remarks = Column(String)
    F_Grade = Column(String)
    yoruba_test = Column(Integer)
    yoruba_exams = Column(Integer)
    youruba_total =  Column(Integer)
    Y_Remarks = Column(String)
    Y_Grade = Column(String)
    civic_test = Column(Integer)
    civic_exams = Column(Integer)
    civic_total =  Column(Integer)
    CI_Remarks = Column(String)
    CI_Grade = Column(String)
    dp_test = Column(Integer)
    dp_exams = Column(Integer)
    dp_total = Column(Integer)
    D_Remarks = Column(String)
    D_Grade = Column(String)
    term = Column(String)
    Class = Column(String)
    average = Column(Integer)
    position = Column(String)
    overall_position  = Column(String)
    resumption = Column(String)