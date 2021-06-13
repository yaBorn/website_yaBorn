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
    TODO:BUG
    BUG-后台一直报
        GET http://192.168.32.105:8080/sockjs-node/info?t=1623033929802 net::ERR_CONNECTION_TIMED_OUT
        发现sockjs-node库创建了一个低延迟、全双工的 用于浏览器和web服务器间的通信通道
        在项目运行的时候会自动调用该接口，如果没有使用，则报错
            1.打开node_modules包并找到/sockjs-client/dist/sockjs.js文件 1609line
            2.ctrl+f搜索self.xhr.send(payload)这段代码，找到之后注释掉
            但是关闭之后，热更新失效。
            此文件是放在npm的文件下的，所以在开发过程中临时关闭，后续部署还是会打开的，没有太大的影响。
            因此实际上可以不用管。
-->

<script>
    /* JWT tocken令牌 */
    // Django.setting.py.SIMPLE_JWT.ACCESS_TOKEN_LIFETIME 一致
    // const JWT_unit = 'minutes' // 未判断其他单位 TODO：想加再改
    const JWT_num = 10
    const JWT_time = 60000*JWT_num // 毫秒

    export default
    {
        JWT_time,
    }
</script>
