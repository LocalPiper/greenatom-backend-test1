from sqlalchemy.orm import Session
from app.src.wsas.schemas import WSACreate
from app.src.wsas.models import WSAModel
from typing import List


class WSARepository:
    def __init__(self, db: Session):
        self.db = db

    def create_wsa(self, wsa: WSACreate) -> WSAModel:
        db_wsa = WSAModel(name=wsa.name)
        self.db.add(db_wsa)
        self.db.commit()
        self.db.refresh(db_wsa)
        return db_wsa

    def get_wsa(self, wsa_id: int) -> WSAModel:
        return self.db.query(WSAModel).filter(WSAModel.id == wsa_id).first()

    def get_by_name(self, name: str) -> WSAModel:
        return self.db.query(WSAModel).filter(WSAModel.name == name).first()

    def get_all_wsas(self) -> List[WSAModel]:
        return self.db.query(WSAModel).all()

    def truncate_data(self) -> None:
        self.db.query(WSAModel).delete()
        self.db.commit()
