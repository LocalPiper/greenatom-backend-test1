from typing import List
from sqlalchemy.orm import Session
from app.src.storages.repository import StorageRepository
from app.src.storages.schemas import StorageCreate, Storage

class StorageService:
    def __init__(self, db: Session):
        self.repository = StorageRepository(db)

    def create_storage(self, storage_data: StorageCreate) -> Storage:
        return self.repository.create_storage(storage_data)

    def get_storage(self, storage_id: int) -> Storage:
        return self.repository.get_storage(storage_id)
    
    def get_all_storages(self) -> List[Storage]:
        return self.repository.get_all_storages()
    
    def update_storage_size(self, storage_id: int, new_size: int) -> Storage:
        if not self.repository.get_storage(storage_id):
            print("no storage with given id")
        elif (self.repository.get_storage(storage_id).capacity < new_size) or (new_size < 0):
            print("invalid size value")
        else:
            return self.repository.update_storage_size(storage_id, new_size)