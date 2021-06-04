<!-- 
    组件 页脚 
        Home.vue
-->

<!-- html -->
<template>
    <!-- 页脚 -->
    <div id="footer">
        <p>yaborn.com</p>
    </div>
</template>

<!-- js -->
<script>
    export default {
        name: 'BlogFooter',
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
    #footer {
        position: fixed;
        left: 0;
        bottom: 0;
        height: 50px;
        width: 100%;
        background: whitesmoke;
        text-align: center;
        font-weight: bold;
    }
</style>
