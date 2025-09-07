import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Adjust credentials here
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_NAME = "clinic_booking.sql"
DB_PORT = 3306

 # Load environment variables from .env file
load_dotenv() 
DB_USER = os.getenv(DB_USER, "root")
DB_PASSWORD = os.getenv(DB_PASSWORD, "")
DB_HOST = os.getenv(DB_HOST, "localhost")
DB_NAME = os.getenv(DB_NAME, "clinic_booking.sql")
DB_PORT = os.getenv("DB_PORT", "3306")  

# First connect without database to ensure DB exists
tmp_engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}")

with tmp_engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
    conn.commit()

DB_PORT = os.getenv("DB_PORT", "3306")

# Build connection string depending on whether password exists
if DB_PASSWORD:
    BASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
else:
    BASE_URL = f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}"

# Now connect to the actual database
DATABASE_URL = f"{BASE_URL}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

