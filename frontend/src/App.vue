<!--
 * Vue 欢迎页面
 * Vue使用组件化思想
 * <template> 标签 -> 传统的 html
 * <script> 标签 -> javascript
 * <style> 标签 -> css
-->

<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
/* HelloWorld 为封装好的组件，位于路径.. */
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
