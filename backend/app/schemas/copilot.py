# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class CopilotRequest(BaseModel):
    organization_id: int
    question: str = Field(..., min_length=1, max_length=1000)
    context: Optional[Dict[str, Any]] = None

class CopilotResponse(BaseModel):
    request_id: str
    answer: str
    suggestions: List[str] = Field(default_factory=list)
    confidence: Optional[float] = None
    requires_human_review: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)