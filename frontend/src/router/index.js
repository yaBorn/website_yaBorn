/*
    vue-router 前端路由 地址分配
*/

import {createWebHistory, createRouter} from "vue-router";
import Home from "@/views/Home.vue";
import ArticleDetail from "@/views/ArticleDetail.vue";

/* routes列表
    定义所有挂载到路由中的路径
    成员：路径url 路径名 路径对应vue对象
*/
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/article/:id", // 动态路由 冒号:id 来定义
        // 文章列表组件 对应 id修改
        name: "ArticleDetail",
        component: ArticleDetail
    }
];

/* 创建vue-router
    hostory：路由模式
        此为HTML5模式，详细路径中无#符号，部署时需要额外配置
        此外还有哈希模式createWebHashiHistory()
*/
const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;