from sqlalchemy.orm import Session
from typing import List, Optional
from app.src.paths.repository import PathRepository
from app.src.paths.schemas import PathCreate, Path
from app.src.paths.models import PathModel


class PathService:
    def __init__(self, db: Session):
        self.repository = PathRepository(db)

    def create_path(self, path_data: PathCreate) -> Path:
        db_path = self.repository.create_path(path_data)
        return Path.from_orm(db_path)

    def get_path(self, path_id: int) -> Optional[Path]:
        db_path = self.repository.get_path(path_id)
        return Path.from_orm(db_path) if db_path else None

    def get_all_paths(self) -> List[Path]:
        db_paths = self.repository.get_all_paths()
        return [Path.from_orm(path) for path in db_paths]

    def get_paths_from_org(self, organization_id: int) -> List[PathModel]:
        db_paths = self.repository.get_paths_from_org(organization_id)
        return db_paths

    def get_paths_from_wsa(self, wsa_id: int) -> List[PathModel]:
        db_paths = self.repository.get_paths_from_wsa(wsa_id)
        return db_paths

    def get_path_from_wsas(self, start: int, end: int) -> PathModel:
        db_path = self.repository.get_path_from_wsas(start, end)
        return db_path

    def truncate_data(self) -> None:
        self.repository.truncate_data()
