
from typing import Optional

from pydantic import BaseModel
from datetime import datetime

# Shared properties
#class IotDeviceBase(BaseModel):
#    message: Optional[str] = None
#    nfc: Optional[str] = None
#    bluetooth: Optional[str] = None

# Properties shared by models stored in DB
class IotDeviceInDB(BaseModel):
    id: int
    sn: str
    time: Optional[str] = None
    identify: Optional[str] = None
    message: Optional[str] = None
    nfc: Optional[str] = None
    bluetooth: Optional[str] = None

    #if not add this code, will orcuse
    #value is not a valid dict (type=type_error.dict)
    owner_id: int
    class Config:
        orm_mode = True

class IotDeviceCreate(BaseModel):
    sn: str
    time: Optional[str] = None
    identify: Optional[str] = None
    message: Optional[str] = None
    nfc: Optional[str] = None
    bluetooth: Optional[str] = None

class IotDevice(IotDeviceCreate):
    pass


