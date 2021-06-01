fastapi 

修改数据苦添加新的表或者修改表的内容后,通过以下操作使其生效

1.进入容器：
sudo docker-compose exec backend[镜像名而不是容器名] bash
2.提交更改
alembic revision --autogenerate -m "Add column last_name to User model"
3.使更改的内容生效
alembic upgrade head




```

<v-card-text>
    <template>
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
    </template>
</v-card-text>

在
@Component
export default class EditUser extends Vue {
}
中新增变量
public menuExDatePicker = false;
用来对日期/时间栏的关闭进行控制，如果不定义则无法通过Cancel按钮关闭菜单。

public dateAc: string = '';
通过该变量可以读取到设置的日期/时间值.

其中上面代码中的 ref="menuExDate" 和<v-btn text color="primary" @click="$refs.menuExDate.save(date)"> OK </v-btn>需要定义相同名称的menuExDate, OK按钮才能正确保存设置的值.
<v-text-field
    v-model="dateEx"
和<v-date-picker v-model="dateEx" no-title scrollable>
中的v-model也要设置为相同的值才能正确的保存设置的值。

```








### 从数据库中读去读

```
在ManageDevice.vue中有
  public async mounted() {
    await dispatchGetDevices(this.$store);
  }

在页面加载后自动请求device信息
在action.ts中
export const dispatchGetDevices = dispatch(actions.actionGetDevices);

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

其中api.getDevices
  async getDevices(token: string) {
    return axios.get<IDeviceProfile[]>(`${apiUrl}/api/v1/device/`, authHeaders(token));
  },  

获取到数据信息后执行commitSetDevices将信息保存在本地
在mutations.ts中
export const commitSetDevices = commit(mutations.setDevices);
    setDevices(state: AdminState, payload: IDeviceProfile[]) {
        state.devices = payload;
    },  
其中AdminState的定义是
export interface AdminState {
    users: IUserProfile[];
    devices: IDeviceProfile[];
}

以上步骤执行完成以后获取到的device信息就保存在了state.devices中了。


当打开EditDevice.vue时,页面加载完成后执行了
    public async mounted() {
    await dispatchGetDevices(this.$store);
    this.reset();
  }
    
在页面定义了获取设备信息的函数，根据id号码获取设备的具体信息
    get device() {
        return readAdminOneDevice(this.$store)(+this.$router.currentRoute.params.id);
    }   

在reset函数中，调用了this.device执行get device函数。获取到正确的设备信息
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
```

### 设置文本栏不可修改

<v-text-field label="Id" v-model="id" disabled required></v-text-field>

只需要添加disabled属性即可。



