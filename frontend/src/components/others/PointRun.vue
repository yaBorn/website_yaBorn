<!-- 
    点动画 组件
-->

<!-- js -->
<script>
    export default {
        name: 'PointRun',
    }
</script>

<!-- html -->
<template>
    <div id="PointRun">
        <div class="dotsBars">
        </div>
    </div>
</template>

<!-- css -->
<style scoped>
    #PointRun {
        margin: 10px 30px 0px 30px;
    }
    .dotsBars {
        width: 40px;
        height: 20px;
        --c:radial-gradient(farthest-side,currentColor 50%, var(--darker));
        background:
            var(--c) 0    0,
            var(--c) 50%  0,
            var(--c) 100% 0;
        background-size:8px 8px;
        background-repeat: no-repeat;
        position: relative;
        top: 30px;
        animation: db-0 1s linear infinite alternate;
    }
    .dotsBars:before {
        content: "";
        position: absolute;
        width: 8px;
        height: 12px;
        background:currentColor;
        left:0;
        top:0;
        animation: 
            db-1 1s  linear infinite alternate,
            db-2 0.5s cubic-bezier(0,200,.8,200) infinite;
    }
    /* 圆点间断跳跃 */
    @keyframes db-0 {
        0%      {background-position: 0  100%,50% 0   ,100% 0}
        8%,42%  {background-position: 0  0   ,50% 0   ,100% 0}
        50%     {background-position: 0  0   ,50% 100%,100% 0}
        58%,92% {background-position: 0  0   ,50% 0   ,100% 0}
        100%    {background-position: 0  0   ,50% 0   ,100% 100%}
    }
    /* 方块左右移动 */
    @keyframes db-1 {
        100% {left:calc(100% - 8px)}
    }
    /* 方块上下移动 */
    @keyframes db-2 {
        100% {top:-0.1px}
    }
    body {
        display: grid;
        grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
        grid-auto-rows: 130px;
        place-items:center;
    }
    * {
        box-sizing: border-box;
    }
</style>
