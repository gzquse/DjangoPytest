# -*- coding:utf-8 -*-
"""
模块描述:
 模拟操作Cookies
作者：Sniper.ZH
"""
import requests

# 首先要完成登录，获得Cookies
login_url = "http://localhost:8001/dologin/"
params = {
    'username': 'admin',
    'pwd': '123456',
    'randomCode': '3223'
}
response = requests.post(login_url, data=params)

print(response.status_code)

# 使用Cookies，来讲无状态的问题进行解决
cookies = response.cookies
print(cookies)
print(type(cookies))
print(cookies.get('sessionid'))
print(cookies.list_domains())
print(cookies.list_paths())
print(cookies.get_dict())

if response.status_code == 200 and response.json()['code'] == 0:
    print(response.text)

    # 创建需求申请
    apply_url = 'http://localhost:8001/commit_order/'
    params = {
        'order_dep': '001',
        'order_date': '2021-07-24',
        'order_name': '需求名称',
        'order_sys': 'sys',
        'order_type': 'change',
        'order_desc': '描述信息',
    }

    # 在后续请求方法中，把Cookies上送
    response = requests.post(apply_url, data=params, cookies=cookies)
    print("申请的状态码:", response.status_code)
    response.encoding = 'utf-8'
    print(response.text)
    print(response.json())
