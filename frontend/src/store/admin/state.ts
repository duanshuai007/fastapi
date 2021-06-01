import { IUserProfile, IDeviceProfile, IIotDeviceProfile } from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    devices: IDeviceProfile[];
    iotdevices: IIotDeviceProfile[];
    iotdevice_record: IIotDeviceProfile[];
}

