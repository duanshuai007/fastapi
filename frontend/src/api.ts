import axios from 'axios';
import { apiUrl } from '@/env';
import { IUserProfile, IUserProfileUpdate, IUserProfileCreate } from './interfaces';
import { IDeviceProfileCreate, IDeviceProfile, IDeviceProfileUpdate, IDeviceProfileDelete } from './interfaces';
import { IIotDeviceProfile } from './interfaces';

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(`${apiUrl}/api/v1/users/me`, data, authHeaders(token));
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async deleteUser(token: string, userId: number) {
    return axios.post(`${apiUrl}/api/v1/users/delete`, userId, authHeaders(token));
  },


  async updateDevice(token: string, devid: number, data: IDeviceProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/device/${devid}`, data, authHeaders(token));
  },
  async deleteDevice(token: string, payload: IDeviceProfileDelete) {
    return axios.post(`${apiUrl}/api/v1/device/delete`, payload, authHeaders(token));
  },

  async getDevices(token: string) {
    return axios.get<IDeviceProfile[]>(`${apiUrl}/api/v1/device/`, authHeaders(token));
  },

  async getIotDevices(token: string) {
    return axios.get<IIotDeviceProfile[]>(`${apiUrl}/api/v1/device/iot/all`, authHeaders(token));
  },

  async getIotDeviceRecodes(token: string, sn: string, filterCond: string) {
    return axios.get<IIotDeviceProfile[]>(`${apiUrl}/api/v1/device/iot/${sn}?filtercond=${filterCond}`,
            authHeaders(token));
  },

  async createDevice(token: string, data: IDeviceProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/device/`, data, authHeaders(token));
  },

  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token,
    });
  },
};
