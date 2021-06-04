<!-- 
    main.js 注册的前端入口
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
</style>
