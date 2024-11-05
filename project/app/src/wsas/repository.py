from sqlalchemy.orm import Session
from app.src.wsas.schemas import WSACreate
from app.src.wsas.models import WSA
from typing import List


class WSARepository:
    def __init__(self, db: Session):
        self.db = db

    def create_wsa(self, wsa: WSACreate) -> WSA:
        db_wsa = WSA(name=wsa.name)
        self.db.add(db_wsa)
        self.db.commit()
        self.db.refresh(db_wsa)
        return db_wsa

    def get_wsa(self, wsa_id: int) -> WSA:
        return self.db.query(WSA).filter(WSA.id == wsa_id).first()

    def get_by_name(self, name: str) -> WSA:
        return self.db.query(WSA).filter(WSA.name == name).first()

    def get_all_wsas(self) -> List[WSA]:
        return self.db.query(WSA).all()

    def truncate_data(self) -> None:
        self.db.query(WSA).delete()
        self.db.commit()
