from typing import List
from sqlalchemy.orm import Session
from app.src.organizations.repository import OrganizationRepository
from app.src.organizations.schemas import OrganizationCreate, Organization
from app.src.organizations.models import OrganizationModel


class OrganizationService:
    def __init__(self, db: Session):
        self.repository = OrganizationRepository(db)

    def create_organization(
        self, organization_data: OrganizationCreate
    ) -> Organization:
        db_org = self.repository.create_organization(organization_data)
        return Organization.from_orm(db_org)

    def get_organization(self, organization_id: int) -> OrganizationModel:
        return self.repository.get_organization(organization_id)

    def get_by_name(self, name: str) -> OrganizationModel:
        return self.repository.get_by_name(name)

    def get_all_organizations(self) -> List[Organization]:
        db_orgs = self.repository.get_all_organizations()
        return [Organization.from_orm(org) for org in db_orgs]

    def truncate_data(self) -> None:
        self.repository.truncate_data()
