from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

#Load in enviornemnt variables (defaults to the .env file extension)
load_dotenv()

#Grab all enviornment variables(makes the DataBase_URL easier to read)
DataBase = os.getenv('DATABASE')
User = os.getenv('DB_USER')
Password = os.getenv('DB_PASSWORD')
Host = os.getenv('DB_HOST')
Port = os.getenv('DB_PORT')

#Create DatabaseURL link
DataBase_URL = f'postgresql://{User}:{Password}@{Host}:{Port}/{DataBase}'

print("DATABASE_URL:", DataBase_URL)  # Debugging print statement


#Establish Database connection as engine instance
engine = create_engine(DataBase_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()