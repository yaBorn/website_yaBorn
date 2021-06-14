<!-- 
    组件 文章列表 
        Home.vue
-->

<!---
    v-属性 即 Vue模板语法标记
    v-for 循环可迭代元素
    info.results 对应后端数据的 json 结构。请对照后端接口进行理解
    v-bind:key 给定了循环中每个元素的主键,方便 Vue 渲染时对元素进行识别
-->

<!-- html -->
<template>
    <div id="articlelist">
        <!-- 文章列表 -->
        <div v-for="article in info.results" v-bind:key="article.url" id="articles">
            <br> <!-- 每个区块 间隔一行 -->
            <div class='global_block'>
                <div class='global_block_content'>
                    <br>
                    <div>
                        <!-- 分类 -->
                        <span v-if="article.category !== null" class="category">
                            {{article.category.title}}
                        </span>
                    
                        <!-- 标签 -->
                        <span v-for="tag in article.tags" v-bind:key="tag" class="tag">
                            {{ tag }}
                        </span>
                    </div>

                    <!-- 为标题图位置布局 设置的网格层 -->
                    <div class="grid" :style="gridStyle(article)">
                        <!-- 标题图 -->
                        <div class="image-container">
                            <img :src="imageIfExists(article)" alt="" class="image">
                        </div>

                        <div class="text">
                            <!-- 文章标题 -->
                            <router-link
                                :to="{ name: 'ArticleDetail', params: { id: article.id }}"
                                class="article-title">
                                {{ article.title }}
                            </router-link>

                            <!-- 内容摘要 -->
                            <br><br>
                            <router-link
                                :to="{ name: 'ArticleDetail', params: { id: article.id }}"
                                class="article-body">
                                {{ article.body.slice(0,300) + ' ...' }}
                            </router-link>
                        </div>
                        <!-- 调用vue-router
                            :to指定跳转位置，动态参数id为后端对应序列化器 aid接口 
                            vue中，属性前的 :表啊是属性绑定，为v-bind:缩写
                            TODO: 跳转失败 id为undefined 后端序列化器接口id字段没有暴露
                        -->

                        <!-- 创建时间 -->
                        <div>
                            <br> {{ formatted_time(article.created) }}
                        </div>
                    </div>
                </div>
                <br>
            </div>
        </div>
        
        <!-- 翻页 -->
        <!-- 每页项目数量 由后端传输json内容决定  setting-->
        <div class='pageinator'>
            <div class='d'></div>
            <!-- 前页 -->
            <div v-if="is_page_exists('previous')">
                <!-- <router-link :to="{ name:'Home', query:{page:get_page_param('previous')} }"> -->
                <router-link :to="get_path('previous')" class="global_btn btn__secondary prew">
                    <p>Prew</p> 
                </router-link>
            </div>
            
            <!-- 当前页 -->
            <div class="current-page">
                {{ get_page_param('current') }}
            </div>

            <!-- 后页 -->
            <div v-if="is_page_exists('next')">
                <!-- <router-link :to="{ name:'Home', query:{page:get_page_param('next')} }"> -->   
                <router-link :to="get_path('next')" class="global_btn btn__secondary next">
                    <p>Next</p> 
                </router-link> 
            </div>  
            <div class='d'></div>
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
                info: '' // data info 属性初始化时赋值空字符串
            }
        },
        // Vue 加载完成 调用生命周期钩子 mounted() 方法
        mounted() {
            this.get_article_data() // 见方法
        },
        // methods方法 可在脚本中直接调用 也可在模板中通过标签属性或花括号调用
        methods: {
            // 显示文章标题图
            imageIfExists(article) {
                if(article.photo) {
                    return article.photo.content
                }
            },
            // 若文章带标题图 改写布局
            gridStyle(article) {
                if(article.photo) {
                    return {
                        display: 'grid',
                        gridTemplateColumns: '1fr 4fr',
                    }
                }
            },
            // 获取文章列表数据
            get_article_data:function () {
                let url = '/bg/article/article-list/'
                // 翻页迭代搜索功能 获取搜索返回的URL对象
                // 原生append()不判断值存在 会出现/?page=undefined 错误
                // myAppendIfExists 排除错误路径 为扩展的对象功能 见main.js
                let params = new URLSearchParams();
                params.myAppendIfExists('page', this.$route.query.page);
                params.myAppendIfExists('search', this.$route.query.search);
                
                const paramsString = params.toString()
                if (paramsString.charAt(0) !== '') { // 默认首页，当页码不存在返回home
                    url = url + '/?' + paramsString
                }
                // 通过 axios 向 Django 后端获取到文章列表数据并赋值给 info
                axios
                    .get(url)
                    .then(response => (this.info = response.data))
            },
            // 标签和创建时间
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            },
            // 判断页面是否存在
            is_page_exists(direction) {
                if(direction === 'next') {
                    return this.info.next !== null
                }
                return this.info.previous !== null
            },
            // 获取页码
            get_page_param:function(direction) {
                try { // 规避意外 TODO:网速缓慢，info还未获取到数据
                    let url_string
                    switch (direction) { // 根据翻页方向返回URL对象页码参数
                        case 'next':
                            url_string = this.info.next
                            break
                        case 'previous':
                            url_string = this.info.previous
                            break
                        default:
                            return this.$route.query.page
                    }
                    const url = new URL(url_string)
                    return url.searchParams.get('page')
                }
                catch (err) {
                    // TODO:添加报错信息提示
                    return
                }
            },
            // 搜索功能迭代 获取页码
            get_path:function(direction) {
                // <router-link>翻页时读取 page值，但对于搜索search则获取不到正确路径
                // 以此迭代 get_article_data()
                let url = '';
                try {
                    switch (direction) {
                        case 'next':
                            if (this.info.next !== undefined) {
                                url += (new URL(this.info.next)).search
                            }
                            break;
                        case 'previous':
                            if (this.info.previous !== undefined) {
                                url += (new URL(this.info.previous)).search
                            }
                            break;
                    }
                }
                catch { 
                    return url 
                }
                return url
            }
        },
        // watch监听路由变化 用于翻页
        watch:{
            // 监听Vue数据，改变时执行相应方法
            $route() { // vue路由对象
                this.get_article_data() // 路由改变，即页数改变，更新
                // 参数page变化对于 vue-router而言不算路径变化，因此不会触发mouted()，而是通过监听执行
            }
        }
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>  
    #articles {
        padding: 10px;
    }  
    /* 翻页 */
    .pageinator {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        /* border: 2px solid var(--dark); */
        text-align: center;
        padding-top: 50px;
    }
    .prew {
        /* 右移动一半 */
        position: relative;
        left: var(--width2);
    }
    .current-page {
        font-size: x-large;
        font-weight: bold;
        padding-left: 10px;
        padding-right: 10px;
    }
    .global_btn {
        /* top: 30px; */
        border-radius: 1.6rem;
        width: 6rem;
        height: 3rem;

        font-size: x-large;
        font-weight: bold;
        padding-left: 10px;
        padding-right: 10px;
    }
    /* .d{
        border: 1px solid black
    } */

    /* 信息块 */
    /* 分类 */
    .category {
        border-radius: 4rem;
        /* 内外边框 */
        padding: 8px 12px 8px 12px;
        margin: 0px 15px 0px -20px;
        /* 颜色 字体 */
        font-family: Georgia, Arial, sans-serif;
        font-size: small;
        background-color: var(--color);
        color: var(--tex);
        /* 阴影 动画速率 */
        transition: 0.2s ease;
        box-shadow: 
            inset 0.2rem 0.2rem 1rem var(--hightLight),
            inset -0.2rem -0.2rem 1rem var(--dark), 
            0.3rem 0.3rem 0.6rem var(--belowShadow), 
            -0.2rem -0.2rem 0.5rem var(--topShadow);
    }
    .category:hover {
        /* 移动动画 变换阴影 */
        color: var(--texch);
        box-shadow: 
            inset 0.2rem 0.2rem 1rem var(--dark), 
            inset -0.2rem -0.2rem 1rem var(--hightLight),
            0.3rem 0.3rem 0.6rem var(--topShadow), 
            -0.2rem -0.2rem 0.5rem var(--belowShadow);
    }
    /* 标签 */
    .tag {
        border-radius: 5px;
        /* 内外边框 */
        padding: 2px 5px 2px 5px;
        margin: 5px 5px 5px 0;
        /* 颜色 字体 */
        font-family: Georgia, Arial, sans-serif;
        font-size: small;
        background-color: var(--gray);
        color: var(--tex);
        /* 阴影 动画速率 */
        transition: 0.2s ease;
        box-shadow: 
            0.3rem 0.3rem 0.6rem var(--belowShadow), 
            -0.2rem -0.2rem 0.5rem var(--topShadow);
    }
    .tag:hover {
        /* 移动动画 变换阴影 */
        color: var(--black);
        background-color: var(--gray2);
        box-shadow: 
            0.3rem 0.3rem 0.6rem var(--topShadow), 
            -0.2rem -0.2rem 0.5rem var(--belowShadow);
    }

    /* 文章 */
    .grid {
        /* 边距 */
        padding-top: 30px;
        padding-bottom: 10px;
    }
    /* 标题图 */
    .image-container {
        width: 200px;
    }
    .image {
        width: 180px;
        border-radius: 10px;
        box-shadow: darkslategrey 0 0 12px;
    }
    .text {
        /* 上右下左 内边距 外边距*/
        padding:0px 0px 10px 10px;
        margin: 0px 100px 0px 0px;
        /* TODO：bug 窗口过窄时 字符信息超出区块 且和标题形式有关 */
        border: 2px solid var(--dark);
    }
    .article-title {
        /* 字体 */
        font-size: x-large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
    .article-body {
        font-size: medium;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }

    a {
        color: black;
    }
</style>
