from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from .database import Base

class Patient(Base):
    __tablename__ = "Patients"
    patient_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    appointments = relationship("Appointment", back_populates="patient")

class Appointment(Base):
    __tablename__ = "Appointments"
    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("Patients.patient_id"))
    doctor_id = Column(Integer)
    appointment_date = Column(DateTime, nullable=False)
    reason = Column(Text)
    status = Column(String(50), default="Scheduled")
    patient = relationship("Patient", back_populates="appointments")
