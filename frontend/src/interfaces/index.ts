export interface IUserProfile {
    id: number;
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IDeviceProfileCreate {
    macaddr: string;
    activetime: string;
    expirationtime: string;
    description?: string;
}

export interface IDeviceProfile {
    id: number;
    macaddr: string;
    activetime: string;
    expirationtime: string;
    description: string;
}

export interface IDeviceProfileUpdate {
    id: number;
    macaddr: string;
    activetime: string;
    expirationtime: string;
    description: string;
}

export interface IDeviceProfileDelete {
    id: number;
    macaddr: string;
}

export interface IIotDeviceProfile {
    sn: string;
    time: string;
    identify: string;
    message: string;
    nfc: string;
    bluetooth: string;
}
