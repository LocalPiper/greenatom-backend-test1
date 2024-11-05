from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.organizations.schemas import OrganizationCreate, Organization
from app.src.organizations.service import OrganizationService
from app.src.database import get_db

router = APIRouter()


@router.post("/organizations/", response_model=Organization)
def create_organization(
    organization_data: OrganizationCreate, db: Session = Depends(get_db)
):
    try:
        service = OrganizationService(db)
        return service.create_organization(organization_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.get("/organizations/", response_model=List[Organization])
def get_all_organizations(db: Session = Depends(get_db)):
    service = OrganizationService(db)
    return service.get_all_organizations()
