/*
Vue配置文件
    跨域代理
        后端Django端口：8000 前端Vue.js端口：8080
        两者不一致，Javascript无法请求到后端资源
        对前端服务器设置代理，将 bg/8080端口_前端请求 --转发-> bg/8000端口_后端
        从而解决跨端口问题
*/

/* 前端端口bg --转发-> 后端端口bg */
module.exports = {
    devServer: {
        proxy: {
            '/bg': {
                target: `http://127.0.0.1:8000/bg`,
                changeOrigin: true,
                pathRewrite: {
                    '^/bg': ''
                }
            }
        }
    }
};
