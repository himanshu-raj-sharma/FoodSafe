# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class RecallItem(Base):
    __tablename__ = "recall_items"

    id = Column(Integer, primary_key=True)
    recall_id = Column(Integer, ForeignKey("recalls.id"), nullable=False)
    outlet_id = Column(Integer, ForeignKey("outlets.id"), nullable=True)
    batch_id = Column(Integer, ForeignKey("batches.id"), nullable=True)
    product_name = Column(String(255), nullable=False)
    quantity_recalled = Column(Float, nullable=False)
    quantity_returned = Column(Float, default=0)
    status = Column(String(50), default="PENDING")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    recall = relationship("Recall", back_populates="items")
    outlet = relationship("Outlet", back_populates="recall_items")
    batch = relationship("Batch", back_populates="recall_items")

    def __repr__(self):
        return f"<RecallItem(id={self.id}, product='{self.product_name}')>"
