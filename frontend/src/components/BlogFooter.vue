<!-- 
    组件 页脚 
        Home.vue
-->

<!-- html -->
<template>
<div>
    <!-- 页脚 -->
    <router-link :to="{name:'Home'}"> <!-- 点击跳转回home -->
        <div id="footer">
            <p>yaborn.com</p>
        </div>
    </router-link>
    <div id="doge">
        <Doge/>
    </div>
</div>
</template>

<!-- js -->
<script>
import Doge from '@/components//others/Doge.vue'

    export default {
        name: 'BlogFooter',
        components: {Doge}
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
        color: black;
    }
</style>
