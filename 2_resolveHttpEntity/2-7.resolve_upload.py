# -*- coding:utf-8 -*-
"""
模块描述:
 文件上传的方法
作者：Sniper.ZH
"""
import requests

url = "http://127.0.0.1:8001/fileUpload/"

files = {
    "baidu_logo": open("baidu.png", "rb")
}

# files参数和files文件字典
response = requests.post(url, files=files)

print(response.status_code)
response.encoding = 'utf-8'
print(response.json())
