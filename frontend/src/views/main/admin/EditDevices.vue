<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Edit Device</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>

            <v-text-field label="Id" v-model="id" disabled required></v-text-field>

            <v-text-field label="MacAddress" type="text" v-model="macaddr" disabled required></v-text-field>

            <!-- <v-text-field
              label="ActiveTime"
              type="text"
              v-model="activetime"
              required
            ></v-text-field>
            <v-text-field
              label="ExpirationTime"
              type="text"
              v-model="expirationtime"
              required
            ></v-text-field> -->

            <div class="headline primary--text">激活时间</div>
            <v-card-text>
                <template>
                    <!-- active date picker -->
                    <v-row>
                    <v-col cols="12" sm="6" md="4" >
                        <v-menu
                            ref="menuAcDate" v-model="menuAcDatePicker"
                            :close-on-content-click="false"
                            :return-value.sync="date"
                            transition="scale-transition"
                            offset-y
                            min-width="auto"
                        >
                            <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                    v-model="dateAc"
                                    label="日期"
                                    prepend-icon="mdi-calendar"
                                    v-bind="attrs"
                                    v-on="on"
                                ></v-text-field>
                            </template>
                            <v-date-picker v-model="dateAc" no-title scrollable>
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menuAcDatePicker = false"> Cancel </v-btn>
                                <!--  or write like this
                                <v-btn text color="primary" @click="ondatepickerclose()"> Cancel </v-btn>
                                -->
                                <v-btn text color="primary" @click="$refs.menuAcDate.save(date)"> OK </v-btn>
                            </v-date-picker>
                        </v-menu>
                    </v-col>
                    </v-row>


                    <v-row>
                    <v-col cols="12" sm="6" md="4" >
                        <v-menu
                            ref="menuAcTime" v-model="menuAcTimePicker"
                            :close-on-content-click="false"
                            :return-value.sync="time"
                            transition="scale-transition"
                            offset-y
                            min-width="auto"
                        >
                            <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                    v-model="timeAc"
                                    label="时间"
                                    prepend-icon="mdi-calendar"
                                    v-bind="attrs"
                                    v-on="on"
                                ></v-text-field>
                            </template>
                            <v-time-picker v-model="timeAc" scrollable format="24hr" use-seconds >
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menuAcTimePicker = false"> Cancel </v-btn>
                                <v-btn text color="primary" @click="$refs.menuAcTime.save(time)"> OK </v-btn>
                            </v-time-picker>
                        </v-menu>
                    </v-col>
                    </v-row>
                </template>
            </v-card-text>

            <div class="headline primary--text">过期时间</div>
            <v-card-text>
                <template>
                    <!-- <v-text-field label="ExpirationDate" type="date" v-model="ExpirationDate" required></v-text-field>
                    <v-text-field label="ExpirationTime" type="time" suffix="EST" v-model="ExpirationTime" required></v-text-field> -->
                    <!-- ex date picker -->
                    <v-row>
                        <v-col cols="12" sm="6" md="4" >
                            <v-menu
                                ref="menuExDate" v-model="menuExDatePicker"
                                :close-on-content-click="false"
                                :return-value.sync="date"
                                transition="scale-transition"
                                offset-y
                                min-width="auto"
                            >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                        v-model="dateEx"
                                        label="日期"
                                        prepend-icon="mdi-calendar"
                                        v-bind="attrs"
                                        v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-date-picker v-model="dateEx" no-title scrollable>
                                    <v-spacer></v-spacer>
                                    <v-btn text color="primary" @click="menuExDatePicker = false"> Cancel </v-btn>
                                    <v-btn text color="primary" @click="$refs.menuExDate.save(date)"> OK </v-btn>
                                </v-date-picker>
                            </v-menu>
                        </v-col>
                        </v-row>

                        <v-row>
                        <v-col cols="12" sm="6" md="4" >
                            <v-menu
                                ref="menuExTime" v-model="menuExTimePicker"
                                :close-on-content-click="false"
                                :return-value.sync="time"
                                transition="scale-transition"
                                offset-y
                                min-width="auto"
                            >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                        v-model="timeEx"
                                        label="时间"
                                        prepend-icon="mdi-calendar"
                                        v-bind="attrs"
                                        v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-time-picker v-model="timeEx" scrollable format="24hr" use-seconds >
                                    <v-spacer></v-spacer>
                                    <v-btn text color="primary" @click="menuExTimePicker = false"> Cancel </v-btn>
                                    <v-btn text color="primary" @click="$refs.menuExTime.save(time)"> OK </v-btn>
                                </v-time-picker>
                            </v-menu>
                        </v-col>
                    </v-row>
                </template>
            </v-card-text>

            <v-text-field label="Description" type="text" v-model="description" required></v-text-field>

          </v-form>
        </template>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="deldev" color="red">Delete</v-btn>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn
          @click="submit"
          :disabled="!valid"
        >
          Save
        </v-btn>
      </v-card-actions>

    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { IDeviceProfile, IDeviceProfileUpdate, IDeviceProfileDelete } from '@/interfaces';
