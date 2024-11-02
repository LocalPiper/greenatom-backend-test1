from sqlalchemy.orm import Session
from app.src.wsas.repository import WSARepository
from app.src.wsas.schemas import WSACreate, WSA

class WSAService:
    def __init__(self, db: Session):
        self.repository = WSARepository(db)

    def create_wsa(self, wsa_data: WSACreate) -> WSA:
        return self.repository.create_wsa(wsa_data)

    def get_wsa(self, wsa_id: int) -> WSA:
        return self.repository.get_wsa(wsa_id)