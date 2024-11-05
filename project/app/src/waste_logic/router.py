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
def transfer_waste(
    transfer_data: WasteTransferRequest, db: Session = Depends(get_db)
) -> List[Storage]:
    """Transfers waste from given Organization to nearest WSAs in given amount.
    If all available WSAs are full, will not transfer waste

    Args:
        transfer_data (WasteTransferRequest): data for waste transfer. Consists of Organization name, waste type and amount to transfer,
        db (Session, optional): database. Defaults to Depends(get_db).

    Raises:
        HTTPException: raised if Organization/Storage/WSA is not found in the process

    Returns:
        List[Storage]: updated list of Storages
    """
    try:
        service = WasteTransferService(db)
        return service.transfer_waste(transfer_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.post("/generate_waste", response_model=List[Storage])
def generate_waste(
    generation_data: WasteGenerationRequest, db: Session = Depends(get_db)
) -> List[Storage]:
    """Fills Storage of given Organization to capacity level.
    If waste type is provided, fills Storage of given type. Otherwise, fills all Storages of given Organization

    Args:
        generation_data (WasteGenerationRequest): data for waste generation. Consists of Organization name and waste type (optional),
        db (Session, optional): database. Defaults to Depends(get_db).

    Raises:
        HTTPException: raised if Organization/Storage was not found

    Returns:
        List[Storage]: list of updated Storages
    """
    try:
        service = WasteProcessingService(db)
        return service.generate_waste(generation_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.post("/recycle_waste", response_model=List[Storage])
def recycle_waste(
    recycle_data: WasteRecycleRequest, db: Session = Depends(get_db)
) -> List[Storage]:
    """Empties Storages of given WSA.
    If waste type is provided, empties Storage of given type. Otherwise, empties all Storages of given WSA

    Args:
        recycle_data (WasteRecycleRequest): data for waste recycling. Consists of WSA name and waste type (optional),
        db (Session, optional): database. Defaults to Depends(get_db).

    Raises:
        HTTPException: raised if WSA/Storage was not found

    Returns:
        List[Storage]: list of updated Storages
    """
    try:
        service = WasteProcessingService(db)
        return service.recycle_waste(recycle_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
