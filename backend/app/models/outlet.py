# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import List, Optional
from datetime import datetime

from .base import Base
class Outlet(Base):
    __tablename__ = "outlets"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    name = Column(String(255), nullable=False)
    code = Column(String(50), nullable=False)
    address = Column(Text, nullable=True)
    contact_person = Column(String(255), nullable=True)
    contact_phone = Column(String(50), nullable=True)
    latitude = Column(String(50), nullable=True)
    longitude = Column(String(50), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    organization = relationship("Organization", back_populates="outlets")
    tasks = relationship("Task", back_populates="outlet")
    task_completions = relationship("TaskCompletion", back_populates="outlet")
    incidents = relationship("Incident", back_populates="outlet")
    deliveries = relationship("Delivery", back_populates="outlet")
    batches = relationship("Batch", back_populates="outlet")
    traceability_events = relationship("TraceabilityEvent", back_populates="outlet")
    recall_items = relationship("RecallItem", back_populates="outlet")
    audit_logs = relationship("AuditLog", back_populates="outlet")

    def __repr__(self):
        return f"<Outlet(id={self.id}, name='{self.name}', code='{self.code}')>"

    @property
    def is_operational(self) -> bool:
        return self.is_active