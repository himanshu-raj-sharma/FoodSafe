# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class DeliveryItem(Base):
    __tablename__ = "delivery_items"

    id = Column(Integer, primary_key=True)
    delivery_id = Column(Integer, ForeignKey("deliveries.id"), nullable=False)
    batch_id = Column(Integer, ForeignKey("batches.id"), nullable=True)
    product_name = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String(50), nullable=True)
    temperature_at_delivery = Column(Float, nullable=True)
    condition = Column(String(100), nullable=True)
    delivered_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    received_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    delivery = relationship("Delivery", back_populates="items")
    batch = relationship("Batch")
    delivered_by_user = relationship("User", foreign_keys=[delivered_by], back_populates="delivered_items")
    received_by_user = relationship("User", foreign_keys=[received_by])

    def __repr__(self):
        return f"<DeliveryItem(id={self.id}, product='{self.product_name}')>"
