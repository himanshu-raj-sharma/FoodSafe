# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class SyncRecord(Base):
    __tablename__ = "sync_records"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    entity_type = Column(String(100), nullable=False)
    entity_id = Column(Integer, nullable=False)
    action = Column(String(50), nullable=False)  # create, update, delete
    data = Column(Text, nullable=True)  # JSON
    version = Column(Integer, default=1)
    is_synced = Column(Integer, default=0)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    synced_at = Column(DateTime(timezone=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    organization = relationship("Organization", back_populates="sync_records")

    def __repr__(self):
        return f"<SyncRecord(id={self.id}, type='{self.entity_type}')>"
