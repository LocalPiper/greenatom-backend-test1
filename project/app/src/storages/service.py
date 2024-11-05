from typing import List, Optional
from sqlalchemy.orm import Session
from app.src.schemas import WasteType
from app.src.storages.repository import StorageRepository
from app.src.storages.schemas import StorageCreate, Storage


class StorageService:
    def __init__(self, db: Session):
        self.repository = StorageRepository(db)

    def create_storage(self, storage_data: StorageCreate) -> Storage:
        return self.repository.create_storage(storage_data)

    def get_storage(self, storage_id: int) -> Storage:
        return self.repository.get_storage(storage_id)

    def get_storages_by_wsa_id(self, id: int) -> List[Storage]:
        return self.repository.get_storages_by_wsa_id(id)

    def get_all_storages(self) -> List[Storage]:
        return self.repository.get_all_storages()

    def get_storage_by_org_id_and_waste_type(
        self, id: int, waste_type: WasteType
    ) -> Storage:
        storages: List[Storage] = self.get_all_storages()
        storage: Optional[Storage] = None
        for s in storages:
            if (s.organization_id == id) and (s.waste_type == waste_type):
                storage = s
                break
        return storage

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
            return self.repository.update_storage_size(storage_id, new_size)

    def truncate_data(self) -> None:
        self.repository.truncate_data()
