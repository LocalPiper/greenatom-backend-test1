# script.py

from sqlalchemy.orm import Session
from app.src.organizations.service import OrganizationService
from app.src.wsas.service import WSAService
from app.src.storages.service import StorageService
from app.src.paths.service import PathService
from app.src.organizations.schemas import OrganizationCreate
from app.src.wsas.schemas import WSACreate
from app.src.storages.schemas import StorageCreate
from app.src.paths.schemas import PathCreate
from enum import Enum

class WasteType(str, Enum):
    BIO = "bio"
    GLASS = "glass"
    PLASTIC = "plastic"

def create_sample_data(db: Session):
    org_service = OrganizationService(db)
    wsa_service = WSAService(db)
    storage_service = StorageService(db)
    path_service = PathService(db)

    # Create Organizations
    org1 = org_service.create_organization(OrganizationCreate(name="Org 1"))
    org2 = org_service.create_organization(OrganizationCreate(name="Org 2"))

    # Create WSAs
    wsa1 = wsa_service.create_wsa(WSACreate(name="WSA 1"))
    wsa2 = wsa_service.create_wsa(WSACreate(name="WSA 2"))
    wsa3 = wsa_service.create_wsa(WSACreate(name="WSA 3"))
    wsa5 = wsa_service.create_wsa(WSACreate(name="WSA 5"))
    wsa6 = wsa_service.create_wsa(WSACreate(name="WSA 6"))
    wsa7 = wsa_service.create_wsa(WSACreate(name="WSA 7"))
    wsa8 = wsa_service.create_wsa(WSACreate(name="WSA 8"))
    wsa9 = wsa_service.create_wsa(WSACreate(name="WSA 9"))

    # Create Storage for Organizations
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=10,
        organization_id=org1.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.GLASS,
        size=0,
        capacity=50,
        organization_id=org1.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=50,
        organization_id=org1.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=60,
        organization_id=org2.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.GLASS,
        size=0,
        capacity=20,
        organization_id=org2.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=50,
        organization_id=org2.id
    ))

    # Create Storage for WSAs
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.GLASS,
        size=0,
        capacity=300,
        wsa_id=wsa1.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=100,
        wsa_id=wsa1.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=50,
        wsa_id=wsa2.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=150,
        wsa_id=wsa2.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=10,
        wsa_id=wsa3.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=250,
        wsa_id=wsa3.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.GLASS,
        size=0,
        capacity=220,
        wsa_id=wsa5.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=25,
        wsa_id=wsa5.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.GLASS,
        size=0,
        capacity=100,
        wsa_id=wsa6.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=150,
        wsa_id=wsa6.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=100,
        wsa_id=wsa7.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=250,
        wsa_id=wsa7.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.GLASS,
        size=0,
        capacity=35,
        wsa_id=wsa8.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=25,
        wsa_id=wsa8.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=52,
        wsa_id=wsa8.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.PLASTIC,
        size=0,
        capacity=250,
        wsa_id=wsa9.id
    ))
    storage_service.create_storage(StorageCreate(
        waste_type=WasteType.BIO,
        size=0,
        capacity=20,
        wsa_id=wsa9.id
    ))

    # Create Paths
    path_service.create_path(PathCreate(
        length=100,
        bidirectional=False,
        organization_id=org1.id,
        wsa_start_id=wsa1.id
    ))
    path_service.create_path(PathCreate(
        length=50,
        bidirectional=False,
        organization_id=org1.id,
        wsa_start_id=wsa2.id
    ))
    path_service.create_path(PathCreate(
        length=600,
        bidirectional=False,
        organization_id=org1.id,
        wsa_start_id=wsa3.id
    ))
    path_service.create_path(PathCreate(
        length=50,
        bidirectional=False,
        organization_id=org2.id,
        wsa_start_id=wsa3.id
    ))
    path_service.create_path(PathCreate(
        length=500,
        bidirectional=False,
        wsa_start_id=wsa1.id,
        wsa_end_id=wsa8.id
    ))
    path_service.create_path(PathCreate(
        length=50,
        bidirectional=True,
        wsa_start_id=wsa2.id,
        wsa_end_id=wsa5.id
    ))
    path_service.create_path(PathCreate(
        length=600,
        bidirectional=False,
        wsa_start_id=wsa3.id,
        wsa_end_id=wsa6.id
    ))
    path_service.create_path(PathCreate(
        length=50,
        bidirectional=True,
        wsa_start_id=wsa3.id,
        wsa_end_id=wsa7.id
    ))
    path_service.create_path(PathCreate(
        length=10,
        bidirectional=True,
        wsa_start_id=wsa8.id,
        wsa_end_id=wsa9.id
    ))

    db.commit()
