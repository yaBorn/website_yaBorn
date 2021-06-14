<!-- 
    main.js 注册的前端入口
        TODO:新建参数文件夹 
            存放各类字段
                vue路径字段 用于import变化
                storage字段 tokenJWT验证信息
                accessTimeJWT参数 令牌有效期 与Django后端对应
-->

<!-- html -->
<template>
    <div id="vue">
        <!-- vue-router 路由的各路径页面实际渲染位置 -->
        <router-view/>
    </div>
</template>

<!-- js -->
<script>
    export default {
        name: 'App'
    }
</script>

<!-- css -->
<style>
    #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 40px;
        margin-right: 40px;
    }
    /* html设置 */
    html {
        background: var(--backcolor);
    }
</style>
