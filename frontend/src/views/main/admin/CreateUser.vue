<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create User</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" v-model="Name" required></v-text-field>
            <v-text-field label="E-mail" type="email" v-model="Email" required></v-text-field>
            <div class="subheading secondary--text text--lighten-2">User is superuser
                <span v-if="isSuperuser">(currently is a superuser)</span>
                <span v-else>(currently is not a superuser)</span>
            </div>
            <v-checkbox label="Is Superuser" v-model="isSuperuser"></v-checkbox>

            <div class="subheading secondary--text text--lighten-2">User is active
                <span v-if="isActive">(currently active)</span>
                <span v-else>(currently not active)</span>
            </div>

            <v-checkbox label="Is Active" v-model="isActive"></v-checkbox>

            <v-layout align-center>
              <v-flex>
                <v-text-field type="password" ref="password" label="Set Password" data-vv-name="password" data-vv-delay="100" v-validate="{required: true}" v-model="Password1" :error-messages="errors.first('password')">
                </v-text-field>

                <v-text-field type="password" label="Confirm Password" data-vv-name="password_confirmation" data-vv-delay="100" data-vv-as="password" v-validate="{required: true, confirmed: 'password'}" v-model="Password2" :error-messages="errors.first('password_confirmation')">
                </v-text-field>
              </v-flex>
            </v-layout>

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
} from '@/interfaces';
import { dispatchGetUsers, dispatchCreateUser } from '@/store/admin/actions';

@Component
export default class CreateUser extends Vue {
  public valid = false;
  public Name: string = '';
  public Email: string = '';
  public isActive: boolean = true;
  public isSuperuser: boolean = false;
  public setPassword = false;
  public Password1: string = '';
  public Password2: string = '';

  public async mounted() {
    await dispatchGetUsers(this.$store);
    this.reset();
  }

  public reset() {
    this.Password1 = '';
    this.Password2 = '';
    this.Name = '';
    this.Email = '';
    this.isActive = false;
    this.isSuperuser = false;
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedProfile: IUserProfileCreate = {
        email: this.Email,
      };
      if (this.Name) {
        updatedProfile.full_name = this.Name;
      }
      if (this.Email) {
        updatedProfile.email = this.Email;
      }
      updatedProfile.is_active = this.isActive;
      updatedProfile.is_superuser = this.isSuperuser;
      updatedProfile.password = this.Password1;
      await dispatchCreateUser(this.$store, updatedProfile);
      this.$router.push('/main/admin/users');
    }
  }
}
</script>
