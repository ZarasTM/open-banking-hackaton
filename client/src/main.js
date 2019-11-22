import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuent from 'vuent'

Vue.config.productionTip = false
Vue.use(Vuent)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
