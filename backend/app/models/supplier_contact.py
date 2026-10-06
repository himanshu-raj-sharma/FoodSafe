# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional

from .base import Base

class SupplierContact(Base):
    __tablename__ = "supplier_contacts"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    name = Column(String(255), nullable=False)
    role = Column(String(100), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    supplier = relationship("Supplier", back_populates="contacts")

    def __repr__(self):
        return f"<SupplierContact(id={self.id}, name='{self.name}')>"
