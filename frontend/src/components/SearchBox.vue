<!--
    搜索框 组件
-->

<!-- html -->
<template>
    <!-- 搜索框 -->
    <div class="search">
        <!-- v-model为数据绑定 input数据和 js的searchText绑定在 共享数据内容 -->
        <input v-model="searchText" class="search-text" 
            type="text" name="" placeholder="搜索内容" maxlength="20">
        <!-- v-on:clic为按键点击事件，触发searchArticles() -->
        <!-- prevent阻止按钮初始表单提交 -->
        <button v-on:click.prevent="searchArticles" class="search-btn" href="#">
            <img class="search-icon" src="@/assets/search.png">       
            <span class="iconfont icon-search"></span>
        </button>
    </div>
</template>

<!-- js -->
<script>
    export default {
        name: 'SearchBox',
        data: function () {
            return {
                searchText: '',
            }
        },
        methods: {
            // 搜索回调函数
            searchArticles() {
                // TODO:搜索范围迭代 搜索标题/标签关键词
                // 并且在更新列表 list高亮该关键词
                // 点击button触发回调，将searchText作为参数进行路径跳转
                const text = this.searchText.trim();
                if(text.charAt(0) !== '') {
                    // 和 <router-link>类似，为脚本中的动态跳转
                    // $route路径对象 $router路由器对象
                    this.$router.push({name:'Home', query:{ search:text}})
                }
            }
        }
    }
</script>

<!-- css -->
<style scoped>
    body{
        margin: 0;
        padding: 0;
    }
    /* 盒子 */
    .search{
        /* 相对定位 相对于父组件 水平垂直居中 */
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        /* 背景 边框 圆角 */
        background: var(--white);
        border: 3px solid var(--color);
        border-radius: 40px;
        padding: 20px;
        /* 搜索盒中元素居中 */
        display: flex;
        align-items: center;
        /* 盒子初始宽高 40px  刚好包裹内部.search-btn*/
        height: 16px;
        width: 20px;
        /* 宽度速率变化 贝塞尔曲线 */
        transition:width  cubic-bezier(0.75, -0.25, 0.25, 1.5)  0.75s;
        /* 阴影 偏移 半径rgba*/
        box-shadow: 
            inset 0.2rem 0.2rem 1rem var(--hightLight),
            inset -0.2rem -0.2rem 1rem var(--dark), 
            0.3rem 0.3rem 0.6rem var(--belowShadow), 
            -0.2rem -0.2rem 0.5rem var(--topShadow);
    }
    /* 按钮 */
    .search-btn{
        color: #72727200;
        /* 去边框 */
        border: none;          
        /* 固定定位 */
        position: fixed;
        /* 放在search的右边 距离和初始盒子宽度一半一致 */
        /* Vue 不支持 CSS的--root参数形式 改不了全局参数 */
        /* TODO: CSS --root参数重构 */
        right: 10px;
        /* 内部的搜索大小 突变flex布局 保持中央*/
        display: flex;
        justify-content: center;
        align-items: center;    
        /* btn大小 */
        width: 40px;
        height: 40px;
        /* 圆形边缘 */
        border-radius: 50%;
        background: var(--color);
        border-bottom: none;
    }
    /* icon */
    .search-icon{
        width: 20px;
        height: 20px;
    }
    /* 输入框 */
    .search-text{
        /* 设置左浮动 所以会跟在外面的search的左侧移动 */
        float: left;
        padding: 0;
        line-height: 40px;
        max-inline-size: 200px;
        /* 初始宽度为0 整个search的大小为40px*40px */
        width: 0px;
        /* 去除默认输入框的背景、描边、边框 */
        background: none;
        outline: none;
        border: none;
        /* 下划线 */
        border-bottom: var(--dark) 2px solid;
        /* 字体*/
        color: var(--gray);
        font-size: 16px;
        /* 过度动画 和search一致*/
        transition:width  cubic-bezier(0.7, -0.25, 0.27, 1.55)  .8s;
    }

    /* 聚焦到搜索框的动画 */
    /* 不设置width属性的话 由内部的search-text和search-btn撑开
        但是浏览器放大到一定比例时 会出现search-btn被挤到另一行的现象
    */
    .search:hover {
        width: 250px;
    }
    /* 设置search-text的宽度 */
    .search:hover > .search-text {
        width: 200px; 
    }
    /* search-btn背景颜色变化 */
    .search:hover > .search-btn {
        background: var(--dark);
        /* 开启动画 */
        animation: global_ani1 1s infinite;
    }
</style>