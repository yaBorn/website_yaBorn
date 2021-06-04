
<!--  frontend/src/App.vue  -->

<!-- html -->
<template>
    <div id="app">
        <!-- vue-router路由 路径页面实际渲染位置 -->
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
