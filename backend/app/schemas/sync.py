# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class SyncRequest(BaseModel):
    organization_id: int
    last_synced_at: Optional[datetime] = None
    pending_changes: List[Dict[str, Any]] = Field(default_factory=list)

class SyncResponse(BaseModel):
    sync_id: int
    status: str
    synced_at: datetime
    conflicts: List[Dict[str, Any]] = Field(default_factory=list)
    server_changes: List[Dict[str, Any]] = Field(default_factory=list)