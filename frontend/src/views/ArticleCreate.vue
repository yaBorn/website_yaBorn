<!-- 
    创建文章 页面
-->

<!-- html -->
<template>
    <div id='articlecreat'>
        <BlogHeader/>
        <div id="article-create">
            <h3>发表文章</h3>
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
                <button class='post-btn' v-on:click.prevent="submit">提交</button>
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
                    return { backgroundColor: 'black', }
                }
                return {
                    backgroundColor: 'lightgrey',
                    color: 'black',
                }
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
        cursor: pointer;
        border: none;
        outline: none;
        background: steelblue;
        color: whitesmoke;
        border-radius: 5px;
        width: 80px;
    }
    .post-btn {
        position: relative;
        left: 600px;
    }
</style>
