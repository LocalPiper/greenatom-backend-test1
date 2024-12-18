# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.src.database import get_db, init_db
from app.src.organizations.router import router as organizations_router
from app.src.script import create_sample_data
from app.src.wsas.router import router as wsas_router
from app.src.storages.router import router as storages_router
from app.src.paths.router import router as paths_router
from app.src.waste_logic.router import router as waste_logic_router

app = FastAPI()

app.include_router(organizations_router, prefix="/api/internal")
app.include_router(wsas_router, prefix="/api/internal")
app.include_router(storages_router, prefix="/api/internal")
app.include_router(paths_router, prefix="/api/internal")
app.include_router(waste_logic_router, prefix="/api")


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to the main page!"}


@app.post("/script")
def generate_sample_data(db: Session = Depends(get_db)) -> None:
    """Generates the layout provided on the image.
    Should only be used once

    Args:
        db (Session, optional): database. Defaults to Depends(get_db).
    """
    create_sample_data(db)


@app.on_event("startup")
def startup_event(db: Session = next(get_db())) -> None:
    init_db()
