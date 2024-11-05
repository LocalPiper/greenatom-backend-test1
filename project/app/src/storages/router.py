from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.storages.schemas import StorageCreate, Storage
from app.src.storages.service import StorageService
from app.src.database import get_db

router = APIRouter()


@router.post("/storages/", response_model=Storage)
def create_storage(
    storage_data: StorageCreate, db: Session = Depends(get_db)
) -> Storage:
    """Creates a Storage object in a database

    Args:
        storage_data (StorageCreate): data for Storage creation,
        db (Session, optional): database. Defaults to Depends(get_db).

    Raises:
        HTTPException: raised if validation error occurs

    Returns:
        Storage: created Storage object
    """
    try:
        service = StorageService(db)
        return service.create_storage(storage_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.get("/storages/", response_model=List[Storage])
def get_all_storages(db: Session = Depends(get_db)) -> List[Storage]:
    """Gets all Storages from database
    Args:
        db (Session, optional): database. Defaults to Depends(get_db).

    Returns:
        List[Storage]: list of Storages
    """
    service = StorageService(db)
    return service.get_all_storages()


@router.patch("/storages/{storage.id}/size", response_model=Storage)
def update_storage_size(
    storage_id: int, new_size: int, db: Session = Depends(get_db)
) -> Storage:
    """Updates the Size of given Storage

    Args:
        storage_id (int): id of Storage,
        new_size (int): new size of Storage - must be lower than it's Capacity,
        db (Session, optional): database. Defaults to Depends(get_db).

    Raises:
        HTTPException: raised if validation error occurrs

    Returns:
        Storage: updated Storage
    """
    try:
        service = StorageService(db)
        updated_storage = service.update_storage_size(storage_id, new_size)
        return updated_storage
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
