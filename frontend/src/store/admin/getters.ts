import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    adminUsers: (state: AdminState) => state.users,
    adminOneUser: (state: AdminState) => (userId: number) => {
        const filteredUsers = state.users.filter((user) => user.id === userId);
        if (filteredUsers.length > 0) {
            return { ...filteredUsers[0] };
        }
    },
    adminDevices: (state: AdminState) => state.devices,
    adminOneDevice: (state: AdminState) => (userId: number) => {
        const filteredDevices = state.devices.filter((device) => device.id === userId);
        if (filteredDevices.length > 0) {
            return { ...filteredDevices[0] };
        }
    },

    adminIotDevices: (state: AdminState) => state.iotdevices,
    adminReadIotDeviceRecords: (state: AdminState) => state.iotdevice_record,
};

const { read } = getStoreAccessors<AdminState, State>('');

export const readAdminOneUser = read(getters.adminOneUser);
export const readAdminUsers = read(getters.adminUsers);
export const readAdminDevices = read(getters.adminDevices);
export const readAdminOneDevice = read(getters.adminOneDevice);
export const readAdminIotDevices = read(getters.adminIotDevices);
export const readIotDeviceRecords = read(getters.adminReadIotDeviceRecords);


