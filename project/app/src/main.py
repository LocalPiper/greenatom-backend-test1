# main.py
from fastapi import FastAPI
from app.src.organizations.router import router as organizations_router

app = FastAPI()

app.include_router(organizations_router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the main page!"}