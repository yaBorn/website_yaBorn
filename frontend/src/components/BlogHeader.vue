<!-- 
    组件 页眉 
    TODO:设置用户登出 OK
    TODO: 每当页面刷新时，页眉都会向后台发送请求确认登录状态。是否可以利用缓存，减轻后端压力？
-->

<!-- html -->
<template>
    <div>
        <!-- 页眉 -->
        <div id="header">
            <div class='content'>
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

                <!-- 用户注册 -->
                <div class="login">
                    <!-- 已登录下拉框 详见css -->
                    <div class="cif" v-if="hasLogin">
                        <div class="global_dropdown">
                            <!-- <p v-text="hasLogin"></p> -->
                            <div class="global_btn btn__secondary">
                                <p> 欢迎，{{com_name}} </p>
                            </div>
                            <!-- 下拉框内容 -->
                            <div class="global_dropdown-content">
                                <!-- 用户中心 -->
                                <router-link :to="{name:'UserCenter',params:{username:username}}">
                                    用户中心
                                </router-link>
                                <!-- 对管理员用户显示文章发表 -->
                                <router-link :to="{name: 'ArticleCreate'}" v-if="com_super">
                                    发表文章
                                </router-link>
                                <!-- 退出 -->
                                <router-link v-on:click.prevent="logout()" :to="{name:'Home'}">
                                    退出
                                </router-link>
                                <!-- <router-link @click='logout()'>
                                    退出
                                </router-link> -->
                            </div>
                        </div>  
                    </div>
                    <div class="cif" v-else>
                        <!-- 登录注册链接 -->
                        <!-- <router-link to="/login" class="login-link"> -->
                        <router-link :to="{name:'Login'}" class="global_btn btn__primary">
                            <p> 登录/注册 </p>
                        </router-link>
                    </div>
                </div>
            </div>
            <!-- 底部下划线 -->
            <hr>
        </div>
        <!-- 网页头固定后 后面页面内容后移 -->
        <br><br><br><br><br><br><br><br>
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
                // 是否为管理员 直接从缓冲中解析json
                isSuperuser: JSON.parse(localStorage.getItem('isSuperuser.myblog')),
            }
        },
        components:{
            SearchBox,
            PointRun,
        },
        props:['welcomeName','isSuper'], // 更新页面传递过来的prop参数
        // 计算属性
        // 基于响应式依赖进行缓存，当相关响应式依赖发生改变时才会重新求值
        // 即只要参数未改变 重复访问时直接返回之前的结果
        // computed默认不接受参数 且不可改变Vue管理数据 否则报错
        computed:{
            com_name() {
                // 判断用户中心页面是否传递来 name更新参数
                // 根据判断 来显示Vue的 {{name}}内容
                console.log('-----header.computed：',this.isSuper)
                return (this.welcomeName !== undefined) ? this.welcomeName : this.username
            },
            com_super() {
                console.log('-----header.computed：',this.isSuper)
                return (this.isSuper !== undefined) ? this.isSuper : this.isSuperuser
            }
        },
        methods: {
            // 刷新界面 根据缓存刷新数值
            // 失败 失败分支迁出 2020.6.13.16：22
            // refresh () {
            //     // 见UserCenter.vue前面的TODO
            //     // 解决 
            //     // 1. 用户中心修改username header未刷新 (TODO 未使用此方法)
            //     // 2. 管理员登录 下拉框发表文章未出现 需要刷新才行
            //     // 父组件 html 组件header加上 ref="header"
            //     // 父组件 js 使用 that.$refs.header.refresh()进行刷新
            //     const that = this
            //     that.isSuperuser = JSON.parse(localStorage.getItem('isSuperuser.myblog'))
            // },
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
        },
        // 模板渲染 html后调用 二次操作 html的 dom结点
        mounted() {
            // 登录管理员用户 login组件通信
            // 用户验证验证代码
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
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
    #header {
        text-align: center;
        margin-top: 0px;
        /* background: whitesmoke; */
        /* 固定顶端位置 并固定宽度100% */
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        background: var(--hfcolor);
    }
    .content {
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
    /* 重设按钮样式 */
    .global_btn {
        border: 2px solid rgba(0, 0, 0, 0);
        /* position: relative;
        left:90%; */
        border-radius: 1rem;
        width: 6rem;
        height: 3rem;
        display: inline-block; /* 不换行 */
        text-align: center;
    }
    .global_btn p {
        font-size: 1rem;
        position: relative;
        top: -3px;
    } 
    .btn__secondary {
        height: 3rem;
        border: 2px solid var(--dark);
        transition: 0.4s ease; 
        /* position: relative;
        left: 0%; */
    }
    .btn__secondary:hover {
        /* 鼠标放上去后改变 颜色与阴影 */
        border: 2px solid var(--color2);
        color: black;
        box-shadow: 
            inset 0.2rem 0.2rem 0.5rem var(--belowShadow), 
            inset -0.2rem -0.2rem 0.5rem var(--topShadow);
    }
</style>
