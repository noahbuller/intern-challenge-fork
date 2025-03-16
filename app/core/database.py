from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

#Load in enviornemnt variables (defaults to the .env file extension)
load_dotenv()

#Grab all enviornment variables(makes the DataBase_URL easier to read)
DataBase = os.getenv('DATABASE')
User = os.getenv('USER')
Password = os.getenv('PASSWORD')
Host = os.getenv('HOST')
Port = os.getenv('PORT')

#Create DatabaseURL link
DataBase_URL = f'postgresql://{User}:{Password}@{Host}:{Port}/{DataBase}'

#Establish Database connection as engine instance
engine = create_engine(DataBase_URL)

Base = declarative_base()