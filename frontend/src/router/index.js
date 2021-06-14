/*
    vue-router 前端路由 地址分配
*/

import {createWebHistory, createRouter} from "vue-router"
import Home from "@/views/Home.vue"
import ArticleDetail from "@/views/ArticleDetail.vue"
import Login from "@/views/Login.vue"
import UserCenter from "@/views/UserCenter.vue"
import ArticleCreate from "@/views/ArticleCreate.vue";
import ArticleEdit from "@/views/ArticleEdit.vue";
import gloCss from "@/cssTest.vue";

/* routes列表
    定义所有挂载到路由中的路径
    成员：路径url 路径名 路径对应vue对象 (注意import该对象)
*/
const routes = [
    // css 测试页面 部署时删去
    {
        path: "/testCss",
        name: "gloCss",
        component: gloCss,
    },
    // 主页面
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    // 文章详情页面
    {
        path: "/article/:id", // 动态路由 冒号:id 来定义
        // 文章列表组件 对应 id修改
        name: "ArticleDetail",
        component: ArticleDetail,
    },
    // 用户注册登录页面
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    // 用户中心页面
    {
        path: "/user/:username",
        name: "UserCenter",
        component: UserCenter,
    },
    // 发表文章页面
    {
        path: "/article/create",
        name: "ArticleCreate",
        component: ArticleCreate
    },
    // 文章更新删除页面
    {
        path: "/article/edit/:id",
        name: "ArticleEdit",
        component: ArticleEdit
    },
]

/* 创建vue-router
    hostory：路由模式
        此为HTML5模式，详细路径中无#符号，部署时需要额外配置
        此外还有哈希模式createWebHashiHistory()
*/
const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router