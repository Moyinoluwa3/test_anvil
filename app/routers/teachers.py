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
    prefix="/teachers",
    tags=['Teachers']
)
auth_handler = auth.Auth()

@router.get("/",response_model=List[schemas.UserOutput])
def get_all_teachers(db : Session = Depends(get_db) ):
    teachers = db.query(models.Teachers).all()
    return teachers


def get_current_teachers(token: str = Depends(oauth2_scheme),db : Session = Depends(get_db)) -> int:

    token_data = auth_handler.decode_token(token)
   
    teachers = db.query(models.Teachers).filter(models.Teachers.id == token_data).first()
    return teachers



@router.post("/", status_code=201, response_model=schemas.UserOutput )
def sign_up(user: schemas.UserCreate,db : Session = Depends(get_db)):
    email =  db.query(models.Teachers).filter(models.Teachers.email == user.email).first()
    email = jsonable_encoder(email)
    
    if  email:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail= "Teacher exists")
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        new_user= models.Teachers(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as err:
        return {"message" : err}


@router.post('/login', response_model=schemas.Token)

def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    
    old_teacher = db.query(models.Teachers).filter(models.Teachers.email == user_credentials.username).first()
    print (old_teacher)
    
    
    if not old_teacher:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")

    if not utils.verify(user_credentials.password, old_teacher.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
   
    access_token = auth_handler.encode_token(old_teacher.id)

    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/{id}',response_model=schemas.UserOutput)
def Get_user(id: int,db : Session = Depends(get_db) ):
    user = db.query(models.Teachers).filter(models.Teachers.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tecaher does not exist")

    return user
