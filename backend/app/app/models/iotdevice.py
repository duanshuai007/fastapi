from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class IotDevice(Base):
    id = Column(Integer, primary_key=True, index=True)
    sn = Column(String, index=True)
    time = Column(String, index=True)
    identify = Column(String, index=True)
    message = Column(String, index=True)
    nfc = Column(String, index=True)
    bluetooth = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="iotdevice")
