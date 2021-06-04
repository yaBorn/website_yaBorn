
<!-- html -->
<template>
    <div id="detail">
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
    import BlogHeader from '@/components/my/BlogHeader.vue'
    import BlogFooter from '@/components/my/BlogFooter.vue'
    import ArticleList from '@/components/my/ArticleList.vue'

    export default {
        name: 'ArticleDetail',
        components: { BlogHeader, BlogFooter, ArticleList }
    }
</script>

<!-- css -->
<style>
</style>
