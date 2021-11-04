import Vue from 'vue'
import AppNewsScrap from './AppNewsScrap.vue'
import vuetify from '../plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(AppNewsScrap)
}).$mount('#app')
