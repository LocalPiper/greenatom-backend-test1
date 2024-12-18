from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.src.paths.schemas import PathCreate, Path
from app.src.paths.service import PathService
from app.src.database import get_db

router = APIRouter()


@router.post("/paths/", response_model=Path)
def create_path(path_data: PathCreate, db: Session = Depends(get_db)) -> Path:
    """Creates a Path object in a database

    Args:
        path_data (PathCreate): data for Path creation,
        db (Session, optional): database. Defaults to Depends(get_db).

    Raises:
        HTTPException: raised if validation error occurs

    Returns:
        Path: created Path object
    """
    try:
        service = PathService(db)
        return service.create_path(path_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.get("/paths/", response_model=List[Path])
def get_all_paths(db: Session = Depends(get_db)) -> List[Path]:
    """Gets all Paths from database

    Args:
        db (Session, optional): database. Defaults to Depends(get_db).

    Returns:
        List[Path]: list of Paths
    """
    service = PathService(db)
    return service.get_all_paths()
