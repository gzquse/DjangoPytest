# -*- coding:utf-8 -*-
"""
模块描述:
 模拟post请求
作者：Sniper.ZH
"""
import requests

login_url = "http://127.0.0.1:8001/dologin/"

params = {
    'username': 'admin',
    'pwd': '123123123123',
    'randomCode': '33333',
}

# post请求就是把get方法换成post方法
# 传递参数 使用data参数
# headers 头部参数和get请求相同
# put/delete/trace/header
response = requests.post(login_url, data=params)

if response.status_code == 200:
    print(response.text)
