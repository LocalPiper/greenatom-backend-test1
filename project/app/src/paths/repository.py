from sqlalchemy.orm import Session
import schemas, models

class PathRepository:
    def __init__(self, db: Session):
         self.db = db
        
    def create_path(self, path: schemas.PathCreate):
         db_path = models.Path(length=path.length, bidirectional=path.bidirectional, organization_id=path.organization_id, wsa_start_id=path.wsa_start_id, wsa_end_id=path.wsa_end_id)
         self.db.add(db_path)
         self.db.commit()
         self.db.refresh(db_path)
         return db_path

    def get_path(self, path_id: int):
         return self.db.query(models.Path).filter(models.Path.id == path_id).first()
    
