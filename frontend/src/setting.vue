<!--
    全局参数 配置文件
        目的在于代码解耦 
        原理：
            1. 设置专用全局变量模块文件，模块里面定义变量初始状态
            2. 用export default 暴露出去
            3.1 (采用) 或者在其它地方需要使用时，引入该模块
                    import set_ from '@/setting.vue'
                    use: set_.xxx
            3.2 在main.js里面使用 Vue.prototype挂载到 vue实例上面，然后this.xx.xx调用
                    main.js:
                        import set_in from '@/setting.vue'
                        Vue.prototype.set_ = set_in //挂载到Vue实例上面
                    use:
                        this.set_.xxx
-->

<script>
    /* JWT tocken令牌 */
    // Django.setting.py.SIMPLE_JWT.ACCESS_TOKEN_LIFETIME 一致
    const JWT_unit = 'minutes' // 未判断其他单位 TODO：想加再改
    const JWT_num = 10
    const JWT_time = 60000*JWT_num // 毫秒

    export default
    {
        JWT_time,
    }
</script>
