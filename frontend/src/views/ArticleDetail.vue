<!--
    文章详情
-->

<!-- html -->
<template>
    <div id="articledetail">
        <BlogHeader/>
        <div class='global_block'>
            <div class='global_block_content'>
                <br>
                <!-- 文章内容 -->
                <!-- 渲染前 v-if判断数据是否存在 -->
                <div v-if="article !== null" class="grid-container">
                    <div>
                        <!-- 标题 -->
                        <h1 id="title">{{ article.title }}</h1>
                        <!-- 引语 -->
                        <p id="subtitle">
                            本文由 {{ article.author.username }} 发布于 {{ formatted_time(article.created) }}
                            <!-- 若是管理员 添加文章编辑界面 -->
                            <span v-if="isSuperuser">
                                <router-link :to="{ name: 'ArticleEdit', params: { id: article.id }}">
                                    更新/删除
                                </router-link>
                            </span>
                        </p>
                        <!-- 内容 -->
                        <!-- body_html 为后端渲染好的 markdown文本 见文章详情序列化器 -->
                        <!-- 直接转换为html 使用 v-html标注 -->
                        <div v-html="article.body_html" class="article-body"></div>
                    </div>
                    <div>
                        <h3>目录</h3>
                        <!-- 目录 toc_html同理 -->
                        <div v-html="article.toc_html" class="toc"></div>
                    </div>
                </div>
            </div>
        </div>
        <!-- 评论组件 -->
        <Comments :article="article" />
        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import Comments from '@/components/Comments.vue'
    import axios from 'axios'

    export default {
        name: 'ArticleDetail',
        components: { 
            BlogHeader, 
            BlogFooter,
            Comments,
        },
        data:function() {
            return{
                article: null
            }
        },
        computed: {
            // 计算属性 判断是否为管理员
            isSuperuser() {
                return localStorage.getItem('isSuperuser.myblog') === 'true'
            }
        },
        mounted() {
            axios
                // $route.params.id 获取路由中的动态参数 见router/index.js
                // 拼接为 后端对应的文章详情地址 见article/urls.py
                .get('/bg/article/article-detail/' + this.$route.params.id)
                .then(response => (this.article = response.data))
        },
        // methods方法 可在脚本中直接调用 也可在模板中通过标签属性或花括号调用
        methods: { // 标签和创建时间
            formatted_time: function(iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            }
        }
    }
</script>

<!-- css -->
<style scoped>
    /* .grid-container 简单的给文章内容、目录划分了网格区域 */
    .grid-container {
        display: grid;
        grid-template-columns: 3fr 1fr;
    }
    #title {
        text-align: center;
        font-size: x-large;
    }
    #subtitle {
        text-align: center;
        color: gray;
        font-size: small;
    }
</style>
<style>
    /* <style> 标签可以有多个 */
    /*52 文章内容、目录都是从原始 HTML 渲染的，不在 scoped 的管理范围内 */
    .article-body p img {
        max-width: 100%;
        border-radius: 50px;
        box-shadow: gray 0 0 20px;
    }

    .toc ul {
        list-style-type: none;
    }

    .toc a {
        color: gray;
    }
</style>
