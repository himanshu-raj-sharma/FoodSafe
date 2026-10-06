# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class RiskResponse(BaseModel):
    organization_id: int
    overall_risk_score: int
    overall_risk_level: str
    outlet_risks: Dict[str, Any] = Field(default_factory=dict)
    supplier_risks: Dict[str, Any] = Field(default_factory=dict)
    incident_trends: Dict[str, Any] = Field(default_factory=dict)
    recommendations: List[str] = Field(default_factory=list)