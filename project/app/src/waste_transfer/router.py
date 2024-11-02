from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.database import get_db
from app.src.storages.schemas import Storage
from app.src.waste_transfer.schemas import WasteTransferRequest
from app.src.waste_transfer.service import WasteTransferService
from app.src.waste_transfer.schemas import GraphModel

router = APIRouter()

@router.post("/transfer_waste", response_model=GraphModel)
def transfer_waste(
    transfer_data: WasteTransferRequest,
    db: Session = Depends(get_db)
):
    service = WasteTransferService(db)
    return service.transfer_waste(transfer_data)