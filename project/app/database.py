from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from .models import Organization, WSA, Storage, Path, WasteType

DATABASE_URL = "postgresql://fastapi:fastapi@db/project"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        create_sample_data(db)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_sample_data(db: Session):
    if db.query(Organization).first() is None:
        org1 = Organization(name="Org 1")
        org2 = Organization(name="Org 2")

        wsa1 = WSA(name="WSA 1")
        wsa2 = WSA(name="WSA 2")
        wsa3 = WSA(name="WSA 3")
        wsa5 = WSA(name="WSA 5")
        wsa6 = WSA(name="WSA 6")
        wsa7 = WSA(name="WSA 7")
        wsa8 = WSA(name="WSA 8")
        wsa9 = WSA(name="WSA 9")

        storageOrg1P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=10, organization=org1)
        storageOrg1G = Storage(waste_type=WasteType.GLASS, size=0, capacity=50, organization=org1)
        storageOrg1B = Storage(waste_type=WasteType.BIO, size=0, capacity=50, organization=org1)
        storageOrg2P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=60, organization=org2)
        storageOrg2G = Storage(waste_type=WasteType.GLASS, size=0, capacity=20, organization=org2)
        storageOrg2B = Storage(waste_type=WasteType.BIO, size=0, capacity=50, organization=org2)
        storageWsa1G = Storage(waste_type=WasteType.GLASS, size=0, capacity=300, wsa=wsa1)
        storageWsa1P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=100, wsa=wsa1)
        storageWsa2P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=50, wsa=wsa2)
        storageWsa2B = Storage(waste_type=WasteType.BIO, size=0, capacity=150, wsa=wsa2)
        storageWsa3P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=10, wsa=wsa3)
        storageWsa3B = Storage(waste_type=WasteType.BIO, size=0, capacity=250, wsa=wsa3)
        storageWsa5G = Storage(waste_type=WasteType.GLASS, size=0, capacity=220, wsa=wsa5)
        storageWsa5B = Storage(waste_type=WasteType.BIO, size=0, capacity=25, wsa=wsa5)
        storageWsa6G = Storage(waste_type=WasteType.GLASS, size=0, capacity=100, wsa=wsa6)
        storageWsa6B = Storage(waste_type=WasteType.BIO, size=0, capacity=150, wsa=wsa6)
        storageWsa7P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=100, wsa=wsa7)
        storageWsa7B = Storage(waste_type=WasteType.BIO, size=0, capacity=250, wsa=wsa7)
        storageWsa8G = Storage(waste_type=WasteType.GLASS, size=0, capacity=35, wsa=wsa8)
        storageWsa8P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=25, wsa=wsa8)
        storageWsa8B = Storage(waste_type=WasteType.BIO, size=0, capacity=52, wsa=wsa8)
        storageWsa9P = Storage(waste_type=WasteType.PLASTIC, size=0, capacity=250, wsa=wsa9)
        storageWsa9B = Storage(waste_type=WasteType.BIO, size=0, capacity=20, wsa=wsa9)

        pathO1_1 = Path(length=100, bidirectional=False, organization_id=org1.id, wsa_start_id=wsa1.id)
        pathO1_2 = Path(length=50, bidirectional=False, organization_id=org1.id, wsa_start_id=wsa2.id)
        pathO1_3 = Path(length=600, bidirectional=False, organization_id=org1.id, wsa_start_id=wsa3.id)
        pathO2_3 = Path(length=50, bidirectional=False, organization_id=org2.id, wsa_start_id=wsa3.id)
        pathW1_8 = Path(length=500, bidirectional=False, wsa_start_id=wsa1.id, wsa_end_id=wsa8.id)
        pathW2_5 = Path(length=50, bidirectional=True, wsa_start_id=wsa2.id, wsa_end_id=wsa5.id)
        pathW3_6 = Path(length=600, bidirectional=False, wsa_start_id=wsa3.id, wsa_end_id=wsa6.id)
        pathW3_7 = Path(length=50, bidirectional=True, wsa_start_id=wsa3.id, wsa_end_id=wsa7.id)
        pathW8_9 = Path(length=10, bidirectional=True, wsa_start_id=wsa8.id, wsa_end_id=wsa9.id)
    

        db.add_all([org1, 
                    org2, 
                    wsa1, 
                    wsa2, 
                    wsa3,
                    wsa5,
                    wsa6,
                    wsa7,
                    wsa8,
                    wsa9,
                    storageOrg1P,
                    storageOrg1G,
                    storageOrg1B,
                    storageOrg2P,
                    storageOrg2G,
                    storageOrg2B,
                    storageWsa1P,
                    storageWsa1G,
                    storageWsa2P,
                    storageWsa2B,
                    storageWsa3P,
                    storageWsa3B,
                    storageWsa5G,
                    storageWsa5B,
                    storageWsa6G,
                    storageWsa6B,
                    storageWsa7P,
                    storageWsa7B,
                    storageWsa8P,
                    storageWsa8G,
                    storageWsa8B,
                    storageWsa9P,
                    storageWsa9B,
                    pathO1_1,
                    pathO1_2,
                    pathO1_3,
                    pathO2_3,
                    pathW1_8,
                    pathW2_5,
                    pathW3_6,
                    pathW3_7,
                    pathW8_9])
        db.commit()