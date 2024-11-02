from typing import List
from sqlalchemy.orm import Session
from app.src.paths.repository import PathRepository
from app.src.paths.schemas import PathCreate, Path

class PathService:
    def __init__(self, db: Session):
        self.repository = PathRepository(db)

    def create_path(self, path_data: PathCreate) -> Path:
        return self.repository.create_path(path_data)

    def get_path(self, path_id: int) -> Path:
        return self.repository.get_path(path_id)
    
    def get_all_paths(self) -> List[Path]:
        return self.repository.get_all_paths()
    
    def get_paths_from_org(self, organization_id: int) -> List[Path]:
        return self.repository.get_paths_from_org(organization_id)
    
    def get_paths_from_wsa(self, wsa_id: int) -> List[Path]:
        return self.repository.get_paths_from_wsa(wsa_id)

    def truncate_data(self) -> None:
        self.repository.truncate_data()