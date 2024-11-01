from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import StorageCreate, Storage
from service import StorageService
from app.src.database import get_db

router = APIRouter()

@router.post("/storages/", response_model=Storage)
def create_storage(
    storage_data: StorageCreate,
    db: Session = Depends(get_db)
):
    service = StorageService(db)
    return service.create_storage(storage_data)
