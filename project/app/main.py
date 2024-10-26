from fastapi import FastAPI
from .routers import organizations, storages
from .database import init_db

app = FastAPI()

app.include_router(organizations.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the main page!"}

@app.on_event("startup")
async def startup():
    init_db()