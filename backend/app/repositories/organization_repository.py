# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from ..models import Organization
from .base_repository import BaseRepository

class OrganizationRepository(BaseRepository):
    """Repository for Organization entity."""

    model = Organization

    def get_by_slug(self, slug: str, organization_id: Optional[int] = None) -> Optional[Organization]:
        """Get organization by slug."""
        query = select(Organization).where(Organization.slug == slug)
        if organization_id:
            query = query.where(Organization.id != organization_id)
        result = self.db.scalar(query)
        return result

    def search(self, name: str, organization_id: Optional[int] = None) -> List[Organization]:
        """Search organizations by name."""
        query = select(Organization).where(Organization.name.ilike(f"%{name}%"))
        if organization_id:
            query = query.where(Organization.id == organization_id)
        results = self.db.execute(query).scalars().all()
        return list(results)

    def get_with_members(self, organization_id: int) -> Optional[Organization]:
        """Get organization with its members."""
        query = select(Organization).where(Organization.id == organization_id)
        result = self.db.scalar(query)
        return result