import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)

app.use(createPinia())
app.use(router)
// Optionally, make axios available globally in components
app.config.globalProperties.$axios = axios
app.mount('#app')
