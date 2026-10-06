# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class AuditPack(Base):
    __tablename__ = "audit_packs"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    outlet_id = Column(Integer, ForeignKey("outlets.id"), nullable=True)
    pack_name = Column(String(255), nullable=False)
    audit_type = Column(String(50), nullable=False)
    scheduled_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(String(50), default="SCHEDULED")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    organization = relationship("Organization", back_populates="audit_packs")
    outlet = relationship("Outlet")
    items = relationship("AuditPackItem", back_populates="audit_pack")

    def __repr__(self):
        return f"<AuditPack(id={self.id}, name='{self.pack_name}')>"
