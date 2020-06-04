import Vue from 'vue'
import Antd from 'ant-design-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'ant-design-vue/dist/antd.css'
import axios from 'axios'

import { message,notification } from 'ant-design-vue'
/* import message from "ant-design-vue/lib/message/index" */

Vue.config.productionTip = false

// Vue.prototype.$appName = 'My App'
Vue.prototype.$http = axios

message.config({
  top: `100px`,
  duration: 2,
  maxCount: 3,
});

Vue.use(Antd)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
