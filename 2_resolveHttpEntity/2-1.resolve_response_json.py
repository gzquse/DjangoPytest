# -*- coding:utf-8 -*-
"""
模块描述:
 解析Json响应报文
作者：Sniper.ZH
"""
import requests
import json

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

if response.status_code == 200 and response.json()['code'] == 0:
    print(response.text)

    # 创建需求申请
    apply_url = 'http://127.0.0.1:8001/commit_order/'
    params = {
        'order_dep': '001',
        'order_date': '2021-07-23',
        'order_name': '需求名称',
        'order_sys': 'sys',
        'order_type': 'change',
        'order_desc': '描述信息',
    }

    # 在后续请求方法中，把Cookies上送
    response = session.post(apply_url, data=params)
    print("申请的状态码:", response.status_code)

    for key in response.headers.keys():
        print(f"{key} --> {response.headers[key]}")

    if response.status_code == 200:
        response.encoding = 'utf-8'
        print(response.text)

        # 解析响应报文体
        # Json格式

        print(response.json())
        print(type(response.json()))

        # 格式化输出json内容
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

        # 获取响应码

        rspCode = response.json()['code']
        print("响应码:", rspCode)
        if rspCode == 0:
            print("新增需求编号:", response.json()['order_id'])
        else:
            print("申请错误:", rspCode)
            print("错误的原因:", response.json().get('msg'))
    else:
        print("需求申请通讯失败:", response.status_code)
else:
    print("登陆异常:", response.status_code)
