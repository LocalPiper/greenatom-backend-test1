from sqlalchemy.orm import Session
from app.src.paths.schemas import PathCreate
from app.src.paths.models import Path

class PathRepository:
    def __init__(self, db: Session):
         self.db = db
        
    def create_path(self, path: PathCreate):
         db_path = Path(length=path.length, bidirectional=path.bidirectional, organization_id=path.organization_id, wsa_start_id=path.wsa_start_id, wsa_end_id=path.wsa_end_id)
         self.db.add(db_path)
         self.db.commit()
         self.db.refresh(db_path)
         return db_path

    def get_path(self, path_id: int):
         return self.db.query(Path).filter(Path.id == path_id).first()
    
    def get_all_paths(self):
         return self.db.query(Path).all()
    
