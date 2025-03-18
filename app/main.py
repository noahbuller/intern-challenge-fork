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

#Prefix all routes with api/v1 to indivate "version 1" of the API -- this can eventually be removed or modified after development
app.include_router(athletes.router, prefix="/api/v1")