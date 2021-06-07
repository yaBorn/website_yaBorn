<!--
    用户注册页面
-->

<!-- html -->
<template>
    <div id="login">
        <BlogHeader/>
        <div id="grid">
            <!-- 用户注册 -->
            <div id="signup">
                <h3>注册账号</h3>
                <form>
                    <div class="form-elem">
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
                    <div class="form-elem">
                        <button v-on:click.prevent="signup">提交</button>
                    </div>
                </form>
            </div>

            <!-- 用户登录 -->
            <div>
            </div>
        </div>
        <BlogFooter/>
    </div>
</template>

<!-- js -->
<script>
    import axios from 'axios';
    import BlogHeader from '@/components/my/BlogHeader.vue'
    import BlogFooter from '@/components/my/BlogFooter.vue'

    export default {
        name: 'Login',
        components: {BlogHeader, BlogFooter},
        data: function () {
            return {
                signupName: '',
                signupPwd: '',
                signupPwdtest: '',
                signupResponse: null,
            }
        },
        methods: {
            signup() {
                const that = this;
                // 验证密码
                if(this.signupPwd !== this.signupPwdtest) {
                    alert('密码不一致，请重新输入');
                    return
                }
                // axios将注册数据 post到 bg/user完成注册
                axios
                    // TODO:VUE_axios_post报错 request failed with status code 403
                    // dijango后台报错 post 403 58
                    // 但从dijango后台 bg/user/可以 post
                    // dijango后台登录了管理员账户，此时前端注册则报错403 58
                    .post('/bg/user/', 
                        {
                            username: this.signupName,
                            password: this.signupPwd,
                        }
                    )
                    .then(function (response) {
                        /* TODO:js中 
                            this为call()方法调用函数时传递的第一个参数
                            this在函数调用时修改，在函数没有调用的时候，this的值无法确定。
                            即 then()中直接使用 this 但 this未定义 导致报错 https://juejin.cn/post/6844903573428371464
                        */
                        that.signupResponse = response.data;
                        alert('用户注册成功，快去登录吧！');
                    })
                    .catch(function (error) {
                        // TODO: 优化报错内容
                        // 400 重复名称
                        alert(error.message);
                        // 报错信息见：https://github.com/axios/axios#handling-errors
                    });
            },
        }
    }
</script>

<!-- css -->
<style scoped>
    #grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
    #signup {
        text-align: center;
    }
    .form-elem {
        padding: 10px;
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