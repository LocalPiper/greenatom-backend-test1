from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.src.wsas.schemas import WSACreate, WSA
from app.src.wsas.service import WSAService
from app.src.database import get_db

router = APIRouter()


@router.post("/wsas/", response_model=WSA)
def create_wsa(wsa_data: WSACreate, db: Session = Depends(get_db)) -> WSA:
    service = WSAService(db)
    return service.create_wsa(wsa_data)


@router.get("/wsas/", response_model=List[WSA])
def get_all_wsas(db: Session = Depends(get_db)) -> List[WSA]:
    service = WSAService(db)
    return service.get_all_wsas()
