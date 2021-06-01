<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Device Recode
      </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field label="filter conditions" v-model="filterConditions"></v-text-field>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="submit">Filter</v-btn>
    </v-toolbar>

    <v-data-table dense :headers="headers" :items="records" :items-per-page="10">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.sn }} </td>
        <td>{{ props.item.time }}</td>
        <td>{{ props.item.identify }}</td>
        <td>{{ props.item.message }}</td>
        <td>{{ props.item.nfc }}</td>
        <td>{{ props.item.bluetooth }}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { readIotDeviceRecords } from '@/store/admin/getters';
import { dispatchGetIotDeviceRecodes } from '@/store/admin/actions';

@Component
export default class IotDeviceRecords extends Vue {
  public headers = [
    {
      text: 'SN1',
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

  public filterConditions: string = '';

  public async mounted() {
    // alert(this.$router.currentRoute.params.sn);
    await dispatchGetIotDeviceRecodes(this.$store,
            {sn : this.$router.currentRoute.params.sn, filter_cond : this.filterConditions});
  }

  get records() {
    return readIotDeviceRecords(this.$store);
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
        const filterCond = this.filterConditions;
        await dispatchGetIotDeviceRecodes(this.$store,
            {sn : this.$router.currentRoute.params.sn, filter_cond : filterCond});
    }
  }
}
</script>
