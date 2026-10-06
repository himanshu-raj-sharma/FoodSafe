# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BatchBase(BaseModel):
    batch_number: str = Field(..., min_length=1, max_length=100)
    product: str = Field(..., min_length=1, max_length=255)
    received_at: datetime
    expiry_date: datetime
    quantity: float = Field(..., gt=0)
    unit: str = Field(..., min_length=1, max_length=50)
    status: Optional[str] = Field(default="received", pattern="^(received|in_use|expired|consumed|recalled)$")

class BatchCreate(BatchBase):
    supplier_id: int
    outlet_id: int

class BatchUpdate(BaseModel):
    batch_number: Optional[str] = Field(None, min_length=1, max_length=100)
    product: Optional[str] = Field(None, min_length=1, max_length=255)
    received_at: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    quantity: Optional[float] = Field(None, gt=0)
    unit: Optional[str] = Field(None, min_length=1, max_length=50)
    status: Optional[str] = Field(None, pattern="^(received|in_use|expired|consumed|recalled)$")

    class Config:
        from_attributes = True

class BatchRead(BatchBase):
    id: int
    supplier_id: int
    outlet_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True