# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class TraceabilityEvent(Base):
    __tablename__ = "traceability_events"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    outlet_id = Column(Integer, ForeignKey("outlets.id"), nullable=False)
    batch_id = Column(Integer, ForeignKey("batches.id"), nullable=True)
    delivery_id = Column(Integer, ForeignKey("deliveries.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_type = Column(String(100), nullable=False)  # received, transferred, used, disposed
    quantity = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    occurred_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    organization = relationship("Organization", back_populates="traceability_events")
    outlet = relationship("Outlet", back_populates="traceability_events")
    batch = relationship("Batch", back_populates="traceability_events")
    delivery = relationship("Delivery")
    user = relationship("User", back_populates="traceability_events")

    def __repr__(self):
        return f"<TraceabilityEvent(id={self.id}, type='{self.event_type}')>"
