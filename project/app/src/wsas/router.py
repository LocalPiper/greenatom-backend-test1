from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import WSACreate, WSA
from service import WSAService
from app.src.database import get_db

router = APIRouter()

@router.post("/wsas/", response_model=WSA)
def create_wsa(
    wsa_data: WSACreate,
    db: Session = Depends(get_db)
):
    service = WSAService(db)
    return service.create_wsa(wsa_data)
