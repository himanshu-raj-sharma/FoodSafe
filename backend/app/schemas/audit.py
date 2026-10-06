# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class AuditPackBase(BaseModel):
    start_date: datetime
    end_date: datetime

class AuditPackCreate(AuditPackBase):
    organization_id: int
    outlet_id: int

class AuditPackRead(AuditPackBase):
    id: int
    organization_id: int
    outlet_id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True