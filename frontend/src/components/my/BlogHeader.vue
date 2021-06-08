<!-- 
    组件 页眉 
        Home.vue
    TODO:设置用户登出
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
            <div></div>
        </div>
        <!-- 底部下划线 -->
        <hr>

        <!-- 用户注册 -->
        <div class="login">
            <!-- <p v-text="hasLogin"></p> -->
            <div v-if="hasLogin">
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
    import axios from 'axios'
    import SearchBox from '@/components/my/SearchBox.vue'

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
