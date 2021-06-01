from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=List[schemas.Device])
def read_devices(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    devices = crud.device.get_multi(db, skip=skip, limit=limit)
    '''
    for dev in devices:
        print("owner_id={}".format(dev.owner_id))
        if dev.owner_id is None:
            dev.owner_id = 0
        print("id={} macaddr={} actime={} extime={} desc={}".format(dev.id, dev.macaddr, dev.activetime, dev.expirationtime, dev.description))
    '''
    return devices

@router.post("/", response_model=schemas.Device)
def create_device(
    *,
    db: Session = Depends(deps.get_db),
    device_in: schemas.DeviceCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    print("===>: create device info : {}".format(device_in))
    device = crud.device.create_with_owner(db=db, obj_in=device_in, owner_id=current_user.id)
    #if settings.EMAILS_ENABLED and device_in.macaddr:
    #    send_new_account_email(
    #        email_to=user_in.email, username=user_in.email, password=user_in.password
    #    )
    return device

@router.put("/{device_id}", response_model=schemas.Device)
def update_device(
    *,
    db: Session = Depends(deps.get_db),
    device_id: int,
    macaddr: str = Body(None),
    activetime: datetime = Body(None),
    expirationtime: datetime = Body(None),
    description : str = Body(None),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    print("{} {} {} {} {}".format(device_id, macaddr, activetime, expirationtime, description))
    #print("===>: update device info : {}".format(device_in))
    device = crud.device.get(db, id=device_id)
    if not device:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    device_in = schemas.DeviceUpdate(
        id=device_id,
        macaddr=macaddr,
        activetime=activetime,
        expirationtime=expirationtime,
        description=description,
    )
    device = crud.device.update(db, db_obj=device, obj_in=device_in)
    return device

@router.get("/{device_id}", response_model=schemas.Device)
def read_device_by_id(
    device_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    device = crud.device.get(db, id=device_id)
    '''
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    '''
    if not device:
        raise HTTPException(
            status_code=404, detail="device not exists"
        )
    return device

@router.post("/delete", response_model=schemas.DeviceResp)
def delete_device(
    *,
    db: Session = Depends(deps.get_db),
    deldev: schemas.DeviceDelete,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete a device.
    """
    print("delete device id={}".format(deldev))
    device = crud.device.get(db, id=deldev.id)
    if not device:
        raise HTTPException(
            status_code=404,
            detail="The device with this username does not exist in the system",
        )
    if device.macaddr != deldev.macaddr:
        raise HTTPException(
            status_code=400,
            detail="device macaddr error",
        )
    if not current_user:
        raise HTTPException(
            status_code=400,
            detail="Current user not superuser",
        )
    crud.device.remove(db=db, id=deldev.id)
    resp = schemas.DeviceResp(
        code=200,
        status="ok",
    )
    return resp


@router.post("/iot/create", response_model=schemas.DeviceResp)
def iot_device_create(
        *,
        db: Session = Depends(deps.get_db),
        iotdev: schemas.IotDeviceCreate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    device = crud.iotdevice.get(db, sn=iotdev.sn)
    if device:
        #print("--- {} {} {} {} {} {}".format(device.sn, device.time, device.identify, device.message, device.nfc, device.bluetooth))
        raise HTTPException(
            status_code=400,
            detail="The Device already exists"
        )
    device = crud.iotdevice.create_with_owner(db=db, obj_in=iotdev, owner_id=current_user.id)
    if device:
        return schemas.DeviceResp(status="ok", code=200)
    else:
        return schemas.DeviceResp(status="fail", code=400)


@router.post("/iot/status", response_model=schemas.DeviceResp)
def iot_device_status_handle(
        *,
        db: Session = Depends(deps.get_db),
        iotdev: schemas.IotDeviceCreate,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    update iot doorlock device status
    and save it in databases
    """
    device = crud.device.get_by_macaddr(db, macaddr=iotdev.sn)
    if not device:
        device_create = schemas.DeviceCreate(
            macaddr=iotdev.sn,
            activetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            expirationtime='2021-01-01 12:00:00',
            description='description',
            owner_id=current_user.id,
        )
        device = crud.device.create_with_owner(db, obj_in=device_create, owner_id=current_user.id)
        if not device:
            raise HTTPException(
                status_code=400,
                detail="create device failed"
            )
    '''
    device = crud.iotdevice.get(db, sn=iotdev.sn)
    if not device:
        print("---> create new iot device")
        device = crud.iotdevice.create_with_owner(db=db, obj_in=iotdev, owner_id=current_user.id)
    else:
        print("---> update iot device")
        device = crud.iotdevice.update(db, db_obj=device, obj_in=iotdev)
    '''
    device = crud.iotdevice.create_with_owner(db=db, obj_in=iotdev, owner_id=current_user.id)
    if device:
        return schemas.DeviceResp(status="ok", code=200)
    else:
        return schemas.DeviceResp(status="fail", code=400)


@router.get("/iot/all", response_model=List[schemas.IotDevice])
def read_all_iot_devices(
        *,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    #print("---> get all iot devices")
    #first:get all device sn
    devices = crud.device.get_multi(db, skip=0, limit=9999)
    #second:get every devices last message
    devices_lastmsg = []
    for dev in devices:
        devices_lastmsg.append(crud.iotdevice.get_newest(db, dev.macaddr))

    #devices = crud.iotdevice.get_multi(db, skip=0, limit=100)
    return_result = []
    for dev in devices_lastmsg:
        return_result.append(schemas.IotDevice(
            sn=dev.sn,
            time=dev.time,
            identify=dev.identify,
            message=dev.message,
            nfc=dev.nfc,
            bluetooth=dev.bluetooth,
        ))
    return return_result

@router.get("/iot/{sn}", response_model=List[schemas.IotDevice])
def read_iot_devices_by_sn(
        *,
        sn: str,
        filtercond: str = None,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    #devices = crud.iotdevice.get_all_record_by_sn(db, sn)
    devices = crud.iotdevice.get_all_record_by_sn_filter(db, sn, filtercond)
    return_result = []
    for dev in devices:
        #print("id={}".format(dev.id))
        return_result.append(schemas.IotDevice(
            sn=dev.sn,
            time=dev.time,
            identify=dev.identify,
            message=dev.message,
            nfc=dev.nfc,
            bluetooth=dev.bluetooth,
        ))
    return return_result

@router.post("/iot/del/{sn}", response_model=schemas.DeviceResp)
def del_iot_device(
        *,
        sn: str,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    print('---> del iot devices')
    result = crud.iotdevice.remove(db, sn)
    if result:
        return schemas.DeviceResp(status="ok", code=200)
    else:
        return schemas.DeviceResp(status="fail", code=400)

