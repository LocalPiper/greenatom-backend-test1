from sqlalchemy.orm import Session
from repository import OrganizationRepository
from schemas import OrganizationCreate, Organization

class OrganizationService:
    def __init__(self, db: Session):
        self.repository = OrganizationRepository(db)

    def create_organization(self, organization_data: OrganizationCreate) -> Organization:
        return self.repository.create_organization(organization_data)

    def get_organization(self, organization_id: int) -> Organization:
        return self.repository.get_organization(organization_id)
