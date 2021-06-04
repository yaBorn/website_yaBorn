<!-- 
    main.js 注册的前端入口
-->

<!-- html -->
<template>
    <div id="vue">
        <BlogHeader/>
        <BlogFooter/>
        <!-- vue-router 路由的各路径页面实际渲染位置 -->
        <!-- <router-view/> -->
    </div>
</template>

<!-- js -->
<script>
    import BlogHeader from '@/components/my/BlogHeader.vue'
    import BlogFooter from '@/components/my/BlogFooter.vue'

    export default {
        name: 'App',
        components: { BlogHeader, BlogFooter}
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
