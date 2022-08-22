from fastapi import HTTPException, status, Depends,APIRouter,Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from typing import List

from .. import auth
from .. import models, schemas, utils
from ..database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='admin/login')
router = APIRouter(tags=['Admins'])

auth_handler = auth.Auth()

def get_current_admin(token: str = Depends(oauth2_scheme),db : Session = Depends(get_db)):

    token_data = auth_handler.decode_token(token)
   
    admin = db.query(models.Admin).filter(models.Admin.id ==token_data).first()
    return admin

@router.post("/admin", response_model=schemas.AdminOut)
def create_admin(admin:schemas.Admin,db: Session = Depends(get_db)):
    old_admin = db.query(models.Admin).filter(models.Admin.name == admin.name).first()
    old_admin = jsonable_encoder(old_admin)
    if old_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail= "Admin exists")
    try:
        hashed_password = utils.hash(admin.password)
        admin.password = hashed_password
        new_admin= models.Admin(**admin.dict())
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
    except Exception as err:
        return {"message" : err}

@router.get('/admin/all',response_model=List[schemas.AdminOut])
def get_admin(db: Session = Depends(get_db)):
    admins = db.query(models.Admin).all()
    return admins

@router.post('/admin/login', response_model=schemas.Token)
def login(admin_credentials: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    
    admin = db.query(models.Admin).filter(models.Admin.name == admin_credentials.username).first()
    print (admin)
    
    
    if not admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")

    if not utils.verify(admin_credentials.password, admin.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")
   
    access_token = auth_handler.encode_token(admin.id)

    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/admin/{id}' ,response_model=schemas.AdminOut)
def get_an_admin(id:int,db : Session = Depends(get_db)):
    admin = db.query(models.Admin).filter(models.Admin.id == id).first()

    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="admin does not exist")

    return admin
