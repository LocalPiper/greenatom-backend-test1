from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.storages.schemas import StorageCreate, Storage
from app.src.storages.service import StorageService
from app.src.database import get_db

router = APIRouter()


@router.post("/storages/", response_model=Storage)
def create_storage(storage_data: StorageCreate, db: Session = Depends(get_db)):
    service = StorageService(db)
    return service.create_storage(storage_data)


@router.get("/storages/", response_model=List[Storage])
def get_all_storages(db: Session = Depends(get_db)):
    service = StorageService(db)
    return service.get_all_storages()


@router.patch("/storages/{storage.id}/size", response_model=Storage)
def update_storage_size(storage_id: int, new_size: int, db: Session = Depends(get_db)):
    service = StorageService(db)
    updated_storage = service.update_storage_size(storage_id, new_size)
    if updated_storage is None:
        raise HTTPException(status_code=404, detail="Storage not found")
    return updated_storage
