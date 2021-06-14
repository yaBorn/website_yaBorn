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
        components: {Doge},

        // TODO:测试 css使用 VUE管理变量
        data () {
            return {
                hei: '50px',
                color:{
                    bla: 'black',
                },
            }
        },
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
/*  <style vars="{ }"> 方法已弃用 改进https://github.com/vuejs/rfcs/pull/231 */
/* 直接使用v-bind双向数据绑定即可 */
    #footer {
        position: fixed;
        left: 0;
        bottom: 0;
        height: v-bind(hei);
        width: 100%;
        background: var(--hfcolor);
        text-align: center;
        font-weight: bold;
        color: v-bind('color.bla');
    }
</style>
