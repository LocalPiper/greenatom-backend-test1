from sqlalchemy.orm import Session
import schemas, models

class WSARepository:
    def __init__(self, db: Session):
         self.db = db
        
    def create_wsa(self, wsa: schemas.WSACreate):
         db_wsa = models.WSA(name = wsa.name)
         self.db.add(db_wsa)
         self.db.commit()
         self.db.refresh(db_wsa)
         return db_wsa

    def get_wsa(self, wsa_id: int):
         return self.db.query(models.WSA).filter(models.WSA.id == wsa_id).first()
    
