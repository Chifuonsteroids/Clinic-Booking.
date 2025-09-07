from fastapi import FastAPI
from app.database import Base, engine
from app import models
from .routers import patients, appointments
from . import models, database

Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(patients.router)
app.include_router(appointments.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Clinic Booking System API"}
