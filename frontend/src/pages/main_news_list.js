import Vue from 'vue'
import AppNewsList from './AppNewsList.vue'
import vuetify from '../plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(AppNewsList)
}).$mount('#app')
