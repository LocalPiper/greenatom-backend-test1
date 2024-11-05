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
) -> Organization:
    """Creates an Organization object in a database

    Args:
        organization_data (OrganizationCreate): data for Organization creation,
        db (Session, optional): database. Defaults to Depends(get_db).

    Raises:
        HTTPException: raised if validation error occurs

    Returns:
        Organization: _description_
    """
    try:
        service = OrganizationService(db)
        return service.create_organization(organization_data)
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))


@router.get("/organizations/", response_model=List[Organization])
def get_all_organizations(db: Session = Depends(get_db)) -> List[Organization]:
    """Gets all Organizations from database

    Args:
        db (Session, optional): database. Defaults to Depends(get_db).

    Returns:
        List[Organization]: list of Organizations
    """
    service = OrganizationService(db)
    return service.get_all_organizations()
