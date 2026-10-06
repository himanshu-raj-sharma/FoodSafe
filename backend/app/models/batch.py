# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class Batch(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    batch_number = Column(String(100), nullable=False)
    product_name = Column(String(255), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    manufacture_date = Column(DateTime(timezone=True), nullable=True)
    expiry_date = Column(DateTime(timezone=True), nullable=True)
    quantity = Column(Float, nullable=False)
    unit = Column(String(50), nullable=True)
    storage_requirements = Column(Text, nullable=True)
    lot_number = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    organization = relationship("Organization", back_populates="batches")
    supplier = relationship("Supplier")
    deliveries = relationship("Delivery", back_populates="batch")
    traceability_events = relationship("TraceabilityEvent", back_populates="batch")
    recall_items = relationship("RecallItem", back_populates="batch")

    def __repr__(self):
        return f"<Batch(id={self.id}, number='{self.batch_number}')>"
