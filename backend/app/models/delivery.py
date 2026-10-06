# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    outlet_id = Column(Integer, ForeignKey("outlets.id"), nullable=False)
    delivery_date = Column(DateTime(timezone=True), nullable=False)
    status = Column(String(50), default="PENDING")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    organization = relationship("Organization")
    supplier = relationship("Supplier", back_populates="deliveries")
    outlet = relationship("Outlet")
    items = relationship("DeliveryItem", back_populates="delivery")

    def __repr__(self):
        return f"<Delivery(id={self.id}, date='{self.delivery_date}')>"
