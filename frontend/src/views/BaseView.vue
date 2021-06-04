<!-- 初试空页 -->

<!-- html -->
<template>
    <div id="name">     <!--  此处添加id  -->
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
        name: '',   // name
        components: {BlogHeader, BlogFooter}
    }
</script>

<!-- css -->
<style>
/*  
    #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 40px;
        margin-right: 40px;
    }
*/
</style>