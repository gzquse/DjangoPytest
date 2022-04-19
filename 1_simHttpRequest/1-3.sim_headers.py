# -*- coding:utf-8 -*-
"""
模块描述:
 头部参数的使用 请求头部和响应头部
作者：Sniper.ZH
"""
import requests


baidu_search_url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

response = requests.get(baidu_search_url, headers=headers)

# 查看响应头
print(response.headers)
print(type(response.headers))
print("Content-Type:", response.headers.get('Content-Type'))
print("Date:", response.headers.get('Date'))

# 查看所有的响应头
print("----------response headers------------")
for key in response.headers.keys():
    print(key, response.headers.get(key))
print("----------response headers------------")

# 查看所有的请求头
print("----------request headers------------")
for key in response.request.headers.keys():
    print(key, response.request.headers.get(key))
print("----------request headers------------")

if response.status_code == 200:
    # 将得到的结果写入html文件
    with open("temp_wd.html", "wb") as wf:
        wf.write(response.content)
else:
    print("通讯异常:", response.status_code)

