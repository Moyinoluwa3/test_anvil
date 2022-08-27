from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import students,teachers,admin,classes


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)
app.include_router(students.router)
app.include_router(teachers.router)
app.include_router(admin.router)
app.include_router(classes.router)

@app.get("/")
def root():
    return {"message": " I am Alive:("}