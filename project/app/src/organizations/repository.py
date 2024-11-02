from sqlalchemy.orm import Session
from app.src.organizations.schemas import OrganizationCreate
from app.src.organizations.models import Organization

class OrganizationRepository:
    def __init__(self, db: Session):
         self.db = db
        
    def create_organization(self, organization: OrganizationCreate):
         db_organization = Organization(name = organization.name)
         self.db.add(db_organization)
         self.db.commit()
         self.db.refresh(db_organization)
         return db_organization

    def get_organization(self, organization_id: int):
         return self.db.query(Organization).filter(Organization.id == organization_id).first()
    
