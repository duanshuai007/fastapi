fastapi:记录新增一个表需要做的修改项



在app/models下创建iotdevice.py文件，输入一下内容

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
    owner = relationship("User", back_populates="iot_doorlock")

修改app/models/__init__.py
添加
from .iotdevice import IotDevice

修改app/models/user.py文件
在class User(Base):新增关系
iotdevice = relationship("IotDevice", back_populates="owner")


在app/schemas目录创建iotdevice.py，输入以下内容

from typing import Optional

from pydantic import BaseModel
from datetime import datetime

# Shared properties
class IotDeviceBase(BaseModel):
    sn: str

# Properties shared by models stored in DB
class IotDeviceInDBBase(IotDeviceBase):
    time: str
    identify: str
    messgae: str

class IotDeviceInDBNfc(IotDeviceBase):
    nfc: str

class IotDeviceInDBBt(IotDeviceBase):
    bluetooth: str


修改app/schemas/__init__.py文件
添加
from .iotdevice import IotDeviceBase, IotDeviceInDBBase, IotDeviceInDBNfc, IotDeviceInDBBt



修改app/db/base.py文件
增加
from app.models.iotdevice import IotDevice

在app/crud/目录下新建crud_iotdevice.py文件，输入以下内容
from typing import List
 
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import Optional
from app.crud.base import CRUDBase
from app.models.iotdevice import IotDevice
from app.schemas.iotdevice import IotDeviceInDBBase, IotDeviceInDBNfc, IotDeviceInDBBt


class CRUDDevice(CRUDBase[IotDevice, IotDevice, IotDevice]):
    pass

iotdevice = CRUDDevice(IotDevice)


修改app/crud/__init__.py文件
from .crud_iotdevice import iotdevice






