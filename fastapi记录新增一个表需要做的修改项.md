## fastapi:记录新增一个表需要做的修改项


- 1.在app/models下创建iotdevice.py文件，输入一下内容

```
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
```

- 2.修改`app/models/__init__.py`  
添加  
`from .iotdevice import IotDevice`


- 3.修改`app/models/user.py`文件  
在`class User(Base):`新增关系  
`iotdevice = relationship("IotDevice", back_populates="owner")`


- 4.`在app/schemas`目录创建`iotdevice.py`，输入以下内容  

```
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
```


- 5.修改`app/schemas/__init__.py`文件  
添加  
`from .iotdevice import IotDeviceBase, IotDeviceInDBBase, IotDeviceInDBNfc, IotDeviceInDBBt`


- 6.修改`app/db/base.py`文件  
增加  
`from app.models.iotdevice import IotDevice`

- 7.在`app/crud/`目录下新建`crud_iotdevice.py`文件，输入以下内容  

```
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
```


- 8.修改`app/crud/__init__.py`文件  
`from .crud_iotdevice import iotdevice`  





end
