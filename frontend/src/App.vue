<!--
 * Vue使用组件化思想
 * <template> 标签 -> 传统的 html
 * <script> 标签 -> javascript
 * <style> 标签 -> css
-->

<!-- html -->
<template>
    <div id="vue">
        <router-view/>
    </div>
</template>

<!-- js -->
<script>
/* 
    Vue组件化思想
    分解成模块，增加解耦和复用
*/
    export default {
        name: 'App',
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
