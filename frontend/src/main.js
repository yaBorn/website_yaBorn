/*
    * 将 Vue组件挂载到 public/index.html
    * 前端初始化设置可写在此处
*/
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

// 前端路由 vue-router 加载到vue
// TODO: 加载router后，页面显示空白
import router from './router'
createApp(App).use(router).mount('#app');
