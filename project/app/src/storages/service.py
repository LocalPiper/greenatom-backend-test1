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