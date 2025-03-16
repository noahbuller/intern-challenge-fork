#Main Python File (called on Uvicorn boot up)

from fastapi import FastAPI
from app.api import athletes

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(athletes.router, prefix="/api/v1")