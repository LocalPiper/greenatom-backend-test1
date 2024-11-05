from email import message
from typing import List
from exceptiongroup import catch
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.database import get_db
from app.src.storages.schemas import Storage
from app.src.waste_logic.schemas import (
    WasteTransferRequest,
    WasteGenerationRequest,
    WasteRecycleRequest,
)
from app.src.waste_logic.service import WasteTransferService, WasteProcessingService

router = APIRouter()


@router.post("/transfer_waste", response_model=List[Storage])
def transfer_waste(transfer_data: WasteTransferRequest, db: Session = Depends(get_db)):
    try:
        service = WasteTransferService(db)
        return service.transfer_waste(transfer_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.post("/generate_waste", response_model=List[Storage])
def generate_waste(
    generation_data: WasteGenerationRequest, db: Session = Depends(get_db)
):
    try:
        service = WasteProcessingService(db)
        return service.generate_waste(generation_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.post("/recycle_waste", response_model=List[Storage])
def recycle_waste(recycle_data: WasteRecycleRequest, db: Session = Depends(get_db)):
    try:
        service = WasteProcessingService(db)
        return service.recycle_waste(recycle_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
