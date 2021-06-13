<!-- 
    组件 页眉 
    TODO:设置用户登出 OK
    TODO: 每当页面刷新时，页眉都会向后台发送请求确认登录状态。是否可以利用缓存，减轻后端压力？
-->

<!-- html -->
<template>
    <!-- 页眉 -->
    <div id="header">
        <!-- 布局 -->
        <div class="grid">
            <!-- 搜索框 -->
            <SearchBox/>

            <!-- 标题 -->
            <router-link :to="{name:'Home'}"> <!-- 点击跳转回 home -->
                <div class="headertex">
                    <h1>yaBorn Blog</h1>
                </div>
            </router-link>
            <!-- grid布局 搜多-标题-空 -->
            <PointRun/>
        </div>
        <!-- 底部下划线 -->
        <hr>

        <!-- 用户注册 -->
        <div class="login">
            <!-- 已登录下拉框 详见css -->
            <div v-if="hasLogin">
                <div class="dropdown">
                    <!-- <p v-text="hasLogin"></p> -->
                    <button class="dropbtn">
                        欢迎，{{name}}
                    </button>
                    <!-- 下拉框内容 -->
                    <div class="dropdown-content">
                        <router-link :to="{name:'UserCenter',params:{username:username}}">
                            用户中心
                        </router-link>
                        <!-- <router-link @click='logout()'>
                            退出
                        </router-link> -->
                        <router-link v-on:click.prevent="logout()" :to="{name:'Home'}">
                            退出
                        </router-link>
                    </div>
                </div>  
            </div>
            <div v-else>
                <!-- 登录注册链接 -->
                <!-- <router-link to="/login" class="login-link"> -->
                <router-link :to="{name:'Login'}" class="login-link">
                    登录/注册
                </router-link>
            </div>
        </div>
    </div>
</template>

<!-- js -->
<script>
    import SearchBox from '@/components/SearchBox.vue'
    import authorization from '@/func/authorization'
    import PointRun from '@/components//others/PointRun.vue'

    export default {
        name: 'BlogHeader',
        data: function () {
            return {
                username: '',
                hasLogin: false,
            }
        },
        components:{
            SearchBox,
            PointRun,
        },
        props:['welcomeName'], // 更新页面传递过来的prop参数
        // 计算属性
        // 基于响应式依赖进行缓存，当相关响应式依赖发生改变时才会重新求值
        // 即只要参数未改变 重复访问时直接返回之前的结果
        // computed默认不接受参数 且不可改变Vue管理数据 否则报错
        computed:{
            name() {
                // 判断用户中心页面是否传递来 name更新参数
                // 根据判断 来显示Vue的 {{name}}内容
                return (this.welcomeName !== undefined) ? this.welcomeName : this.username
            }
        },
        // 模板渲染 html后调用 二次操作 html的 dom结点
        mounted() {
            // 整合验证代码
            authorization()
                .then(
                    (data) => [this.hasLogin, this.username] = data
                )
            /*  // 未整合 func用户验证的代码
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
                            storage.clear()
                            that.hasLogin = false
                        })
                }
                // token过期 失效
                else {
                    storage.clear()
                    that.hasLogin = false
                    console.log('令牌过期，失效，清空token，hasLogin:', that.hasLogin)
                }
            */
        },
        methods: {
        // 用户登出按钮回调
            logout () {
                console.log('-----Header.vue.logout')
                const storage = localStorage
                storage.clear()
                this.hasLogin = false
                console.log('用户登出，清空token')
                // 刷新页面 不刷新也可 router-link有跳转
                // window.location.reload() 
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
        grid-template-columns: 1fr 5fr 1fr; /* grid布局 1:4:1 空白-标题-搜索框 */
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

<!-- 拉按钮样式 -->
<style scoped>
    /* 来源: https://www.runoob.com/css/css-dropdowns.html */
    .dropbtn {
        background-color: rgb(136, 136, 136);
        color: white;
        padding: 8px 8px 30px 8px ;
        font-size: 16px;
        border: none;
        cursor: pointer;
        height: 16px;
        border-radius: 5px;
    }
    /* 容器 <div> - 需要定位下拉内容 */
    .dropdown {
        position: relative;
        display: inline-block;
    }
    /* 下拉内容 (默认隐藏) */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 120px;
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    /* 下拉菜单的链接 */
    .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }
    /* 鼠标移上去后修改下拉菜单链接颜色 */
    .dropdown-content a:hover {
        background-color: #f1f1f1
    }
    /* 在鼠标移上去后显示下拉菜单 */
    .dropdown:hover .dropdown-content {
        display: block;
    }
    /* 当下拉内容显示后修改下拉按钮的背景颜色 */
    .dropdown:hover .dropbtn {
        background-color: rgb(190, 190, 190);
    }
</style>