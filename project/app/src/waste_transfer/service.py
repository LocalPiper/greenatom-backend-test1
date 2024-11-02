from sqlalchemy.orm import Session
from app.src.storages.service import StorageService
from app.src.organizations.service import OrganizationService
from app.src.wsas.service import WSAService
from app.src.paths.service import PathService
from app.src.waste_transfer.schemas import WasteTransferRequest

class WasteTransferService:
    def __init__(self, db: Session):
        self.db = db
        self.storage_service = StorageService(db)
        self.organization_service = OrganizationService(db)
        self.path_service = PathService(db)
        self.wsa_service = WSAService(db)

    def transfer_waste(self, transfer_data: WasteTransferRequest):
        organization = self.organization_service.get_by_name(transfer_data.organization_name)
        if not organization:
            raise ValueError("Organization not found!")
        
        