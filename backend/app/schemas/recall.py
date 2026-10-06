# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class RecallBase(BaseModel):
    recall_type: str = Field(..., pattern="^(MOCK|REAL)$")
    reason: str = Field(..., min_length=1, max_length=1000)
    status: Optional[str] = Field(default="INITIATED", pattern="^(INITIATED|IN_PROGRESS|COMPLETED|CANCELLED)$")

class RecallCreate(RecallBase):
    batch_id: int

class RecallRead(RecallBase):
    id: int
    batch_id: int
    organization_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True