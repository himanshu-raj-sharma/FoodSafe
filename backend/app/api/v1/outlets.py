# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...core.database import get_db_session
from ...schemas.outlet import OutletCreate, OutletRead, OutletUpdate, OutletListItem
from ...models import Outlet, Organization
from ...core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/outlets", tags=["outlets"])

def get_organization(
    org_id: int,
    db: Session = Depends(get_db_session)
) -> Organization:
    """Get organization by ID or raise 404."""
    organization = db.get(Organization, org_id)
    if not organization:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
            error_code="organization_not_found",
        )
    return organization

@router.post("/{organization_id}", status_code=status.HTTP_201_CREATED, response_model=OutletRead)
async def create_outlet(
    organization_id: int,
    outlet_data: OutletCreate,
    db = Depends(get_db_session),
):
    """Create a new outlet."""
    # Verify organization exists and is active
    organization = get_organization(organization_id, db)
    if not organization.is_active:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Organization is not active",
            error_code="insufficient_permissions",
        )
    # Check outlet code is unique within organization
    from sqlalchemy import select
    stmt = select(Outlet).where(
        Outlet.organization_id == organization_id,
        Outlet.code == outlet_data.code
    )
    existing = db.scalar(stmt)
    if existing:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An outlet with this code already exists in this organization",
            error_code="conflicting_operation",
        )
    # Create outlet
    outlet = Outlet(
        organization_id=organization_id,
        name=outlet_data.name,
        code=outlet_data.code,
        address=outlet_data.address,
        contact_person=outlet_data.contact_person,
        contact_phone=outlet_data.contact_phone,
        latitude=outlet_data.latitude,
        longitude=outlet_data.longitude,
        is_active=outlet_data.is_active or True,
    )
    db.add(outlet)
    db.commit()
    db.refresh(outlet)
    return outlet