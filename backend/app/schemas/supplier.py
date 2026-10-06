# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SupplierBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    contact: Optional[str] = Field(None, max_length=255)
    category: Optional[str] = Field(None, max_length=100)
    status: Optional[str] = Field(default="active", pattern="^(active|inactive|suspended)$")
    notes: Optional[str] = Field(None, max_length=1000)

class SupplierCreate(SupplierBase):
    organization_id: int

class SupplierUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    contact: Optional[str] = Field(None, max_length=255)
    category: Optional[str] = Field(None, max_length=100)
    status: Optional[str] = Field(None, pattern="^(active|inactive|suspended)$")
    notes: Optional[str] = Field(None, max_length=1000)

    class Config:
        from_attributes = True

class SupplierRead(SupplierBase):
    id: int
    organization_id: int
    risk_score: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True