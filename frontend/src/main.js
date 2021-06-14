/*
    * 将 Vue组件挂载到 public/index.html
    * 前端初始化设置可写在此处
*/
import './css/global.css'
import { createApp } from 'vue'
import App from './App.vue'

// 前端路由 vue-router 加载到vue
// createApp(App).mount('#app')
// TODO: 加载router后，页面显示空白 -> app重复创建
import router from './router'

// 扩展 URLSearchParams方法
// 用于ArticleList.vue_script_get_article_data()
URLSearchParams.prototype.myAppendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        // 比 append()多了判断值存在的情况
        this.append(key, value)
    }
};

createApp(App).use(router).mount('#app');
