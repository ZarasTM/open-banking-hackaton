import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import QRCode from 'qrcode'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(QRCode)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
