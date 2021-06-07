<!-- 
    组件 页眉 
        Home.vue
-->

<!-- html -->
<template>
    <!-- 页眉 -->
    <div id="header">
        <!-- 布局 -->
        <div class="grid">
            <!-- 搜索框 -->
            <div class="search">
                <form>
                    <input type="text" placeholder="输入内容...">
                    <button></button>
                </form>
            </div>
            <!-- 标题 -->
            <router-link :to="{name:'Home'}"> <!-- 点击跳转回 home -->
                <div class="headertex">
                    <h1>yaBorn Blog</h1>
                </div>
            </router-link>
            <!-- grid布局 搜多-标题-空 -->
            <div></div>
        </div>
        <!-- 底部下划线 -->
        <hr>
    </div>
</template>

<!-- js -->
<script>
    export default {
        name: 'BlogHeader',
    }
</script>

<!-- css -->
<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
    #header {
        text-align: center;
        margin-top: 20px;
    }
    .grid { 
        display: grid;
        grid-template-columns: 1fr 4fr 1fr; /* grid布局 1:4:1 空白-标题-搜索框 */
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
</style>
<!-- 搜索框 css 样式 -->
<style scoped>
    * {
        box-sizing: border-box;
    }
    form {
        position: relative;
        width: 200px;
        margin: 0 auto;
    }
    input, button {
        border: none;
        outline: none;
    }
    input {
        width: 100%;
        height: 35px;
        padding-left: 13px;
        padding-right: 46px;
    }
    button {
        height: 35px;
        width: 35px;
        cursor: pointer;
        position: absolute;
    }
    .search input {
        border: 2px solid rgba(78, 79, 97, 0.678);
        border-radius: 5px;
        background: transparent;
        top: 0;
        right: 0;
    }
    .search button {
        background: rgba(78, 79, 97, 0.678);
        border-radius: 0 5px 5px 0;
        width: 45px;
        top: 0;
        right: 0;
    }
    .search button:before {
        content: "搜索";
        font-size: 13px;
        color: rgba(255, 255, 255, 0.904);
    }
</style>
