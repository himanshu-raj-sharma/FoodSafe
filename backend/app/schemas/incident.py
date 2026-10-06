from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class IncidentBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    type: str = Field(..., pattern="^(TEMPERATURE_DEVIATION|HYGIENE_ISSUE|EXPIRED_INGREDIENT|PEST_ISSUE|CROSS_CONTAMINATION_RISK|SUPPLIER_ISSUE|EQUIPMENT_FAILURE|FOREIGN_OBJECT|CUSTOMER_COMPLAINT|OTHER)$")
    severity: str = Field(..., pattern="^(LOW|MEDIUM|HIGH|CRITICAL)$")
    reported_at: datetime
    supplier: Optional[str] = Field(None, max_length=255)
    delivery: Optional[str] = Field(None, max_length=255)
    batch: Optional[str] = Field(None, max_length=255)
    immediate_action: Optional[str] = Field(None, max_length=2000)
    root_cause: Optional[str] = Field(None, max_length=2000)
    assigned_to: Optional[int] = None

class IncidentCreate(IncidentBase):
    outlet_id: int
    organization_id: int
    reported_by: int

class IncidentUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[str] = Field(None, pattern="^(OPEN|ACKNOWLEDGED|INVESTIGATING|ACTION_REQUIRED|AWAITING_VERIFICATION|RESOLVED|CLOSED)$")
    severity: Optional[str] = Field(None, pattern="^(LOW|MEDIUM|HIGH|CRITICAL)$")
    immediate_action: Optional[str] = Field(None, max_length=2000)
    root_cause: Optional[str] = Field(None, max_length=2000)
    assigned_to: Optional[int] = None

    class Config:
        from_attributes = True

class IncidentRead(IncidentBase):
    id: int
    outlet_id: int
    organization_id: int
    reported_by: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True