/*
    vue-router路由
    路由相关文件
*/

import {createWebHistory, createRouter} from "vue-router";
import Home from "@/views/Home.vue";
import ArticleDetail from "@/views/ArticleDetail.vue";

/*
    routes列表
    定义所有需要挂在到路由中的路径
    成员为 路径url 路径名 路径vue对象
*/
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/article/:id", // 动态路由 :id
        name: "ArticleDetail",
        component: ArticleDetail
    }
];

/*
    创建路由
    history定义路由形式 
        使用HTML5模式 具体路径不带#, 部署时需要额外配置
        此外还有哈希模式 createWebHashHistory()
*/
const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;