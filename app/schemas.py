from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: date

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    date_of_birth: Optional[date]

class PatientResponse(PatientBase):
    patient_id: int
    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    reason: Optional[str]
    status: Optional[str] = "Scheduled"

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    patient_id: Optional[int]
    doctor_id: Optional[int]
    appointment_date: Optional[datetime]
    reason: Optional[str]
    status: Optional[str]

class AppointmentResponse(AppointmentBase):
    appointment_id: int
    class Config:
        from_attributes = True
