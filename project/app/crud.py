from sqlalchemy.orm import Session
from . import models, schemas

def create_organization(db: Session, organization: schemas.OrganizationCreate):
    db_organization = models.Organization(name=organization.name)
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization