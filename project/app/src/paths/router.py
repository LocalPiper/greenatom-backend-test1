from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import PathCreate, Path
from service import PathService
from app.src.database import get_db

router = APIRouter()

@router.post("/paths/", response_model=Path)
def create_path(
    path_data: PathCreate,
    db: Session = Depends(get_db)
):
    service = PathService(db)
    return service.create_path(path_data)
