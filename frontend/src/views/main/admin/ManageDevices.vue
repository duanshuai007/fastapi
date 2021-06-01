<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Devices
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/device/manage">Manage Devices</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="devices">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.id }} </td>
        <td>{{ props.item.macaddr}}</td>
        <td>{{ props.item.activetime}}</td>
        <td>{{ props.item.expirationtime}}</td>
        <td>{{ props.item.description}}</td>

        <!-- <td><v-icon v-if="props.item.is_active">checkmark</v-icon></td> -->
        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-admin-users-device-edit', params: {id: props.item.id}}">
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
        </td>

      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IDeviceProfile } from '@/interfaces';
import { readAdminUsers, readAdminDevices } from '@/store/admin/getters';
import { dispatchGetDevices } from '@/store/admin/actions';

@Component
export default class ManageDevices extends Vue {
  public headers = [
    {
      text: 'Id',
      sortable: true,
      value: 'id',
      align: 'left',
    },
    {
      text: 'MacAddress',
      sortable: true,
      value: 'macaddr',
      align: 'left',
    },
    {
      text: 'ActiveTime',
      sortable: true,
      value: 'activetime',
      align: 'left',
    },
    {
      text: 'ExpirationTime',
      sortable: true,
      value: 'expirationtime',
      align: 'left',
    },
    {
      text: 'Description',
      sortable: true,
      value: 'description',
      align: 'left',
    },
  ];

  get devices() {
    return readAdminDevices(this.$store);
  }

  public async mounted() {
    await dispatchGetDevices(this.$store);
  }
}
</script>
