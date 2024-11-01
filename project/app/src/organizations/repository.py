from sqlalchemy.orm import Session
import schemas, models

class OrganizationRepository:
    def __init__(self, db: Session):
         self.db = db
        
    def create_organization(self, organization: schemas.OrganizationCreate):
         db_organization = models.Organization(name = organization.name)
         self.db.add(db_organization)
         self.db.commit()
         self.db.refresh(db_organization)
         return db_organization

    def get_organization(self, organization_id: int):
         return self.db.query(models.Organization).filter(models.Organization.id == organization_id).first()
    
