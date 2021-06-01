<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create Device</div>
      </v-card-title>

      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="MacAddr" type="text" v-model="MacAddr" required></v-text-field>

            <div class="headline primary--text">激活时间</div>
            <v-card-text>
                <template>
                    <!-- <v-text-field label="ActiveDate" type="date" v-model="ActiveDate" required></v-text-field>
                    <v-text-field label="ActiveTime" type="time" v-model="ActiveTime" required></v-text-field> -->

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
                                    label="设置激活日期"
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
                                    label="设置激活时间"
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
                                        label="设置过期日期"
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
                                        label="设置过期时间"
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

            <v-text-field label="设备描述" type="text" v-model="description" required></v-text-field>

            <!-- <div class="subheading secondary--text text--lighten-2">User is superuser <span v-if="isSuperuser">(currently is a superuser)</span><span v-else>(currently is not a superuser)</span></div>
            <v-checkbox label="Is Superuser" v-model="isSuperuser"></v-checkbox>
            <div class="subheading secondary--text text--lighten-2">User is active <span v-if="isActive">(currently active)</span><span v-else>(currently not active)</span></div>
            <v-checkbox label="Is Active" v-model="isActive"></v-checkbox>
            -->

          </v-form>
        </template>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn @click="submit" :disabled="!valid">
              Save
            </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {
  IUserProfile,
  IUserProfileUpdate,
  IUserProfileCreate,
  IDeviceProfileCreate,
} from '@/interfaces';
import { dispatchCreateDevice } from '@/store/admin/actions';

@Component
export default class CreateDevice extends Vue {
  public valid = false;
  public MacAddr: string = '';
  // public ActiveTime: string = '';
  // public ExpirationTime: string = '';
  public description: string = '';
  public date = new Date().toISOString().substr(0, 10);
  public menuExDatePicker = false;
  public menuExTimePicker = false;
  public menuAcDatePicker = false;
  public menuAcTimePicker = false;
  public dateAc: string = '';
  public timeAc: string = '';
  public dateEx: string = '';
  public timeEx: string = '';

  public async mounted() {
    this.reset();
  }

    // public onDateChange(): void {
    //     alert(new Date().toISOString().substr(0, 10));
    // }

    // public ondatepickerclose(): void {
    //     this.menudatepicker = false;
    // }

  public reset() {
    this.MacAddr = '';
    // this.ActiveTime = '';
    this.dateAc = '';
    this.dateEx = '';
    this.timeAc = '';
    this.timeEx = '';
    // this.ExpirationTime = '';
    this.description = '';
    this.$validator.reset();
  }

  public cancel() {
    // alert('active time:' + this.dateAc + ' ' + this.timeAc + 'extime:' + this.dateEx + ' ' + this.timeEx);
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {

      const updatedProfile: IDeviceProfileCreate = {
        macaddr: this.MacAddr,
        // activetime : this.ActiveTime,
        // expirationtime : this.ExpirationTime,
        activetime : this.dateAc + ' ' + this.timeAc,
        expirationtime : this.dateEx + ' ' + this.timeEx,
      };

      if (this.description) {
        updatedProfile.description = this.description;
      }
      await dispatchCreateDevice(this.$store, updatedProfile);
      this.$router.push('/main/admin/users/device/manage');
    }
  }
}
</script>
