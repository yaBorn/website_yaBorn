<!--
 * Vue 欢迎页面
 * Vue使用组件化思想
 * <template> 标签 -> 传统的 html
 * <script> 标签 -> javascript
 * <style> 标签 -> css
-->

<template>
    <!--- v
        打头的属性即是 Vue 的模板语法标记
        v-for 即循环可迭代元素
        info.results 对应后端数据的 json 结构。请对照后端接口进行理解
        v-bind:key 给定了循环中每个元素的主键,方便 Vue 渲染时对元素进行识别
    -->
    <div v-for="article in info.results" v-bind:key="article.url" id="articles">
        <div class="article-title">
            {{ article.title }}
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    // Vue 实例被创建时, 将 data 对象返回的所有属性加入到 Vue 的响应式系统
    // 当这些属性的值发生改变时，视图将会产生“响应”，即自动更新为新的值
    export default {
        name: 'App',
        data: function () {
        // data info 属性初始化时赋值空字符串
            return {
                info: ''
            }
        },
        // Vue 加载完成后,调用生命周期钩子 mounted() 方法
        // 通过 axios 向 Django 后端获取到文章列表数据并赋值给 info 后
        // 页面中关联的部分也会立即随之更新，而不用手动去操作页面元素
        mounted() {
            axios
                .get('/bg/article/article-list/')
                .then(response => (this.info = response.data))
        }
    }
</script>

<style>
/*
    css
    规定页面各元素的大小、位置、颜色等样式
*/
    #articles {
        padding: 10px;
    }

    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
</style>
