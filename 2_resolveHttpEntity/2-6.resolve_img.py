# -*- coding:utf-8 -*-
"""
模块描述:
    获取百度logo图片
作者：Sniper.ZH
"""
import requests

# 图片的类型 image/png
url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

response = requests.get(url)
#
# print(response.status_code)
# # 不能用text content来打印查看内容了
# print(response.text)
# print(response.content)
#
print(response.headers.get("Content-Type"))
#
# # 必须将它保存到文件系统中，使用对应的工具来查看
with open("baidu.png", "wb") as bf:
    bf.write(response.content)


# 百度首页的类型是 text/html
# url = "https://www.baidu.com"
# response = requests.get(url)
# print(response.status_code)
# print(response.headers.get("Content-Type"))

# 登陆请求 json application/json
# login_url = "http://127.0.0.1:8001/dologin/"
# params = {
#     'username': 'admin',
#     'pwd': '123456',
#     'randomCode': '3223'
# }
# response = requests.post(login_url, data=params)
# print(response.headers.get("Content-Type"))

# mimeType
# text/html application/json image/png image/jpeg

# 就是文件下载、206 200
