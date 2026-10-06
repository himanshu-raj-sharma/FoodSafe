# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class SupplierRiskEvent(Base):
    __tablename__ = "supplier_risk_events"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    event_type = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    risk_score = Column(Float, nullable=True)
    occurred_at = Column(DateTime(timezone=True), server_default=func.now())
    resolved = Column(Integer, default=0)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    supplier = relationship("Supplier", back_populates="risk_events")

    def __repr__(self):
        return f"<SupplierRiskEvent(id={self.id}, type='{self.event_type}')>"
