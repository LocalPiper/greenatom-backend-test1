from typing import Optional, List
from sqlalchemy.orm import Session
from app.src.storages.schemas import StorageCreate
from app.src.storages.models import StorageModel
from app.src.schemas import WasteType


class StorageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_storage(self, storage: StorageCreate) -> StorageModel:
        db_storage = StorageModel(
            waste_type=storage.waste_type,
            size=storage.size,
            capacity=storage.capacity,
            organization_id=storage.organization_id,
            wsa_id=storage.wsa_id,
        )
        self.db.add(db_storage)
        self.db.commit()
        self.db.refresh(db_storage)
        return db_storage

    def get_storage(self, storage_id: int) -> Optional[StorageModel]:
        return self.db.query(StorageModel).filter(StorageModel.id == storage_id).first()

    def get_storages_by_wsa_id(self, id: int) -> List[StorageModel]:
        return self.db.query(StorageModel).filter(StorageModel.wsa_id == id).all()

    def get_storages_by_org_id(self, id: int) -> List[StorageModel]:
        return (
            self.db.query(StorageModel).filter(StorageModel.organization_id == id).all()
        )

    def get_all_storages(self) -> List[StorageModel]:
        return self.db.query(StorageModel).all()

    def get_storage_by_org_id_and_waste_type(self, id: int, waste_type: WasteType):
        return (
            self.db.query(StorageModel)
            .filter(StorageModel.waste_type == waste_type)
            .filter(StorageModel.organization_id == id)
            .first()
        )

    def get_storage_by_wsa_id_and_waste_type(self, id: int, waste_type: WasteType):
        return (
            self.db.query(StorageModel)
            .filter(StorageModel.waste_type == waste_type)
            .filter(StorageModel.wsa_id == id)
            .first()
        )

    def update_storage_size(
        self, storage_id: int, new_size: int
    ) -> Optional[StorageModel]:
        db_storage = self.get_storage(storage_id)
        if db_storage:
            db_storage.size = new_size
            self.db.commit()
            self.db.refresh(db_storage)
        return db_storage

    def truncate_data(self) -> None:
        self.db.query(StorageModel).delete()
        self.db.commit()
