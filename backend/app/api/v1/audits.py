# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...core.database import get_db_session
from ...schemas.audit import AuditPackCreate, AuditPackRead
from ...models import AuditPack, Organization
from ...core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/audits", tags=["audits"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AuditPackRead)
async def create_audit_pack(
    audit_data: AuditPackCreate,
    db = Depends(get_db_session)
):
    """Create a new audit pack."""
    # Verify organization exists
    organization = db.get(Organization, audit_data.organization_id)
    if not organization:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
            error_code="organization_not_found",
        )
    # Create audit pack
    audit_pack = AuditPack(
        organization_id=audit_data.organization_id,
        outlet_id=audit_data.outlet_id,
        start_date=audit_data.start_date,
        end_date=audit_data.end_date,
        status="GENERATING",
    )
    db.add(audit_pack)
    db.commit()
    db.refresh(audit_pack)
    return audit_pack