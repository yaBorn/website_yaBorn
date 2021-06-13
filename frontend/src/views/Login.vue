<!--
    用户注册页面
-->

<!-- html -->
<template>
    <div id="login">
        <BlogHeader ref="header"/>
        <div id="grid">
            <!-- 用户注册 -->
            <div id="signup">
                <h3>
                    注册账号
                </h3>
                <form>
                    <div class="form-elem">
                        <!-- TODO:输入格式限制 -->
                        <!-- 后端密码限制：小于150字符，只包括字母、数字和@/./+/-/_ 详见:8000/bg/user/ -->
                        <span>账号名称：</span> 
                        <input v-model="signupName" type="text" placeholder="输入用户名">
                    </div>
                    <div class="form-elem">
                        <span>输入密码：</span> 
                        <input v-model="signupPwd" type="text" placeholder="输入密码">
                    </div>
                    <div class="form-elem">
                        <span>再次输入：</span> 
                        <input v-model="signupPwdtest" type="password" placeholder="输入密码">
                    </div>
                    <!-- 错误提示框 -->
                    <div id="putgrid">
                        <div class="form-elem">
                            <button v-on:click.prevent="signup">
                                注册
                            </button>
                        </div>
                        <div class="message">
                            <p v-text="errorMessageUp"></p>
                        </div>
                    </div>
                </form>
            </div>

            <!-- 用户登录 -->
            <div id="signin">
                <h3>
                    登录账号
                </h3>
                <form>
                    <div class="form-elem">
                        <span>账号：</span> 
                        <input v-model="signinName" type="text" placeholder="输入用户名">
                    </div>
                    <div class="form-elem">
                        <span>密码：</span> 
                        <input v-model="signinPwd" type="text" placeholder="输入密码">
                    </div>
                    <!-- 错误提示框 -->
                    <div id="putgrid">
                        <div class="form-elem">
                            <button v-on:click.prevent="signin">
                                登录
                            </button>
                        </div>
                        <div class="message">
                            <p v-text="errorMessageIn"></p>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
    import axios from 'axios';
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'

    export default {
        name: 'Login',
        components: {
            BlogHeader, 
            BlogFooter,
        },
        data: function () {
            return {
                signupName: '',
                signupPwd: '',
                signupPwdtest: '',
                errorMessageUp:'',
                signupResponse: null,

                signinName: '',
                signinPwd: '',
                errorMessageIn: '',
            }
        },
        methods: {
            // 注册按钮回调
            signup () {
                console.log('-----Login.vue.signup')

                const that = this;
                this.errorMessageIn = '' // 重置信息框 二次修改
                // 判断空值
                if(this.signupName=='' || this.signupPwd=='' || this.signupPwdtest=='') {
                    this.errorMessageUp = '输入为空'
                    return
                }
                // 验证密码
                if(this.signupPwd !== this.signupPwdtest) {
                    // alert('密码不一致，请重新输入');
                    this.errorMessageUp = '密码不一致，请重新输入'
                    return
                }
                // axios将注册数据 post到 bg/user完成注册
                axios
                    // TODO:VUE_axios_post报错 request failed with status code 403
                    // dijango后台报错 post 403 58
                    // 但从dijango后台 bg/user/可以 post
                    // dijango后台登录了管理员账户，此时前端注册则报错403 58
                    .post('/bg/user/', {
                        username: this.signupName,
                        password: this.signupPwd,
                    })
                    .then(function (response) {
                        /* TODO:js中 
                            this为call()方法调用函数时传递的第一个参数
                            this在函数调用时修改，在函数没有调用的时候，this的值无法确定。
                            即 then()中直接使用 this 但 this未定义 导致报错 https://juejin.cn/post/6844903573428371464
                        */
                        that.signupResponse = response.data
                        // alert('用户注册成功！')
                        that.errorMessageUp = '用户注册成功！'
                    })
                    .catch(function (error) {
                        // TODO: 优化报错内容 error.message
                        // 400 重复名称
                        // 403 后端页码登录
                        // alert(error.message)
                        switch(error.message) {
                            case 'Request failed with status code 400':
                                that.errorMessageUp = '该名称已注册'
                                break
                            case 'Request failed with status code 403':
                                that.errorMessageUp = '后端异常：请联系管理员'
                                break
                            default:
                                that.errorMessageUp = '意料外异常：请联系管理员'
                                alert(error.message)
                                return
                        }
                        // 报错信息见：https://github.com/axios/axios#handling-errors
                    });
            },
            // 登录按钮回调
            signin () {
                console.log('-----Login.vue.signin')

                const that = this;
                this.errorMessageIn = '' // 重置信息框 二次修改
                // 判断空值
                if(this.signinName=='' || this.signinPwd=='') {
                    this.errorMessageIn = '输入为空'
                    return
                }
                // axios将注册数据 post到 bg/user完成登录
                axios
                    .post('/bg/token/', {
                        // 发送请求申请token
                        username: this.signinName,
                        password: this.signinPwd,
                    })
                    .then(function (response) {
                            // console.log()
                            // 将token令牌，过期时间，用户数据存放到 LS
                            const storage = localStorage;
                            // Date.parse(...) 返回1970年1月1日UTC以来的毫秒数
                            // TODO:修改JWT验证时间
                            // Token 在后端 setting-SIMPLE_JWT被设置为1分钟 此处加上60000毫秒
                            // 此外 Header-mounted-axios 刷新token相同设置
                            const expiredTime = Date.parse(response.headers.date) + 60000
                            // 设置 localStorage
                            // header mounted中被使用 同步修改该名称
                            storage.setItem('access.myblog', response.data.access)
                            storage.setItem('refresh.myblog', response.data.refresh)
                            storage.setItem('expiredTime.myblog', expiredTime)
                            storage.setItem('username.myblog', that.signinName)

                            // 记录是否为管理员用户
                            axios
                                .get('/bg/user/' + that.signinName + '/')
                                .then(function (response) {
                                    // 存入缓存
                                    storage.setItem('isSuperuser.myblog', response.data.is_superuser)
                                    console.log('super权限：', response.data.is_superuser)
                                    // 刷新header组件 (TODO原因见 UserCenter.vue和 Header.vue.refresh)
                                    console.log(that.$refs.header.ss)
                                })

                            // 路由跳转 登录成功后回到博客首页
                            console.log('登录成功 账户：', that.signinName)
                            console.log('token：', response.data.access)
                            that.$router.push({name: 'Home'})
                    })
                    .catch(function (error) {
                        switch(error.message) {
                            case 'Request failed with status code 401':
                                // TODO: 优化报错内容 error.message
                                that.errorMessageIn = '账号不存在 / 密码错误'
                                break
                            case 'Request failed with status code 403':
                                that.errorMessageIn = '后端异常：请联系管理员'
                                break
                            default:
                                that.errorMessageIn = '意料外异常：请联系管理员'
                                // alert(error.message)
                                console.log(error.message)
                                return
                        }
                    });
            }
        }
    }
</script>

<!-- css -->
<style scoped>
    #grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
    #signin {
        text-align: center;
    }
    #signup {
        text-align: center;
    }
    .form-elem {
        padding: 10px;
    }
    #putgrid {
        display: grid;
        grid-template-columns: 1fr 1fr;
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