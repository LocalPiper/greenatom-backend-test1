from sqlalchemy.orm import Session
from app.src.storages.schemas import StorageCreate
from app.src.storages.models import Storage

class StorageRepository:
    def __init__(self, db: Session):
         self.db = db
        
    def create_storage(self, storage: StorageCreate):
         db_storage = Storage(waste_type=storage.waste_type, size=storage.size, capacity=storage.capacity, organization_id=storage.organization_id, wsa_id=storage.wsa_id)
         self.db.add(db_storage)
         self.db.commit()
         self.db.refresh(db_storage)
         return db_storage

    def get_storage(self, storage_id: int):
         return self.db.query(Storage).filter(Storage.id == storage_id).first()
    
    def get_all_storages(self):
         return self.db.query(Storage).all()
    
    def update_storage_size(self, storage_id: int, new_size: id):
         db_storage = self.get_storage(storage_id)
         if db_storage:
              db_storage.size = new_size
              self.db.commit()
              self.db.refresh(db_storage)
         return db_storage
    
    def truncate_data(self):
         self.db.query(Storage).delete()
         self.db.commit()
