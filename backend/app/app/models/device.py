from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class Device(Base):
    id = Column(Integer, primary_key=True, index=True)
    macaddr = Column(String, index=True)
    activetime = Column(DateTime(timezone=True), index=True, default=func.now())
    expirationtime = Column(DateTime(timezone=True), index=True)
    description = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="devices")
