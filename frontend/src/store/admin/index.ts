import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { AdminState } from './state';

const defaultState: AdminState = {
    users: [],
    devices: [],
    iotdevices: [],
    iotdevice_record: [],
};

export const adminModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
