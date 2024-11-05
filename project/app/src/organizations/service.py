from typing import List
from sqlalchemy.orm import Session
from app.src.organizations.repository import OrganizationRepository
from app.src.organizations.schemas import OrganizationCreate
from app.src.organizations.models import Organization


class OrganizationService:
    def __init__(self, db: Session):
        self.repository = OrganizationRepository(db)

    def create_organization(
        self, organization_data: OrganizationCreate
    ) -> Organization:
        return self.repository.create_organization(organization_data)

    def get_organization(self, organization_id: int) -> Organization:
        return self.repository.get_organization(organization_id)

    def get_by_name(self, name: str) -> Organization:
        return self.repository.get_by_name(name)

    def get_all_organizations(self) -> List[Organization]:
        return self.repository.get_all_organizations()

    def truncate_data(self) -> None:
        self.repository.truncate_data()
