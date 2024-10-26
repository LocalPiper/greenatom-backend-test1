from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/organization/", response_model=schemas.OrganizationCreate)
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(database.get_db)):
    return crud.create_organization(db=db, organization=organization)