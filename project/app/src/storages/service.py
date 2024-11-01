from sqlalchemy.orm import Session
from repository import StorageRepository
from schemas import StorageCreate, Storage

class StorageService:
    def __init__(self, db: Session):
        self.repository = StorageRepository(db)

    def create_storage(self, storage_data: StorageCreate) -> Storage:
        return self.repository.create_storage(storage_data)

    def get_storage(self, storage_id: int) -> Storage:
        return self.repository.get_storage(storage_id)