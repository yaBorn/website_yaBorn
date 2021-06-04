<!-- 
    组件 页眉 
        Home.vue
-->

<!-- html -->
<template>
    <!-- 页眉 -->
    <router-link :to="{name:'Home'}"> <!-- 点击跳转回home -->
        <div id="header">
            <h1>yaBorn Blog</h1>
            <hr>
        </div>
    </router-link>
</template>

<!-- js -->
<script>
    export default {
        name: 'BlogHeader',
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
    #header {
        text-decoration: none;
        text-align: center;
        margin-top: 20px;
        color: black;
    }
</style>
