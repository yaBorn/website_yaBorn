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
                    <input v-model="passWord" type="passWord" placeholder="输入密码">
                </div>

                <div class="form-elem">
                    <span>再次输入：</span> 
                    <input v-model="passWordTest" type="passWord" placeholder="输入密码">
                </div>

                <!-- 错误提示框 -->
                <div id="grid">
                    <div class="form-elem">
                        <button v-on:click.prevent="changInfo">
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
        mounted () {
            this.userName = storage.getItem('userName.myblog')
        },
        menthods: {
            // 更新按钮 回调函数
            changeInfo () {
                const that = this
                // TODO:更多的格式化
                // 验证二次输入
                if(that.passWord !== that.passWordTest) {
                    // alert('密码不一致，请重新输入')
                    that.errorMessage = '密码不一致，请重新输入'
                    return
                }
                // 格式规定 密码长度
                if( that.passWord.length > 0 && that.passWord.length < 6) {
                    that.errorMessage = '密码需大于6位'
                    return
                }
                /* 调用 func-authorization() 进行用户验证
                    旧方法见 git提交历史 2021.6.8 16：03 用户登录 Login.vue-methods
                */
                authorization()
                    .then(function (response) {
                        // 检查登录状态
                        if( !response[0]) {
                            that.errorMessage = '登录过期，请重新登录'
                            console.log('-----UserCenter.vue')
                            console.log('登录过期，请重新登录')
                            return
                        }
                        // 获取令牌
                        that.token = storage.getItem('access.myblog')
                        // 旧 username用于 axios发送数据
                        const oldUserName = storage.getItem('username.myblog')
                        // 获取填写的数据
                        let data = {}
                        if(that.userName !=='') { // 判空 空则不更新
                            data.username = that.userName
                        }
                        if(that.passWord !== '') {
                            data.password = that.passWord
                        }
                        // 将令牌和填写的数据发送到 axios 更新数据
                        axios
                            .patch(
                                'bg/user/'+oldUserName+'/',
                                data, 
                                {headers: {Authorization:'Bearer'+that.token}}
                            )
                            .then(function (response) {
                                const name = response.data.userName
                                storage.setItem('username.myblog', name)
                                that.$router.push({
                                    name:'UserCenter', 
                                    params:{username:name}
                                })
                            })
                    })
            }
        }
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
        width: 200px;
    }
</style>