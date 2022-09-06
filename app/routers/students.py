from fastapi import HTTPException, status, Depends,APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from typing import List
from .. import auth
from .. import models, schemas, utils
from ..database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
router = APIRouter(
    prefix="/students",
    tags=['Students']
)
auth_handler = auth.Auth()

@router.get("/",response_model=List[schemas.StudentOut])
def get_all_students(db : Session = Depends(get_db) ):
    students = db.query(models.Students).all()
    return students


def get_current_students(token: str = Depends(oauth2_scheme),db : Session = Depends(get_db)) -> int:

    token_data = auth_handler.decode_token(token)
   
    students = db.query(models.Students).filter(models.User.id == token_data).first()
    return students



@router.post("/signup", status_code=201, response_model=schemas.StudentOut )
def sign_up(user: schemas.Student_In,db : Session = Depends(get_db)):
    email =  db.query(models.Students).filter(models.Students.email == user.email).first()
    email = jsonable_encoder(email)
    
    if  email:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail= "Student exists")
    obj = db.query(models.Students).order_by(models.Students.admission_no.desc())
    last_admission_no= obj.first()
    if last_admission_no :
        admission_no = last_admission_no.admission_no + 1
    else:
        admission_no = 1000
    # result = db.query(models.Results).filter(models.Results.email == user.email).first()
    # result.admission_no = admission_no
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_student= models.Students(admission_no=admission_no,**user.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.post('/login', response_model=schemas.Token)

def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    
    old_student = db.query(models.Students).filter(models.Students.email == user_credentials.username).first()
    print (old_student)
    
    
    if not old_student:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")

    if not utils.verify(user_credentials.password, old_student.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
   
    access_token = auth_handler.encode_token(old_student.id)

    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/{id}',response_model=schemas.StudentOut)
def Get_user(id: int,db : Session = Depends(get_db) ):
    user = db.query(models.Students).filter(models.Students.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students does not exist")

    return user
@router.get("/email")
def Get_user(email: str,db : Session = Depends(get_db) ):
    user = db.query(models.Students).filter(models.Students.email == email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students does not exist")

    else:
        user_id = user.id
        print(user_id)


@router.post('/Class',response_model=List[schemas.StudentOut])
def Get_Student(Class: str,db : Session = Depends(get_db)):
    student = db.query(models.Students).filter(models.Students.Class == Class).all()

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students does not exist")

    return student
                        
