<!-- 组件 文章列表 -->

<!---
    v-属性 即 Vue模板语法标记
    v-for 循环可迭代元素
    info.results 对应后端数据的 json 结构。请对照后端接口进行理解
    v-bind:key 给定了循环中每个元素的主键,方便 Vue 渲染时对元素进行识别
-->

<!-- html -->
<template>
<div id="ArticleList">
    <!-- 文章列表 -->
    <div v-for="article in info.results" v-bind:key="article.url" id="articles">
        <!-- 标签 -->
        <div>
            <span
                    v-for="tag in article.tags"
                    v-bind:key="tag"
                    class="tag"
            >
                {{ tag }}
            </span>
        </div>

        <!-- 文章标题 -->
        <div class="article-title">
            {{ article.title }}
        </div>

        <!-- 创建时间 -->
        <div>
            {{ formatted_time(article.created) }}
        </div>
    </div>
</div>
</template>

<!-- js -->
<script>
    // Vue 实例被创建时, 将 data 对象返回的所有属性加入到 Vue 的响应式系统
    // 当这些属性的值发生改变时，视图将会产生“响应”，即自动更新为新的值
    import axios from 'axios';

    export default {
        name: 'ArticleList',
        data: function () {
            return {
                info: ''        // data info 属性初始化时赋值空字符串
            }
        },

        mounted() {        // Vue 加载完成后,调用生命周期钩子 mounted() 方法
            // 通过 axios 向 Django 后端获取到文章列表数据并赋值给 info 后
            // 页面中关联的部分也会立即随之更新，而不用手动去操作页面元素
            axios
                .get('/bg/article/article-list/')
                .then(response => (this.info = response.data))
        },

        methods: {  // 标签和创建时间
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            }
        }
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
/*  
    规定页面各元素的大小、位置、颜色等样式
    #name 样式挂载的指定页面 
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
    .tag {
        padding: 2px 5px 2px 5px;
        margin: 5px 5px 5px 0;
        font-family: Georgia, Arial, sans-serif;
        font-size: small;
        background-color: #4e4e4e;
        color: whitesmoke;
        border-radius: 5px;
    }
</style>
