import { api } from '@/api';
import { ActionContext } from 'vuex';
import { IUserProfileCreate, IUserProfileUpdate} from '@/interfaces';
import { IDeviceProfileCreate, IDeviceProfileUpdate, IDeviceProfileDelete} from '@/interfaces';
import { IIotDeviceProfile } from '@/interfaces';
import { State } from '../state';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { commitSetUsers, commitSetUser, commitSetDevices, commitSetDevice } from './mutations';
import { commitSetIotDevices, commitSetIotDeviceRecord } from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';

type MainContext = ActionContext<AdminState, State>;

export const actions = {
    async actionGetUsers(context: MainContext) {
        try {
            const response = await api.getUsers(context.rootState.main.token);
            if (response) {
                commitSetUsers(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateUser(context: MainContext, payload: { id: number, user: IUserProfileUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateUser(context.rootState.main.token, payload.id, payload.user),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateUser(context: MainContext, payload: IUserProfileCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createUser(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionDeleteUser(context: MainContext, id: number) {
        try {
            const loadingNotification = { content: 'deleteing', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.deleteUser(context.rootState.main.token, id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully deleted', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    async actionGetDevices(context: MainContext) {
        try {
            const response = await api.getDevices(context.rootState.main.token);
            if (response) {
                commitSetDevices(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    async actionCreateDevice(context: MainContext, payload: IDeviceProfileCreate) {
        try {
            const loadingNotification = { content: 'create device', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createDevice(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetDevice(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'device successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    async actionDeleteDevice(context: MainContext, payload: IDeviceProfileDelete) {
        try {
            const loadingNotification = { content: 'delete device', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.deleteDevice(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetDevice(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Device successfully deleted', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    async actionUpdateDevice(context: MainContext, payload: { id: number, device: IDeviceProfileUpdate }) {
        try {
            const loadingNotification = { content: 'save device', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateDevice(context.rootState.main.token, payload.id, payload.device),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

    async actionGetIotDevices(context: MainContext) {
        try {
            const response = await api.getIotDevices(context.rootState.main.token);
            if (response) {
                commitSetIotDevices(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionGetIotDeviceRecords(context: MainContext, payload: { sn: string, filter_cond: string}) {
        try {
            const response = await api.getIotDeviceRecodes(context.rootState.main.token,
                        payload.sn, payload.filter_cond);
            if (response) {
                commitSetIotDeviceRecord(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },

};

const { dispatch } = getStoreAccessors<AdminState, State>('');

export const dispatchCreateUser = dispatch(actions.actionCreateUser);
export const dispatchGetUsers = dispatch(actions.actionGetUsers);
export const dispatchUpdateUser = dispatch(actions.actionUpdateUser);
export const dispatchDeleteUser = dispatch(actions.actionDeleteUser);

export const dispatchCreateDevice = dispatch(actions.actionCreateDevice);
export const dispatchGetDevices = dispatch(actions.actionGetDevices);
export const dispatchDeleteDevice = dispatch(actions.actionDeleteDevice);
export const dispatchUpdateDevice = dispatch(actions.actionUpdateDevice);

export const dispatchGetIotDevices = dispatch(actions.actionGetIotDevices);
export const dispatchGetIotDeviceRecodes = dispatch(actions.actionGetIotDeviceRecords);
