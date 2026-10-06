# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.database import get_db_session
from ..schemas.organization import OrganizationCreate, OrganizationRead, OrganizationUpdate
from ..models import Organization
from ..core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/organizations", tags=["organizations"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OrganizationRead)
async def create_organization(
    org_data: OrganizationCreate,
    db = Depends(get_db_session)
):
    """Create a new organization."""
    # Check slug is unique
    from sqlalchemy import select
    stmt = select(Organization).where(Organization.slug == org_data.slug)
    existing = db.scalar(stmt)
    if existing:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An organization with this slug already exists",
            error_code="conflicting_operation",
        )
    # Create organization
    organization = Organization(
        name=org_data.name,
        slug=org_data.slug,
        description=org_data.description,
        status=org_data.status or "active",
        tier=org_data.tier or "starter",
    )
    db.add(organization)
    db.commit()
    db.refresh(organization)
    return organization