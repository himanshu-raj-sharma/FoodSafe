# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CAPABase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    root_cause: Optional[str] = Field(None, max_length=2000)
    corrective_action: str = Field(..., min_length=1, max_length=2000)
    preventive_action: Optional[str] = Field(None, max_length=2000)
    due_date: datetime
    priority: str = Field(..., pattern="^(LOW|MEDIUM|HIGH|CRITICAL)$")

class CAPACreate(CAPABase):
    incident_id: int
    organization_id: int
    assigned_to: int

class CAPAUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    root_cause: Optional[str] = Field(None, max_length=2000)
    corrective_action: Optional[str] = Field(None, min_length=1, max_length=2000)
    preventive_action: Optional[str] = Field(None, max_length=2000)
    due_date: Optional[datetime] = None
    priority: Optional[str] = Field(None, pattern="^(LOW|MEDIUM|HIGH|CRITICAL)$")
    status: Optional[str] = Field(None, pattern="^(OPEN|ASSIGNED|IN_PROGRESS|AWAITING_VERIFICATION|COMPLETED|VERIFIED|REJECTED)$")

    class Config:
        from_attributes = True

class CAPARead(CAPABase):
    id: int
    incident_id: int
    organization_id: int
    assigned_to: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True