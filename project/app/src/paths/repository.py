from typing import List, Optional
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.src.paths.models import PathModel
from app.src.paths.schemas import PathCreate


class PathRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_path(self, path: PathCreate) -> PathModel:
        db_path = PathModel(
            length=path.length,
            bidirectional=path.bidirectional,
            organization_id=path.organization_id,
            wsa_start_id=path.wsa_start_id,
            wsa_end_id=path.wsa_end_id,
        )
        self.db.add(db_path)
        self.db.commit()
        self.db.refresh(db_path)
        return db_path

    def get_path(self, path_id: int) -> Optional[PathModel]:
        return self.db.query(PathModel).filter(PathModel.id == path_id).first()

    def get_all_paths(self) -> List[PathModel]:
        return self.db.query(PathModel).all()

    def get_paths_from_org(self, organization_id: int) -> list[PathModel]:
        return (
            self.db.query(PathModel)
            .filter(PathModel.organization_id == organization_id)
            .all()
        )

    def get_paths_from_wsa(self, wsa_id: int) -> list[PathModel]:
        return (
            self.db.query(PathModel)
            .filter(
                and_(
                    PathModel.wsa_start_id == wsa_id, PathModel.organization_id == None
                )
            )
            .all()
        )

    def get_path_from_wsas(self, start: int, end: int) -> Optional[PathModel]:
        return (
            self.db.query(PathModel)
            .filter(PathModel.wsa_start_id == start, PathModel.wsa_end_id == end)
            .first()
        )

    def truncate_data(self) -> None:
        self.db.query(PathModel).delete()
        self.db.commit()
