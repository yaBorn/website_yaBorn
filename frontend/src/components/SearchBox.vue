<!--
    搜索框 组件
-->

<!-- html -->
<template>
    <!-- 搜索框 -->
    <div class="search">
        <form>
            <!-- v-model为数据绑定 input数据和 js的searchText绑定在 共享数据内容 -->
            <input v-model="searchText" type="text" placeholder="输入内容...">
            <!-- v-on:clic为按键点击事件，触发searchArticles() -->
            <!-- prevent阻止按钮初始表单提交 -->
            <button v-on:click.prevent="searchArticles">
            </button>
        </form>
    </div>
</template>

<!-- js -->
<script>
    export default {
        name: 'SearchBox',
        data: function () {
            return {
                searchText: '',
            }
        },
        methods: {
            // 搜索回调函数
            searchArticles() {
                // TODO:搜索范围迭代 搜索标题/标签关键词
                // 并且在更新列表 list高亮该关键词
                // 点击button触发回调，将searchText作为参数进行路径跳转
                const text = this.searchText.trim();
                if(text.charAt(0) !== '') {
                    // 和 <router-link>类似，为脚本中的动态跳转
                    // $route路径对象 $router路由器对象
                    this.$router.push({name:'Home', query:{ search:text}})
                }
            }
        }
    }
</script>

<!-- css -->
<style scoped>
    * {
        box-sizing: border-box;
    }
    form {
        position: relative;
        width: 200px;
        margin: 0 auto;
    }
    input, button {
        border: none;
        outline: none;
    }
    input {
        width: 100%;
        height: 35px;
        padding-left: 13px;
        padding-right: 46px;
    }
    button {
        height: 35px;
        width: 35px;
        cursor: pointer;
        position: absolute;
    }
    .search input {
        border: 2px solid rgba(78, 79, 97, 0.678);
        border-radius: 5px;
        background: transparent;
        top: 0;
        right: 0;
    }
    .search button {
        background: rgba(78, 79, 97, 0.678);
        border-radius: 0 5px 5px 0;
        width: 45px;
        top: 0;
        right: 0;
    }
    .search button:before {
        content: "搜索";
        font-size: 13px;
        color: rgba(255, 255, 255, 0.904);
    }
</style>