import { dispatchDeleteDevice, dispatchGetDevices, dispatchUpdateDevice } from '@/store/admin/actions';
import { readAdminOneDevice } from '@/store/admin/getters';

@Component
export default class EditDevices extends Vue {
  public valid = true;
  // public expirationtime: string = '';
  public description: string = '';
  // public activetime: string = '';
  public macaddr: string = '';
  public devname: string = '';
  public id: number = 1;
  public dateAc: string = '';
  public timeAc: string = '';
  public dateEx: string = '';
  public timeEx: string = '';

  public menuExDatePicker = false;
  public menuExTimePicker = false;
  public menuAcDatePicker = false;
  public menuAcTimePicker = false;


  public async mounted() {
    await dispatchGetDevices(this.$store);
    this.reset();
  }

  public reset() {
    this.macaddr = '';
    // this.activetime = '';
    // this.expirationtime = '';
    this.dateAc = '';
    this.dateEx = '';
    this.timeAc = '';
    this.timeEx = '';
    this.description = '';
    this.$validator.reset();
    if (this.device) {
        this.dateAc = this.device.activetime.slice(0, 10);
        this.dateEx = this.device.expirationtime.slice(0, 10);
        this.timeAc = this.device.activetime.slice(11);
        this.timeEx = this.device.expirationtime.slice(11);
        this.id = this.device.id;
        this.macaddr = this.device.macaddr;
        // this.activetime = this.device.activetime;
        // this.expirationtime = this.device.expirationtime;
        this.description = this.device.description;
    }
  }

  public async deldev() {

    if (await this.$validator.validateAll()) {
        const deleteProfile: IDeviceProfileDelete = {
            id : this.id,
            macaddr : this.macaddr,
        };
        await dispatchDeleteDevice(this.$store, deleteProfile);
        this.$router.push('/main/admin/users/device/manage');
    }
  }

  public cancel() {
    // alert('ac:' + this.dateAc + ' ' + this.timeAc + 'ex:' + this.dateEx + ' ' + this.timeEx);
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedProfile: IDeviceProfileUpdate = {
        id : this.id,
        macaddr : this.macaddr,
        // activetime : this.activetime,
        // expirationtime : this.expirationtime,
        activetime : this.dateAc + ' ' + this.timeAc,
        expirationtime : this.dateEx + ' ' + this.timeEx,
        description : this.description,
      };

      await dispatchUpdateDevice(this.$store, { id: this.device!.id, device: updatedProfile });
      this.$router.push('/main/admin/users/device/manage');
    }
  }

  get device() {
    // alert('--->get device');
    return readAdminOneDevice(this.$store)(+this.$router.currentRoute.params.id);
  }
}
</script>
