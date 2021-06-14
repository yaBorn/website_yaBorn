<!-- 
    创建文章 页面
        TODO:在该页面等待权限过期，过期后 设置自动跳转
        将权限单独抽离为一个线程或模块
-->

<!-- html -->
<template>
    <div id='articlecreat'>
        <BlogHeader/>
        <div id="article-create">
        <div class='global_block'>
        <div class='global_block_content'>
            <h3>发表文章</h3>
            <!-- 标题图像 -->
            <form id="image_form">
                <div class="form-elem">
                    <span>标题图像：</span>
                    <!-- 选定文件 触发ofc方法 -->
                    <input v-on:change="onFileChange" 
                        type="file" id="file"
                        accept="image/gif,image/jpeg,image/png">
                        <!-- TODO:迭代更多的im格式 -->
                        <!-- TODO:前端未加密，存在安全问题，在后端也补上相应验证 -->
                        <!-- TODO:覆写后端model.save()方法 执行图像压缩 -->
                        <!-- TODO:存在自己服务器吃资源 对象储存云服务器部署？ -->
                        <!-- TODO：标题图仅自己的图片资源，外部链接？想md外链那样 然后用gitee储存 -->
                </div>
            </form>
            
            <!-- 文章内容 -->
            <form>
            <div class="form-elem">
                <span>标题：</span>
                <input v-model="title" type="text" placeholder="输入标题">
            </div>

            <div class="form-elem">
                <span>分类：</span>
                <span
                    v-for="category in categories"
                    :key="category.id"
                    >
                <!--样式通过 :style 绑定-->
                <button
                        class="category-btn"
                        :style="categoryStyle(category)"
                        @click.prevent="chooseCategory(category)"
                        >
                    {{category.title}}
                </button>
                </span>
            </div>

            <div class="form-elem">
                <span>标签：</span>
                <input v-model="tags" type="text" placeholder="输入标签，用逗号分隔">
            </div>

            <div class="form-elem">
                <span>正文：</span>
                <textarea v-model="body" placeholder="输入正文" rows="20" cols="80"></textarea>
            </div>

            <div class="form-elem">
                <button class="global_btn btn__primary post-btn" v-on:click.prevent="submit">提交</button>
            </div>
            </form>
        </div>
        </div>
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

    export default {
        name: 'ArticleCreate',
        components: {
            BlogHeader, 
            BlogFooter,
        },
        data: function () {
            return {
                title: '',  // 文章标题
                body: '',  // 文章正文
                categories: [],  // 数据库中所有的分类
                selectedCategory: null,  // 选定的分类
                tags: '',  // 标签

                imageID: null, // 标题图像id
            }
        },
        mounted() {
            // 页面初始化时获取所有分类
            axios
                .get('/bg/category/category-list/') // TODO 后端路径参数
                .then(response => this.categories = response.data)
        },
        methods: {
            // 根据分类是否被选中，按钮颜色变化
            // css 也是可以被 vue 绑定
            categoryStyle(category) {
                if (this.selectedCategory!==null && category.id===this.selectedCategory.id) {
                    return { backgroundColor: 'var(--hightLight)', }
                }
                return {
                    backgroundColor: 'lightgrey',
                    color: 'black',
                }
            },
            // 标题图像文件上传
            // e为控件所触发的事件对象
            onFileChange(e) {
                // 二进制文件数据添加入上传数据中
                // 图像二进制流不应该表示为字符串数据 应使用FormData表单对象
                // var urlname = that.$route.path.split("/").pop() // 页面径最后一个元素(用户名称)
                const file = e.target.files[0]
                let formData = new FormData()
                formData.append("content", file)
                formData.append("title", '标题图')
                formData.append("describe", '标题图')
                // TODO：图像上传早于标题输入等
                //      判断标题输入后才可上传图像，然后标题和描述可用之前输入信息 与文章关联
                // /bg/photo/需要post 标题 描述 文件 否则 Bad Request
                // TODO:如何一次性post formData+headers 和 标题/描述
                // 通过formData的append方法 文档https://developer.mozilla.org/zh-CN/docs/Web/API/FormData

                // TODO:增加错误排查 权限审查
                
                // 发送图像到后端
                axios
                    .post('/bg/photo/',
                        formData, 
                        {headers: {
                            'Content-Type': 'multipart/form-data',
                            'Authorization': 'Bearer ' + localStorage.getItem('access.myblog')
                        }})
                    .then( response => this.imageID = response.data.id)
            },
            // 选取分类的方法
            chooseCategory(category) {
                // 点击已选取的分类 将 selectedCategory 置空
                if (this.selectedCategory!==null && this.selectedCategory.id===category.id) {
                    this.selectedCategory = null
                }
                // 未选中当前分类 选中它
                else {
                    this.selectedCategory = category;
                }
            },
            // 点击提交按钮 回调函数
            submit() {
                const that = this;
                // 验证用户
                authorization().then(function (response) {
                    if (response[0]) {
                        console.log('-----ArticleCreate.submit')
                        // 需要传给后端的数据字典
                        let data = {
                            title: that.title,
                            body: that.body,
                        };

                        // 添加分类
                        if (that.selectedCategory) {
                            data.category_id = that.selectedCategory.id
                        }
                        // 标签预处理 转为接口对应数据
                        data.tags = that.tags
                            .split(/[,，]/) // 用逗号分隔标签
                            .map(x => x.trim()) // 剔除标签首尾空格
                            .filter(x => x.charAt(0) !== '') // 剔除长度为零的无效标签

                        // 添加标题图
                        // onFileChange()上传了图像 返回了id 此处直接postid
                        if (that.imageID) {
                            // TODO:代码解耦 发送的data名称需与后端一致
                            // 建立全局参数表
                            data.photo_id = that.imageID
                        }

                        // 将发表文章请求发送至接口
                        // 成功后前往详情页面
                        console.log('submitData:', data)                      
                        const token = localStorage.getItem('access.myblog');
                        axios
                            .post('/bg/article/article-list/',
                                data,
                                {headers: {Authorization: 'Bearer ' + token}}
                                // TODO 报错psot 500
                                // 如果postman测试正常 则前端传给后端的数据内容有误
                                // ...末尾没有/
                                // TODO 提交成功 但是body部分提交失败
                            )
                            .then(function (response) {
                                that.$router.push({name: 'ArticleDetail', params: {id: response.data.id}});
                            })
                    }
                    else {
                        alert('令牌过期，请重新登录。')
                    }
                })
            }
        }
    }
</script>

<!-- css -->
<style scoped>
    .global_block {
        /* 内外边框 */
        text-align: center;
        padding: 0px 0px 0px 0px;
        margin: 20px 0px 0px 0px;
    }
    .category-btn {
        margin-right: 10px;
    }
    #article-create {
        text-align: center;
        font-size: large;
    }
    form {
        text-align: left;
        padding-left: 100px;
        padding-right: 10px;
    }
    .form-elem {
        padding: 10px;
    }
    input {
        height: 25px;
        padding-left: 10px;
        width: 50%;
    }
    button {
        height: 35px;
        border: none;
        outline: none;
        width: 80px;
    }
    .post-btn {
        position: relative;
        left: 70%;
    }
</style>
