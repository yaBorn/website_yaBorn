<!-- 
    创建文章 页面
-->

<!-- html -->
<template>
    <div id='articlecreat'>
        <BlogHeader/>

        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
import BlogHeader from '@/components/BlogHeader.vue'
import BlogFooter from '@/components/BlogFooter.vue'

export default {
    name: 'ArticleCreate',
    components: {
        BlogHeader, 
        BlogFooter,
    }
}
</script>