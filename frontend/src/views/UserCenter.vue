<!-- 
    用户中心 页面
-->

<!-- html -->
<template>
    <div id="UC">
        <BlogHeader/>
        <div id="user-center">
            <!-- 用户中心 表单 -->
            <h3>更新信息</h3>
            <form> 
                <div class="form-elem">
                    <span>用户名：</span>
                    <input v-model="userName" type="text" placeholder="输入用户名...">
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
                userName: '',
                passWord: '',
                passWordTest: '',
                errorMessage: '',
                token: '',
            }
        },
        // 加载用户中心时 检查登录状态
        mounted() {
            console.log('-----UserCenter.vue.mounted')
            this.userName = storage.getItem('userName.myblog')
            
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
                // console.log('输入用户名：',that.userName)
                // console.log('输入password:',that.passWord)
                // console.log('输入passwordtst:',that.passWordTest)

                // TODO:更多的格式化
                // 均空 不更新
                if(that.passWord.length == 0
                    && that.passWordTest.length == 0
                    && that.userName == null) {
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
                if(that.passWord.length > 0 && that.passWord.length < 3) {
                    console.log('输入格式错误')
                    that.errorMessage = '密码需大于3位'
                    return
                }
                axios
                    .patch( 
                        // TODO:此处报错 转发到了 8080:user/bg/user 404
                        // 第一个user为该页面地址 与路由 index同步
                        // 改为 post也一样
                        // 与正常运行的 Login.vue.sigin.axios.post比较
                        // sigin的 post地址为 8080:bg/token 无路由前缀
                        'bg/user/' + this.userName + '/', 
                        {
                            username: this.userName,
                            password: this.passWord,
                        }, 
                        {headers:{Authorization:'Bearer'+that.token}} // token验证字段 头对象
                    )

                /* 调用 func-authorization() 进行用户验证
                    旧方法见 git提交历史 2021.6.8 16：03 用户登录 Login.vue-methods
                */
                authorization()
                    .then(function (response) {
                        console.log('--UserCenter.vue.then')
                        // 检查登录状态
                        if( !response[0]) {
                            that.errorMessage = '登录过期，请重新登录'
                            console.log('登录过期，请重新登录')
                            return
                        }

                        // 用于 axios
                        that.token = storage.getItem('access.myblog') // 获取令牌
                        const oldUserName = storage.getItem('username.myblog') // 旧 username用于 axios发送数据
                        // 获取填写的数据
                        let data = {}
                        if(that.userName !=='') { // 判空 空则不更新
                            data.username = that.userName
                        }
                        if(that.passWord !== '') {
                            data.password = that.passWord
                        }

                        console.log('token:', that.token)
                        console.log('oldname:', oldUserName)

                        // 将令牌和填写的数据发送到 axios 更新数据
                        axios
                            .patch( 
                                /* TODO:此处报错 转发到了 8080:user/bg/user 404
                                    第一个user为该页面地址 与路由 index同步
                                    与正常运行的 Login.vue.sigin.axios.post比较
                                    sigin的 post地址为 8080:bg/token 无路由前缀
                                        改为 post也一样，排除 patch/post差异
                                        在authorization()之前也一样，排除 .then包围影响
                                */
                                'bg/user/' + oldUserName + '/', {
                                    username: data.username,
                                    password: data.password,
                                }, 
                                {headers:{Authorization:'Bearer'+that.token}} // token验证字段 头对象
                            )
                            .then(function (response) {
                                const name = response.data.userName
                                storage.setItem('username.myblog', name)
                                that.$router.push({
                                    name:'UserCenter', 
                                    params:{username:name}
                                })
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