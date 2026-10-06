# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.database import get_db_session
from ..schemas.supplier import SupplierCreate, SupplierRead, SupplierUpdate
from ..models import Supplier, Organization
from ..core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/suppliers", tags=["suppliers"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SupplierRead)
async def create_supplier(
    supplier_data: SupplierCreate,
    db = Depends(get_db_session)
):
    """Create a new supplier."""
    # Verify organization exists
    organization = db.get(Organization, supplier_data.organization_id)
    if not organization:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
            error_code="organization_not_found",
        )
    # Create supplier
    supplier = Supplier(
        organization_id=supplier_data.organization_id,
        name=supplier_data.name,
        contact=supplier_data.contact,
        category=supplier_data.category,
        status=supplier_data.status or "active",
        notes=supplier_data.notes,
        risk_score=0,
    )
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier