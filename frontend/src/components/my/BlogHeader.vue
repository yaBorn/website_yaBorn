<!-- 
    组件 页眉 
        Home.vue
-->

<!-- html -->
<template>
    <!-- 页眉 -->
    <div id="header">
        <h1>yaBorn Blog</h1>
        <hr>
    </div>
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
        text-align: center;
        margin-top: 20px;
    }
</style>
