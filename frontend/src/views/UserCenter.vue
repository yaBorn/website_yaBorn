<!-- 
    用户中心 页面
-->

<!-- html -->
<template>
    <div id="UC">
        <BlogHeader :welcome-name='name2header'/>
        <!-- :x即双向绑定Vue管理的数据 v-bind:缩写
        目的在更新name后 header欢迎{{name}}同步改变
        HTML大小写不敏感，Vue规定prop命名的 N大写用-n替换
        welcome-name对应header的prop welcomeName -->
        <!-- TODO 简单的方法 -->
        <!-- Header写个refresh更新username为本地localstorage.getitem
        <BlogHeader ref="header"/>
        js使用 that.$refs.header.refresh()调用子组件函数 -->
        <div id="user-center">
            <!-- 用户中心 表单 -->
            <h3>更新信息</h3>
            <form> 
                <div class="form-elem">
                    <span>用户名：</span>
                    <input v-model="username" type="text" placeholder="输入用户名...">
                </div>

                <div class="form-elem">
                    <span>新密码：</span>
                    <input v-model="passWord" type="text" placeholder="输入密码">
                </div>

                <div class="form-elem">
                    <span>再次输入：</span> 
                    <input v-model="passWordTest" type="passWord" placeholder="输入密码">
                </div>

                <!-- 错误提示框 -->
                <div id="grid">
                    <div></div>
                    <div class="form-elem">
                        <button v-on:click.prevent="changeinfo">
                            更新
                        </button>
                    </div>
                    <div class="message">
                        <p v-text="errorMessage"></p>
                    </div>
                </div>
            </form>
        </div>
        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import axios from 'axios'
    import authorization from '@/func/authorization'
    const storage = localStorage

    export default {
        name: 'UserCenter',
        components: {
            BlogHeader, 
            BlogFooter,
        },
        data: function () {
            return {
                username: '',
                passWord: '',
                passWordTest: '',
                errorMessage: '',
                token: '',
                // 更新name后传递给header以更新欢迎词
                name2header: '',
            }
        },
        // 加载用户中心时 检查登录状态
        mounted() {
            console.log('-----UserCenter.vue.mounted')
            this.name2header = storage.getItem('username.myblog')
            this.username = storage.getItem('username.myblog')
            
            // 进行用户验证
            const that = this
            authorization()
                .then(function (response) {
                    // 检查登录状态
                    if( !response[0]) {
                        that.errorMessage = '登录过期，请重新登录'
                        console.log('登录过期，请重新登录')
                        alert('登录过期，请重新登录') // 通知框通知用户                        
                        // TODO 跳转主页面 
                        // this.$router.push({name:'Home'})
                        that.$router.push({name:'Home'})
                        // 若为this，报错Uncaught (in promise) TypeError: Cannot read property '$router' of undefined
                        // 原因同login 129TODO this关键字的作用域问题
                        return
                    }
                })
            console.log('令牌通过')
        },
        methods: {
            // 更新按钮 回调函数
            changeinfo () {
                console.log('-----UserCenter.vue.changeinfo')

                const that = this
                that.errorMessage = '' // 重置信息框
                // console.log('输入用户名：',that.username)
                // console.log('输入password:',that.passWord)
                // console.log('输入passwordtst:',that.passWordTest)

                // TODO:更多的格式化
                // 均空 不更新
                if(that.passWord.length == 0
                    && that.passWordTest.length == 0
                    && that.username == null) {
                    console.log('输入为空')
                    that.errorMessage = '请输入内容'
                    return
                }
                // 验证二次输入
                if(that.passWord !== that.passWordTest) {
                    console.log('密码不一致')
                    that.errorMessage = '密码不一致，请重新输入'
                    return
                }
                // 格式规定 密码长度
                if(that.passWord.length > 0 && that.passWord.length < 2) {
                    console.log('输入格式错误')
                    that.errorMessage = '密码需大于2位'
                    return
                }

                // 调用 func-authorization() 进行用户验证
                // 旧方法见 git提交历史 2021.6.8 16：03 用户登录 Login.vue-methods
                authorization()
                    .then(function (response) {
                        console.log('--UserCenter.vue.then')
                        // 检查登录状态
                        if( !response[0]) {
                            that.errorMessage = '登录过期，请重新登录'
                            console.log('登录过期，请重新登录')
                            return
                        }
                        // 获取填写的数据
                        let data = {}
                        if(that.username !=='') { // 判空 空则不更新
                            data.username = that.username
                        }
                        if(that.passWord !== '') {
                            data.password = that.passWord
                        }

                        // 用于 axios发送请求
                        that.token = storage.getItem('access.myblog') // 获取令牌
                        const oldUsername = storage.getItem('username.myblog') // 旧 username用于 axios发送数据
                        console.log('token:', that.token)
                        console.log('oldname:', oldUsername)
                        console.log('changeData:', data)

                        // 将令牌和填写的数据发送到 axios 更新数据
                        axios
                            .patch( 
                                // TODO:此处报错 转发到了 8080:user/bg/user 404
                                // 第一个user为该页面地址 与路由 index同步
                                // 改为 post也一样
                                // 与正常运行的 Login.vue.sigin.axios.post比较
                                // sigin的 post地址为 8080:bg/token 无路由前缀
                                // 解决 
                                //      'bg/uer/'则会添加该页面的路径 变成 'user/bg/user'
                                //      '/bg/user/'则为 '/bg/user'
                                '/bg/user/' + oldUsername + '/', 
                                data, 
                                {
                                    headers: {Authorization: 'Bearer '+ that.token}
                                } // token验证字段 头对象
                                // TODO:报错2 PATCH http://127.0.0.1:8080/bg/user/c1/ 401 (Unauthorized)
                                // 输入原账号密码仍 Request failed with status code 401 
                                // 猜测token身份验证错误
                                // 登录时获取的response.data.access和此处headers相同
                                // 解决 'Bearer' -> 'Bearer '....patch过去的命令 Bearer没带空格
                            )
                            .then(function (response) {
                                // 更改本地存放的数据
                                const name = response.data.username
                                storage.setItem('username.myblog', name)
                                // 跳转到更改用户名后对应的路由界面
                                that.$router.push({
                                    name:'UserCenter', 
                                    params:{username:name}
                                })
                                // TODO：跳转后发现问题，路径/表单等数据 name已更新成 新name
                                // 但 vue-header组件上 欢迎，{{username}} 未更新
                                // 原因 Vue$router跳转同一个页面时，只渲染发生变化的组件
                                // 页眉_默认参数 name=''，通过生命周期钩子 mounted()，验证用户后更新 name
                                // 则此处 axios更新 name资料后 跳转 Vue认为 header组件未改变
                                // Vue判定组件改变的依据在 Vue管理下的数据变化
                                // 而不会判定本地 localStorage变化
                                // 通过 props 组件间参数传递实现
                                that.name2header = name
                            })
                            .catch(function (error) {
                                console.log(error.message)
                            })
                    })
            }
        },
    }
</script>

<!-- css -->
<style scoped>
    #user-center {
        text-align: center;
    }
    .form-elem {
        padding: 10px;
    }
    #grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
    }
    .message {
        text-align: left;
        font-size: 10px;
        color: rgba(251, 14, 14, 0.931);
    }
    input {
        height: 25px;
        padding-left: 10px;
    }
    button {
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: gray;
        color: whitesmoke;
        border-radius: 5px;
        width: 60px;
    }
</style>