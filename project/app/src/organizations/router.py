from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import OrganizationCreate, Organization
from service import OrganizationService
from app.src.database import get_db

router = APIRouter()

@router.post("/organizations/", response_model=Organization)
def create_organization(
    organization_data: OrganizationCreate,
    db: Session = Depends(get_db)
):
    service = OrganizationService(db)
    return service.create_organization(organization_data)
