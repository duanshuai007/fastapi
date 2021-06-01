from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import Optional
from app.crud.base import CRUDBase
from app.models.device import Device
from app.schemas.device import DeviceCreate, DeviceUpdate


class CRUDDevice(CRUDBase[Device, DeviceCreate, DeviceUpdate]):
    def get_by_macaddr(self, db: Session, *, macaddr: str) -> Optional[Device]:
        return db.query(self.model).filter(Device.macaddr == macaddr).first()

    def create_with_owner(
        self, db: Session, *, obj_in: DeviceCreate, owner_id: int
    ) -> Device:
        print("===>curd device create_with_owner:{} {}".format(obj_in, owner_id))
        print("===>db = {}".format(db))
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Device]:
        return (
            db.query(self.model)
            .filter(Device.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


device = CRUDDevice(Device)
