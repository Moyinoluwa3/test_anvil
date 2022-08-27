from fastapi import HTTPException, status, Depends,APIRouter,Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import admin
from .. import models,schemas,database
from typing import List

router = APIRouter(tags=["Classes"]) 

@router.post('/classes',status_code=201)
def create_class(classes: schemas.ClassIn, db : Session = Depends(database.get_db)):
    old_classes = db.query(models.Classes).filter(models.Classes.name == classes.name).first()
    if old_classes:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail= "Class exists")
    new_class = models.Classes(**classes.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

@router.post('/subjects')
def create_subject(subject: schemas.SubjectIn,db : Session = Depends(database.get_db)):
    old_subjects = db.query(models.Subjects).filter(models.Subjects.subject == subject.subject).first()

    if old_subjects:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Wrong Entry")

    new_subject = models.Subjects(**subject.dict())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject


@router.get('/subjects/all',response_model=List[schemas.SubjectOut])
def get_all_subjects(db : Session = Depends(database.get_db)):
    subjects =  db.query(models.Subjects).all()
    return subjects

@router.get('/{Class}',response_model=List[schemas.StudentOut])
def Get_Student(Class: str,db : Session = Depends(database.get_db)):
    student = db.query(models.Students).filter(models.Students.Class == Class).all()

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students does not exist")

    return student
                        