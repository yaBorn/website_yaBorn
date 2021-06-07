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
                // 检验一致性
                axios
                    .post('/api/user/', {
                        username: this.signupName,
                        password: this.signupPwd,
                    })
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
                        alert(error.message);
                        // Handling Error here...
                        // https://github.com/axios/axios#handling-errors
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