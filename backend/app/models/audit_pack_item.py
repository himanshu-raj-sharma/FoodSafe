# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class AuditPackItem(Base):
    __tablename__ = "audit_pack_items"

    id = Column(Integer, primary_key=True)
    audit_pack_id = Column(Integer, ForeignKey("audit_packs.id"), nullable=False)
    checklist_item = Column(String(255), nullable=False)
    requirement = Column(Text, nullable=True)
    status = Column(String(50), default="PENDING")  # pending, pass, fail, n/a
    findings = Column(Text, nullable=True)
    evidence_urls = Column(Text, nullable=True)  # JSON array
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    audit_pack = relationship("AuditPack", back_populates="items")

    def __repr__(self):
        return f"<AuditPackItem(id={self.id}, item='{self.checklist_item}')>"
