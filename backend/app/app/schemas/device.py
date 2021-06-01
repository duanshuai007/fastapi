from typing import Optional

from pydantic import BaseModel
from datetime import datetime
'''
id = Column(Integer, primary_key=True, index=True)
macaddr = Column(String, index=True)
activetime = Column(datetime, index=True)
expirationtime = Column(datetime, index=True)
description = Column(String, index=True)
owner_id = Column(Integer, ForeignKey("user.id"))
owner = relationship("User", back_populates="items")
'''
# Shared properties
class DeviceBase(BaseModel):
    description: Optional[str] = None

# Properties to receive on item creation
class DeviceCreate(DeviceBase):
    macaddr: str
    activetime: datetime
    expirationtime: datetime

# Properties to receive on item update
class DeviceUpdate(DeviceBase):
    id : int
    macaddr : str
    activetime : datetime
    expirationtime : datetime
    pass

# Properties shared by models stored in DB
class DeviceInDBBase(DeviceBase):
    id: int
    macaddr: str
    activetime: datetime
    expirationtime: datetime

    owner_id: int
    class Config:
        orm_mode = True

# Properties to return to client
class Device(DeviceInDBBase):
    pass

# Properties properties stored in DB
class DeviceInDB(DeviceInDBBase):
    pass

class DeviceDelete(BaseModel):
    id: int
    macaddr : str

class DeviceResp(BaseModel):
    status : str
    code : int

