from fastapi import HTTPException, status, Depends,APIRouter,Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import admin
from .. import models,schemas,database
from typing import List
from sqlalchemy.sql import text 
from sqlalchemy import or_

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

@router.post('/results')
def create_result(result: schemas.ResultIn,db : Session = Depends(database.get_db)):
    former_name = db.query(models.Results).filter(models.Results.admission_no == result.admission_no).first()
    if former_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You cant a create result for a student twice")
    average = (result.biology_total+result.chemistry_total+result.civic_total+result.dp_total+result.English_total+result.furthermaths_total+result.geography_total
    +result.Mathematics_total+result.physics_total+result.youruba_total)/10
   
    new_result = models.Results(average=average**result.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return {"message": "Sucessfully updated"}

# @router.post('/result')
# def create_result()

@router.get("/results/{admission_no}", response_model=schemas.ResultIn)
def get_result(db : Session = Depends(database.get_db)):
    result = db.query(models.Results).filter(models.Results.admission_no == result.admission_no).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not available")
    return result

@router.post("/findsubjects", response_model=List[schemas.StudentOut])
def get_a_student(Class: str , subject: str , db : Session = Depends(database.get_db)):
    
    student = db.query(models.Students).filter(models.Students.Class == Class,or_(models.Students.subject_1.like(subject),models.Students.subject_2.like(subject),
    models.Students.subject_3.like(subject),models.Students.subject_4.like(subject),models.Students.subject_5.like(subject),models.Students.subject_6.like(subject),
    models.Students.subject_7.like(subject),models.Students.subject_8.like(subject),models.Students.subject_9.like(subject),models.Students.subject_10.like(subject))).all()
    if not student:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not available")
    return student
    

                        