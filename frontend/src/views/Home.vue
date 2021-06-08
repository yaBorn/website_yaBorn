<!--
    Home 页面 文章列表 
-->

<!-- html -->
<template>
    <div id="home">
        <BlogHeader/>
        <ArticleList/>
        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
/* 
    Vue组件化思想
    分解成模块，增加解耦和复用
*/
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import ArticleList from '@/components/ArticleList.vue'

    export default {
        name: 'Home',
        components: { BlogHeader, BlogFooter, ArticleList }
    }
</script>

<!-- css -->
<style>
</style>
