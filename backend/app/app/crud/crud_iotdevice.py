from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import Optional
from app.crud.base import CRUDBase
from app.models.iotdevice import IotDevice
from app.schemas.iotdevice import IotDeviceInDB, IotDeviceCreate
from sqlalchemy import and_, or_, text


class CRUDDevice(CRUDBase[IotDevice, IotDeviceInDB, IotDeviceInDB]):

    def get(self, db: Session, sn: str) -> Optional[IotDeviceInDB]:
        return db.query(self.model).filter(self.model.sn == sn).first()

    def create_with_owner(
        self, db: Session, *, obj_in: IotDeviceCreate, owner_id: int
    ) -> IotDevice:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_newest(self, db: Session, sn: str) -> Optional[IotDeviceInDB]:
        return db.query(self.model).filter(self.model.sn == sn).order_by('id')[-1]

    def get_all_record_by_sn(self, db: Session, sn: str) -> Optional[IotDeviceInDB]:
        return db.query(self.model).filter(self.model.sn == sn).order_by('id').all()

    #return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(self.model.time>="2021-05-27").all()
    def get_all_record_by_sn_filter(self, db: Session, sn: str, filtercond: str) -> Optional[IotDeviceInDB]:
        print("--->filter cond:{}".format(filtercond))
        if filtercond is None or len(filtercond) == 0:
            return db.query(self.model).filter(self.model.sn == sn).order_by('id').all()
        else:
            if '-a-' in filtercond:
                condlist = filtercond.split('-a-')
                condlast = []
                for cond in condlist:
                    #print("cond={}".format(cond))
                    if 'time' in cond:
                        if '>=' in cond:
                            c = cond.split('>=')[1]
                            condlast.append(self.model.time >= c)
                        elif '<=' in cond:
                            c = cond.split('<=')[1]
                            condlast.append(self.model.time <= c)
                        elif '==' in cond:
                            c = cond.split('==')[1]
                            cmin = "{} 00:00:00".format(c)
                            cmax = "{} 23:59:59".format(c)
                            condlast.append(self.model.time >= cmin)
                            condlast.append(self.model.time <= cmax)
                    if 'message' in cond:
                        if '==' in cond:
                            c = cond.split('==')[1]
                            condlast.append(self.model.message == c)
                    if 'nfc' in cond:
                        condlast.append(self.model.nfc.isnot(None))
                    if 'bluetooth' in cond:
                        condlast.append(self.model.bluetooth.isnot(None))
                lastconditions = and_(condlast[0], condlast[1])
                if len(condlast) > 2:
                    for i in condlast[2:]:
                        #print(i)
                        lastconditions = and_(lastconditions, i)
                print("lastconditions={}".format(lastconditions))
                return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(
                    lastconditions).all()
            else:
                #signal conditions filter
                if 'time' in filtercond:
                    if '>=' in filtercond:
                        cond = filtercond.split('>=')[1]
                        return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(
                            self.model.time >= cond).all()
                    elif '<=' in filtercond:
                        cond = filtercond.split('<=')[1]
                        return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(
                            self.model.time <= cond).all()
                    elif '==' in filtercond:
                        cond = filtercond.split('==')[1]
                        condmin = '{} 00:00:00'.format(cond)
                        condmax = '{} 23:59:59'.format(cond)
                        return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(
                            and_(self.model.time >= condmin, self.model.time <= condmax)).all()
                    pass
                elif 'message' in filtercond:
                    if '==' in filtercond:
                        cond = filtercond.split('==')[1]
                        return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(
                            self.model.message == cond).all()
                    pass
                elif 'nfc' in filtercond:
                    return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(
                        self.model.nfc.isnot(None)).all()
                    pass
                elif 'bluetooth' in filtercond:
                    return db.query(self.model).filter(self.model.sn == sn).order_by('id').filter(
                        self.model.bluetooth.isnot(None)).all()
                    pass
                else:
                    pass
            return []


    def remove(self, db: Session, sn: str) -> Optional[IotDeviceInDB]:
        obj = db.query(self.model).filter(self.model.sn == sn).first()
        db.delete(obj)
        db.commit()
        return obj


iotdevice = CRUDDevice(IotDevice)



