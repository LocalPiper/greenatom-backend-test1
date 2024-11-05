from typing import List, Optional
from sqlalchemy.orm import Session
from app.src.schemas import WasteType
from app.src.storages.repository import StorageRepository
from app.src.storages.schemas import StorageCreate, Storage
from app.src.storages.models import StorageModel


class StorageService:
    def __init__(self, db: Session):
        self.repository = StorageRepository(db)

    def create_storage(self, storage_data: StorageCreate) -> Storage:
        possible_storage = self.repository.get_storage_by_org_id_and_waste_type(
            storage_data.organization_id, storage_data.waste_type
        )
        possible_storage2 = self.repository.get_storage_by_wsa_id_and_waste_type(
            storage_data.wsa_id, storage_data.waste_type
        )
        if (possible_storage is not None) or (possible_storage2 is not None):
            raise ValueError("Given Organization/WSA already has this type of storage!")
        db_storage = self.repository.create_storage(storage_data)
        return Storage.from_orm(db_storage)

    def get_storage(self, storage_id: int) -> Storage:
        return self.repository.get_storage(storage_id)

    def get_storages_by_wsa_id(self, id: int) -> List[StorageModel]:
        return self.repository.get_storages_by_wsa_id(id)

    def get_storages_by_org_id(self, id: int) -> List[StorageModel]:
        return self.repository.get_storages_by_org_id(id)

    def get_all_storages(self) -> List[Storage]:
        db_storage = self.repository.get_all_storages()
        return [Storage.from_orm(storage) for storage in db_storage]

    def get_storage_by_org_id_and_waste_type(
        self, id: int, waste_type: WasteType
    ) -> StorageModel:
        return self.repository.get_storage_by_org_id_and_waste_type(id, waste_type)

    def update_storage_size(self, storage_id: int, new_size: int) -> Optional[Storage]:
        if storage_id < 1:
            raise ValueError("incorrect id")
        if not self.repository.get_storage(storage_id):
            raise ValueError("no storage with given id")
        elif (self.repository.get_storage(storage_id).capacity < new_size) or (
            new_size < 0
        ):
            raise ValueError("invalid size value")
        else:
            db_storage = self.repository.update_storage_size(storage_id, new_size)
            return Storage.from_orm(db_storage) if db_storage else None

    def truncate_data(self) -> None:
        self.repository.truncate_data()
