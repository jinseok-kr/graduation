import Vue from 'vue'
import AppNewsDetail from './AppNewsDetail.vue'
import vuetify from '../plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(AppNewsDetail)
}).$mount('#app')
