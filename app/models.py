import re
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import TIMESTAMP, Column,Integer, String , Boolean,VARCHAR
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship







class Teachers(Base):
    __tablename__ = "Teachers"
    
    id = Column(Integer, primary_key= True , nullable=False)
    email = Column(String, nullable=False, unique=True)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Students(Base):
    __tablename__ = "Students"
    
    id = Column(Integer, primary_key= True , nullable=False)
    email = Column(String, nullable=False, unique=True)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
