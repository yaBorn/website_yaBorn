<!-- 首页 文章列表 -->

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
    import BlogHeader from '../components/my/BlogHeader.vue'
    import BlogFooter from '../components/my/BlogFooter.vue'
    import ArticleList from '../components/my/ArticleList.vue'

    export default {
        name: 'Home',
        components: { BlogHeader, BlogFooter, ArticleList }
    }
</script>

<!-- css -->
<style>
</style>
