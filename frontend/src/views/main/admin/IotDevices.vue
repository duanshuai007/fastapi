<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Show Iot Devices
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-text-field label="device_sn" type="text" v-model="device_sn"></v-text-field>
      <v-spacer></v-spacer>
      <v-btn color="primary">Serach</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="iotdevices">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.sn }} </td>
        <td>{{ props.item.time }}</td>
        <td>{{ props.item.identify }}</td>
        <td>{{ props.item.message }}</td>
        <td>{{ props.item.nfc }}</td>
        <td>{{ props.item.bluetooth }}</td>

        <td class="justify-center layout px-0">
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-admin-users-device-iot-record', params: {sn: props.item.sn}}">
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
import { readAdminIotDevices } from '@/store/admin/getters';
import { dispatchGetIotDevices } from '@/store/admin/actions';

@Component
export default class IotDevices extends Vue {
  public headers = [
    {
      text: 'SN',
      sortable: true,
      value: 'sn',
      align: 'left',
    },
    {
      text: 'time',
      sortable: true,
      value: 'time',
      align: 'left',
    },
    {
      text: 'identify',
      sortable: true,
      value: 'identify',
      align: 'left',
    },
    {
      text: 'message',
      sortable: true,
      value: 'message',
      align: 'left',
    },
    {
      text: 'nfc',
      sortable: true,
      value: 'nfc',
      align: 'left',
    },
    {
      text: 'bluetooth',
      sortable: true,
      value: 'bluetooth',
      align: 'left',
    },
  ];

  public id = 0;
  public timer;

  get iotdevices() {
    return readAdminIotDevices(this.$store);
  }

  public async mounted() {
    await dispatchGetIotDevices(this.$store);
    this.timer = setInterval(this.update_status, 1000);
  }

  public async update_status() {
      await dispatchGetIotDevices(this.$store);
      if (this.timer) {
        clearInterval(this.timer);
      }
      this.timer = setInterval(this.update_status, 2000);
  }

  public beforeDestroy() {
    if (this.timer) {
        clearInterval(this.timer);
    }
  }
}
</script>
