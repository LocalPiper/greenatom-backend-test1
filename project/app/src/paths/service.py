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