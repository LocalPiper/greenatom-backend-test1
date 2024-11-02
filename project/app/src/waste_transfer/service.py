from typing import List
from sqlalchemy.orm import Session
from app.src.storages.service import StorageService
from app.src.organizations.service import OrganizationService
from app.src.wsas.service import WSAService
from app.src.paths.service import PathService
from app.src.waste_transfer.schemas import WasteTransferRequest
from app.src.storages.models import Storage

class WasteTransferService:
    def __init__(self, db: Session):
        self.db = db
        self.storage_service = StorageService(db)
        self.organization_service = OrganizationService(db)
        self.path_service = PathService(db)
        self.wsa_service = WSAService(db)

    def transfer_waste(self, transfer_data: WasteTransferRequest):
        # find organization
        organization = self.organization_service.get_by_name(transfer_data.organization_name)
        if not organization:
            raise ValueError("Organization not found!")
        
        # find storage that is going to be unloaded
        storages : List[Storage] = self.storage_service.get_all_storages()
        storage : Storage = None
        for s in storages:
            if (s.organization_id == organization.id) and (s.waste_type == transfer_data.waste_type):
                storage = s
                break
        
        if not storage:
            raise ValueError("Storage not found!")
        