from sqlalchemy.orm import Session
from app.src.organizations.schemas import OrganizationCreate
from app.src.organizations.models import OrganizationModel


class OrganizationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_organization(
        self, organization: OrganizationCreate
    ) -> OrganizationModel:
        db_organization = OrganizationModel(name=organization.name)
        self.db.add(db_organization)
        self.db.commit()
        self.db.refresh(db_organization)
        return db_organization

    def get_organization(self, organization_id: int) -> OrganizationModel:
        return (
            self.db.query(OrganizationModel)
            .filter(OrganizationModel.id == organization_id)
            .first()
        )

    def get_by_name(self, name: str) -> OrganizationModel:
        return (
            self.db.query(OrganizationModel)
            .filter(OrganizationModel.name == name)
            .first()
        )

    def get_all_organizations(self) -> OrganizationModel:
        return self.db.query(OrganizationModel).all()

    def truncate_data(self) -> OrganizationModel:
        self.db.query(OrganizationModel).delete()
        self.db.commit()
