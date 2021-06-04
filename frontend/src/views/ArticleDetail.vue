<!-- 文章详情页 -->

<!-- html -->
<template>
    <div id="ArticleDetail">
        <BlogHeader/>
        <!--  此处添加内容  -->
        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'

    export default {
        name: 'ArticleDetail',
        components: {BlogHeader, BlogFooter}
    }
</script>

<!-- css -->
<style>
</style>