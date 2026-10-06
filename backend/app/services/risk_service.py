# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from ..models import Incident, Outlet, CorrectiveAction, Supplier, Batch

class RiskService:
    def __init__(self, db: Session):
        self.db = db

    def calculate_organization_risk(self, organization_id: int) -> Dict[str, Any]:
        """Calculate risk for an entire organization."""
        # Get all outlets for this organization
        outlets = self.db.query(Outlet).filter(
            Outlet.organization_id == organization_id,
            Outlet.deleted_at.is_(None)
        ).all()

        # Calculate risk for each outlet
        outlet_risks = {}
        for outlet in outlets:
            risk = self.calculate_outlet_risk(outlet.id, organization_id)
            outlet_risks[outlet.name] = risk

        # Calculate overall risk
        overall_score = 0
        for risk in outlet_risks.values():
            overall_score += risk["risk_score"]
        overall_score = overall_score // len(outlet_risks) if outlet_risks else 0
        overall_level = self._score_to_level(overall_score)

        return {
            "organization_id": organization_id,
            "overall_risk_score": overall_score,
            "overall_risk_level": overall_level,
            "outlet_risks": outlet_risks,
            "supplier_risks": {},
            "incident_trends": {},
            "recommendations": self._generate_recommendations(outlet_risks),
        }

    def calculate_outlet_risk(self, outlet_id: int, organization_id: int) -> Dict[str, Any]:
        """Calculate risk score for a specific outlet."""
        contributors = {}
        total_score = 0

        # Recent critical incidents (last 30 days)
        critical_incidents = self.db.query(Incident).filter(
            Incident.outlet_id == outlet_id,
            Incident.severity == "CRITICAL",
            Incident.reported_at >= datetime.now() - timedelta(days=30),
            Incident.deleted_at.is_(None)
        ).all()
        critical_score = len(critical_incidents) * 30
        contributors["recent_critical_incidents"] = critical_score
        total_score += critical_score

        # Temperature deviations (last 30 days)
        temp_deviations = self.db.query(Incident).filter(
            Incident.outlet_id == outlet_id,
            Incident.type == "TEMPERATURE_DEVIATION",
            Incident.reported_at >= datetime.now() - timedelta(days=30),
            Incident.deleted_at.is_(None)
        ).all()
        temp_score = len(temp_deviations) * 20
        contributors["temperature_deviations"] = temp_score
        total_score += temp_score

        # Repeated hygiene incidents (last 90 days)
        hygiene_incidents = self.db.query(Incident).filter(
            Incident.outlet_id == outlet_id,
            Incident.type == "HYGIENE_ISSUE",
            Incident.reported_at >= datetime.now() - timedelta(days=90),
            Incident.deleted_at.is_(None)
        ).all()
        hygiene_score = len(hygiene_incidents) * 15
        contributors["repeated_hygiene_incidents"] = hygiene_score
        total_score += hygiene_score

        # Overdue CAPA
        overdue_capas = self.db.query(CorrectiveAction).filter(
            CorrectiveAction.organization_id == organization_id,
            CorrectiveAction.due_date < datetime.now(),
            CorrectiveAction.status.in_(["OPEN", "ASSIGNED", "IN_PROGRESS"]),
            CorrectiveAction.deleted_at.is_(None)
        ).all()
        capa_score = len(overdue_capas) * 10
        contributors["overdue_capa"] = capa_score
        total_score += capa_score

        # Cap the score at 100
        total_score = min(total_score, 100)
        risk_level = self._score_to_level(total_score)

        return {
            "outlet_id": outlet_id,
            "risk_score": total_score,
            "risk_level": risk_level,
            "contributors": contributors,
        }

    def _score_to_level(self, score: int) -> str:
        """Convert numeric score to risk level."""
        if score >= 80:
            return "CRITICAL"
        elif score >= 60:
            return "HIGH"
        elif score >= 40:
            return "MEDIUM"
        elif score >= 20:
            return "LOW"
        else:
            return "MINIMAL"

    def _generate_recommendations(self, outlet_risks: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on risk analysis."""
        recommendations = []
        for outlet_name, risk in outlet_risks.items():
            if risk["risk_level"] in ["HIGH", "CRITICAL"]:
                recommendations.append(
                    f"Review {outlet_name} operations immediately - risk level is {risk['risk_level']}"
                )
            if risk["contributors"].get("overdue_capa", 0) > 0:
                recommendations.append(
                    f"Address overdue corrective actions at {outlet_name}"
                )
        return recommendations