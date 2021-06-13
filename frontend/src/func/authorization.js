/*
    JWT用户验证
        用于 Header.vue UserCenter.vue
 */

import axios from 'axios'
import set_ from '@/setting.vue'

/* 异步关键字 async 表示 func内含异步
    axios请求是异步的 需要将异步同步
    不然 localStorage因网络速度导致存取顺序bug
*/
async function auhorization () {
    /*  localStorage与 cookie类似 为用户本地储存
        浏览器隐私模式 localStorage不可读
        为字符串存取，json格式需要 JSON.stringfy()转化
        localStorage爬虫爬不到
    */
    const storage = localStorage

    // 获取 login.vue存取的令牌数据
    // 与 login-setItem名称相同
    let username = storage.getItem('username.myblog') // 账号名称
    const expiredTime = Number(storage.getItem('expiredTime.myblog')) // 过期时间
    const current = (new Date()).getTime() // 当前时间
    const refreshToken = storage.getItem('refresh.myblog') // 刷新
    let hasLogin = false // 登录标记

    console.log(' ')
    console.log('--auhorization.js')
    console.log('账户：', username)
    console.log('当前时间:', current)
    console.log('过期时间:', expiredTime)
    console.log('刷新标识:', refreshToken)

    // token未过期
    if (expiredTime > current) {
        hasLogin = true
        console.log('令牌未过期')
    }
    // token过期 但在可更新时间内
    // 此处 可延长一次令牌时间
    // TODO：改进为 判定 Django.setting.SIMPLE_JWT.REFRESH_TOKEN_LIFETIME 的时长内 连续更新
    else if(refreshToken !== null){
        try {
            // axios重新 post token
            // await用在 async函数内 表示等待异步结果
            // async不返回return 后数据 而是一个 Promise对象 其可能为 rejected 因此用 try包围
            let response = await axios.post('/bg/token/refresh/', {refresh: refreshToken})

            // 更新值
            const newExpiredTime = Date.parse(response.headers.date) + set_.JWT_time
            storage.setItem('access.myblog', response.data.access)
            storage.setItem('expiredTime.myblog', newExpiredTime)
            console.log('刷新令牌返回freshToken: ', response.data.refresh) // refresh获取的新token 不返回refresh token
            storage.removeItem('refresh.myblog') // 刷新后移去刷新token(再次过期则失效)
            hasLogin = true

            console.log('刷新令牌')
            console.log('token:', response.data.access)
        }
        catch (error) {
            // .clear() 清空当前域名下所有的值
            storage.clear()
            hasLogin = false
            console.log('刷新令牌，error:', error.message)
            // TODO:刷新令牌失败
        }
    }
    // token过期 失效
    else {
        storage.clear()
        hasLogin = false
        console.log('令牌失效，清空token')
    }

    console.log('return:', hasLogin, username)
    return [hasLogin, username]
}

export default auhorization // 导出函数 以便其他程序 import