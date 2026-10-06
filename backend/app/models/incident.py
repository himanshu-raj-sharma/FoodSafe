# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional, List
from datetime import datetime
import enum

from .base import Base

class IncidentType(str, enum.Enum):
    CONTAMINATION = "contamination"
    TEMPERATURE_BREACH = "temperature_breach"
    FOREIGN_OBJECT = "foreign_object"
    EXPIRED_PRODUCT = "expired_product"
    ALLERGEN_ISSUE = "allergen_issue"
    HYGIENE_VIOLATION = "hygiene_violation"
    OTHER = "other"

class IncidentSeverity(str, enum.Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class IncidentStatus(str, enum.Enum):
    OPEN = "OPEN"
    INVESTIGATING = "INVESTIGATING"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    outlet_id = Column(Integer, ForeignKey("outlets.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(Enum(IncidentType), nullable=False)
    severity = Column(Enum(IncidentSeverity), nullable=False)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.OPEN)
    reported_by = Column(Integer, ForeignKey("users.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    batch_id = Column(Integer, ForeignKey("batches.id"), nullable=True)
    delivery_id = Column(Integer, ForeignKey("deliveries.id"), nullable=True)
    immediate_action = Column(Text, nullable=True)
    root_cause = Column(Text, nullable=True)
    reported_at = Column(DateTime(timezone=True), server_default=func.now())
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    outlet = relationship("Outlet", back_populates="incidents")
    reporter = relationship("User", foreign_keys=[reported_by], back_populates="incidents")
    assignee = relationship("User", foreign_keys=[assigned_to], back_populates="assigned_incidents")
    evidence = relationship("IncidentEvidence", back_populates="incident")
    timeline = relationship("IncidentTimeline", back_populates="incident")
    capas = relationship("CorrectiveAction", back_populates="incident")

    def __repr__(self):
        return f"<Incident(id={self.id}, title='{self.title}')>"
