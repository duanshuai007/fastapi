import { IUserProfile, IDeviceProfile, IIotDeviceProfile } from '@/interfaces';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setUsers(state: AdminState, payload: IUserProfile[]) {
        state.users = payload;
    },
    setUser(state: AdminState, payload: IUserProfile) {
        const users = state.users.filter((user: IUserProfile) => user.id !== payload.id);
        users.push(payload);
        state.users = users;
    },

    setDevices(state: AdminState, payload: IDeviceProfile[]) {
        state.devices = payload;
    },
    setDevice(state: AdminState, payload: IDeviceProfile) {
        const devices = state.devices.filter((device: IDeviceProfile) => device.id !== payload.id);
        devices.push(payload);
        state.devices = devices;
    },

    setIotDevices(state: AdminState, payload: IIotDeviceProfile[]) {
        state.iotdevices = payload;
    },

    setIotDeviceRecord(state: AdminState, payload: IIotDeviceProfile[]) {
        state.iotdevice_record = payload;
    },
};

const { commit } = getStoreAccessors<AdminState, State>('');

export const commitSetUser = commit(mutations.setUser);
export const commitSetUsers = commit(mutations.setUsers);

export const commitSetDevice = commit(mutations.setDevice);
export const commitSetDevices = commit(mutations.setDevices);
export const commitSetIotDevices = commit(mutations.setIotDevices);
export const commitSetIotDeviceRecord = commit(mutations.setIotDeviceRecord);
