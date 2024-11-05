from typing import List, Set
from sqlalchemy.orm import Session
from app.src.wsas.repository import WSARepository
from app.src.wsas.schemas import WSACreate, WSA
from app.src.paths.models import PathModel


class WSAService:
    def __init__(self, db: Session):
        self.repository = WSARepository(db)

    def create_wsa(self, wsa_data: WSACreate) -> WSA:
        return self.repository.create_wsa(wsa_data)

    def get_wsa(self, wsa_id: int) -> WSA:
        return self.repository.get_wsa(wsa_id)

    def get_by_name(self, wsa_name: str) -> WSA:
        return self.repository.get_by_name(wsa_name)

    def get_all_wsas(self) -> List[WSA]:
        return self.repository.get_all_wsas()

    def get_wsas_from_paths(self, paths: List[PathModel]):
        wsas: List[WSA] = []
        wsas_id_set: Set[int] = set()
        for p in paths:
            wsa = self.get_wsa(p.wsa_start_id)
            if wsa:
                wsas.append(wsa)
                wsas_id_set.add(wsa.id)
        return wsas, wsas_id_set

    def truncate_data(self) -> None:
        self.repository.truncate_data()
