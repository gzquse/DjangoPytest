# -*- coding:utf-8 -*-
"""
模块描述:
 模拟操作Cookies
 使用session会话方式
作者：Sniper.ZH
"""
import requests

# 首先要完成登录，获得Cookies
login_url = "http://127.0.0.1:8001/dologin/"
params = {
    'username': 'admin',
    'pwd': '123456',
    'randomCode': '3223'
}

# 使用session会话方式
session = requests.session()
response = session.post(login_url, data=params)

print(response.status_code)

# 使用Cookies，来讲无状态的问题进行解决
# 使用了会话，就不需要手工处理Cookies了
# cookies = response.cookies

if response.status_code == 200 and response.json()['code'] == 0:
    print(response.text)

    # 创建需求申请
    apply_url = 'http://127.0.0.1:8001/commit_order/'
    params = {
        'order_dep': '001',
        'order_date': '2021-07-24',
        'order_name': '需求名称',
        'order_sys': 'sys',
        'order_type': 'change',
        'order_desc': '描述信息',
    }

    # 在后续请求方法中，把Cookies上送
    response = session.post(apply_url, data=params)
    print("申请的状态码:", response.status_code)
    response.encoding = 'utf-8'
    print(response.text)
