# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.database import get_db_session
from ..schemas.batch import BatchCreate, BatchRead, BatchUpdate
from ..models import Batch, Supplier, Outlet
from ..core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/batches", tags=["batches"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BatchRead)
async def create_batch(
    batch_data: BatchCreate,
    db = Depends(get_db_session)
):
    """Create a new batch."""
    # Verify supplier exists
    supplier = db.get(Supplier, batch_data.supplier_id)
    if not supplier:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Supplier not found",
            error_code="resource_not_found",
        )
    # Verify outlet exists
    outlet = db.get(Outlet, batch_data.outlet_id)
    if not outlet:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Outlet not found",
            error_code="resource_not_found",
        )
    # Create batch
    batch = Batch(
        supplier_id=batch_data.supplier_id,
        outlet_id=batch_data.outlet_id,
        batch_number=batch_data.batch_number,
        product=batch_data.product,
        received_at=batch_data.received_at,
        expiry_date=batch_data.expiry_date,
        quantity=batch_data.quantity,
        unit=batch_data.unit,
        status=batch_data.status or "received",
    )
    db.add(batch)
    db.commit()
    db.refresh(batch)
    return batch