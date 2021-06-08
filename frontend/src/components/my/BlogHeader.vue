<!-- 
    组件 页眉 
        Home.vue
-->

<!-- html -->
<template>
    <!-- 页眉 -->
    <div id="header">
        <!-- 布局 -->
        <div class="grid">
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
            <!-- 标题 -->
            <router-link :to="{name:'Home'}"> <!-- 点击跳转回 home -->
                <div class="headertex">
                    <h1>yaBorn Blog</h1>
                </div>
            </router-link>
            <!-- grid布局 搜多-标题-空 -->
            <div></div>
        </div>
        <!-- 底部下划线 -->
        <hr>
        <!-- 用户注册 -->
        <div class="login">
            <p v-text="hasLogin"></p>
            <!-- TODO:这里 hasLogin为 true但 v-if仍跳过了 -->
            <div v-if="haslogin"> <!-- 判断是否登录 -->
                <!-- 已登录界面 -->
                欢迎，{{username}}
            </div>
            <div v-else>
                <!-- 登录注册链接 -->
                <router-link to="/login" class="login-link">
                    登录/注册
                </router-link>
            </div>
        </div>
    </div>
</template>

<!-- js -->
<script>
import axios from 'axios';

    export default {
        name: 'BlogHeader',
        data: function () {
            return {
                searchText: '',
                username: '',
                hasLogin: false,
            }
        },
        methods: {
            searchArticles() {
                // 点击button触发回调，将searchText作为参数进行路径跳转
                const text = this.searchText.trim();
                if(text.charAt(0) !== '') {
                    // 和 <router-link>类似，为脚本中的动态跳转
                    // $route路径对象 $router路由器对象
                    this.$router.push({name:'Home', query:{ search:text}})
                }
            }
        },
        // 模板渲染 html后调用 二次操作 html的 dom结点
        mounted() {
            const that = this
            const storage = localStorage // login中获取的令牌数据
            // 和 login-setItem名称相同
            const expiredTime = Number(storage.getItem('expiredTime.myblog')) // 过期时间
            const current = (new Date()).getTime() // 当前时间
            const refreshToken = storage.getItem('refresh.myblog') // 刷新
            that.username = storage.getItem('username.myblog') // 账号名称
            console.log('-----header.vue')
            console.log('当前时间:',current)
            console.log('过期时间:',expiredTime)
            console.log('账户：', that.username)


            // token未过期
            if (expiredTime > current) {
                that.hasLogin = true
                console.log('令牌未过期，hasLogin：', that.hasLogin)
            }
            // token过期 但在可更新时间内
            else if(refreshToken !== null){
                // 重新申请token
                console.log('令牌过期，重新申请')
                axios
                    .post('bg/token/refresh/', {
                        refresh: refreshToken
                    })
                    .then(function (response) {
                            // 刷新token
                            const expiredTime = Date.parse(response.headers.date) + 60000;
                            storage.setItem('access.myblog', response.data.access)
                            storage.setItem('expiredTime.myblog', expiredTime)
                            storage.removeItem('refresh.myblog')
                            that.hasLogin = true
                    })
                    .catch(function () {
                        // .clear() 清空当前域名下所有的值
                        storage.clear();
                        that.hasLogin = false;
                    })
            }
            // token过期 失效
            else {
                storage.clear();
                that.hasLogin = false;
                console.log('令牌过期，失效，清空token，hasLogin:', that.hasLogin)
            }
        }
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
    #header {
        text-align: center;
        margin-top: 20px;
    }
    .grid { 
        display: grid;
        grid-template-columns: 1fr 8fr 1fr; /* grid布局 1:4:1 空白-标题-搜索框 */
    }
    .search {
        padding-top: 22px;
    }
    .headertex {
        text-decoration: none;
        text-align: center;
        margin-top: 20px;
        color: black;
    }
    .login {
        text-align: right;
        padding-right: 5px;
    }
    .login-link {
        color:black;
    }
</style>
<!-- 搜索框 css 样式 -->
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
