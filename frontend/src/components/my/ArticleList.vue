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
            <!-- <div class="article-title"> -->
                <!-- {{ article.title }} -->
            <!-- </div> -->
            <router-link
                :to="{ name: 'ArticleDetail', params: { id: article.id }}"
                class="article-title"
            >
                {{ article.title }}
            </router-link>
            <!-- 调用vue-router
                :to指定跳转位置，动态参数id为后端对应序列化器 aid接口 
                vue中，属性前的 :表啊是属性绑定，为v-bind:缩写
                TODO: 跳转失败 id为undefined 后端序列化器接口id字段没有暴露
            -->

            <!-- 创建时间 -->
            <div>
                {{ formatted_time(article.created) }}
            </div>
        </div>
        
        <!-- 翻页 -->
        <div id='pageinator'>
            <!-- 前页 -->
            <span v-if="is_page_exists('previous')">
                <router-link :to="{ name:'Home', query:{page:get_page_param('previous')} }">
                    Prew
                </router-link>
            </span>
            <!-- 当前页 -->
            <span class="current-page">
                {{ get_page_param('current') }}
            </span>
            <!-- 后页 -->
            <span v-if="is_page_exists('next')">
                <router-link :to="{ name:'Home', query:{page:get_page_param('next')} }">
                    Next
                </router-link>    
            </span>           
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
            // 获取文章列表数据
            get_article_data:function () {
                let url = '/bg/article/article-list/'
                const page = Number(this.$route.query.page)
                if (!isNaN(page) && (page !== 0)) { // 默认首页，当页码不存在返回home
                    url = url + '/?page=' + page
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
    #pageinator {
        text-align: center;
        padding-top: 50px;
    }
    a {
        color: black;
    }
    .current-page {
        font-size: x-large;
        font-weight: bold;
        padding-left: 10px;
        padding-right: 10px;
    }
</style>
