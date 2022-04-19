# -*- coding:utf-8 -*-
"""
模块描述:
 模拟最基础的get请求
 1.安装环境，requests三方库
  python + requests
作者：Sniper.ZH
"""
import requests

"""
协议：目标 内容 规则
目标：百度网站
规则：http协议来请求
内容：首页的html文档

网络编程：
客户端： 客户端就是我们python代码
服务端： 百度网站
请求： request
响应： response
"""

# 最基础的get请求
baidu_url = "https://www.baidu.com/"
# 模拟http请求
# 必须用变量来接收请求后的响应内容
response = requests.get(baidu_url)
print(response)
print(type(response))

# 响应中应该包含
# 状态码 2xx 3xx 4xx 5xx
status_code = response.status_code
print("状态码:", status_code)

if status_code == 200:   # 请求执行成功
    # 获取报文实体内容
    # html文档
    print(response.text)

    # 编码方式 中文 GB2312 GBK UTF-8
    print("编码方式:" + response.encoding)

    # 1. content 获取bytes
    print(response.content)
    print("text类型:", type(response.text))
    print("content类型:", type(response.content))
    print(response.content.decode("utf-8"))

    # 2.改变response的编码方式，再获取text
    response.encoding = "utf-8"
    print(response.text)  # property装饰的方法会变成属性，只读属性

    # response.text = "abc"
