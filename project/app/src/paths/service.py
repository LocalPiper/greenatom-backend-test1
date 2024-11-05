from sqlalchemy.orm import Session
from typing import List, Optional
from app.src.paths.repository import PathRepository
from app.src.paths.schemas import PathCreate, Path
from app.src.paths.models import PathModel


class PathService:
    def __init__(self, db: Session):
        self.repository = PathRepository(db)

    def create_path(self, path_data: PathCreate) -> Path:
        possible_path = self.repository.get_path_from_org_and_wsa(
            path_data.organization_id, path_data.wsa_start_id
        )
        possible_path2 = self.repository.get_path_from_wsas(
            path_data.wsa_start_id, path_data.wsa_end_id
        )
        possible_path3 = self.repository.get_path_from_wsas(
            path_data.wsa_end_id, path_data.wsa_start_id
        )
        possible_path4 = self.repository.get_path_from_org_and_wsa(
            path_data.wsa_start_id, path_data.organization_id
        )
        if (
            (possible_path is not None)
            or (possible_path2 is not None)
            or (possible_path3 is not None)
            or (possible_path4 is not None)
        ):
            raise ValueError("Path that uses these points already exists!")
        db_path = self.repository.create_path(path_data)
        return Path.from_orm(db_path)

    def get_path(self, path_id: int) -> Optional[PathModel]:
        db_path = self.repository.get_path(path_id)
        return Path.from_orm(db_path) if db_path else None

    def get_all_paths(self) -> List[Path]:
        db_paths = self.repository.get_all_paths()
        return [Path.from_orm(path) for path in db_paths]

    def get_paths_from_org(self, organization_id: int) -> List[PathModel]:
        return self.repository.get_paths_from_org(organization_id)

    def get_paths_from_wsa(self, wsa_id: int) -> List[PathModel]:
        return self.repository.get_paths_from_wsa(wsa_id)

    def get_path_from_wsas(self, start: int, end: int) -> PathModel:
        return self.repository.get_path_from_wsas(start, end)

    def truncate_data(self) -> None:
        self.repository.truncate_data()
