# -*- coding:utf-8 -*-
"""
模块描述:
 接口测试的方式实现图形验证码识别
作者：Sniper.ZH
"""
import requests
from baidu_api import *

# 要以会话session的方式来处理验证码
session = requests.session()
# 获取验证码图片
url = "http://127.0.0.1:8001/rand_code/?_=1627803865002"

response = session.get(url)

with open("randCode.png", "wb") as rf:
    rf.write(response.content)

# 识别图片内容
randCode = ocr_numbers("randCode.png")
print(randCode)

# 发送带验证码的登陆请求
login_url = "http://127.0.0.1:8001/dologin/"
params = {
    'username': 'admin',
    'pwd': '123456',
    'randomCode': randCode
}

response = session.post(login_url, data=params)

print(response.status_code)
print(response.json())
