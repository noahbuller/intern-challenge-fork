#Main Python File (called on Uvicorn boot up)

from dotenv import load_dotenv
import os
from fastapi import FastAPI
from app.api import athletes
app = FastAPI()
load_dotenv(dotenv_path=".env")
@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(athletes.router, prefix="/api/v1")