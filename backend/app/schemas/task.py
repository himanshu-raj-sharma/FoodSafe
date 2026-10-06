# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class TaskBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    category: str = Field(..., pattern="^(OPENING|TEMPERATURE|STORAGE|CLEANING|HYGIENE|EQUIPMENT|CLOSING|CUSTOM)$")
    frequency: str = Field(..., pattern="^(DAILY|WEEKLY|MONTHLY|CUSTOM)$")
    required_evidence: bool = Field(default=False)
    required_note: bool = Field(default=False)
    threshold: Optional[str] = Field(None, max_length=255)
    is_active: bool = Field(default=True)

class TaskCreate(TaskBase):
    outlet_id: int
    organization_id: int

class TaskUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    category: Optional[str] = Field(None, pattern="^(OPENING|TEMPERATURE|STORAGE|CLEANING|HYGIENE|EQUIPMENT|CLOSING|CUSTOM)$")
    frequency: Optional[str] = Field(None, pattern="^(DAILY|WEEKLY|MONTHLY|CUSTOM)$")
    required_evidence: Optional[bool] = None
    required_note: Optional[bool] = None
    threshold: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None

    class Config:
        from_attributes = True

class TaskRead(TaskBase):
    id: int
    outlet_id: int
    organization_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True