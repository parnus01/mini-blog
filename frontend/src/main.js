import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from '../store/index'
import axios from 'axios'
import 'vue-awesome/icons'

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://localhost:5000';

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons)

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
