# ShortLink

没有做鉴权服务，并且这里没有使用关系型数据库，所以没有执行django数据库迁移命令

> 开发环境python3.7+PyCharm

1. 启动redis服务器
2. 启动django服务器
python3 manage.py runserver 0.0.0.0:8888
3. 使用
- 发送post请求
```json
http://127.0.0.1:8888
data: {
    url: 'http://www.xxx.com/s/x/asdfeafsafe/hhuehnase'
}
```
返回短网址:
```json
{
    link: 'http://127.0.0.1:8888/xiendi'
}
```
- 访问连接
访问短连接：http://127.0.0.1:8888/xiendi，目前只实现了GET请求，其他请求与之类似
