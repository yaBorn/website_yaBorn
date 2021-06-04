<!--
    文章详情
-->

<!-- html -->
<template>
    <div id="articledetail">
        <BlogHeader/>
        <!-- 留空 -->
        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
    import BlogHeader from '@/components/my/BlogHeader.vue'
    import BlogFooter from '@/components/my/BlogFooter.vue'

    export default {
        name: 'ArticleDetail',
        components: { BlogHeader, BlogFooter}
    }
</script>

<!-- css -->
<style>
</style>
