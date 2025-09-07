# Clinic Booking System API (FastAPI)

This project is a **CRUD API** built with **FastAPI** and **SQLAlchemy** to manage patients and appointments for a clinic.  

It connects to the **MySQL database** designed in Question 1 (`clinic_booking.sql`).

## 📌 Features
- **Patients CRUD** (Create, Read, Update, Delete)  
- **Appointments CRUD** (Create, Read, Update, Delete)  
- Built with **FastAPI** + **SQLAlchemy ORM**  
- Interactive API docs available via **Swagger UI**  

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/clinic-booking-api.git
cd clinic-booking-api
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
pip install fastapi uvicorn sqlalchemy pymysql
```

## 🗄️ Database Setup
```bash
mysql -u root -p < clinic_booking.sql
```
Update DB URL in `database.py` if needed.

## 🚀 Run the API
```bash
uvicorn app.main:app --reload
```
- Root: http://127.0.0.1:3306  
- Docs: http://127.0.0.1:8000/docs  

## 📖 Endpoints
Patients: `/patients/`  
Appointments: `/appointments/`  
