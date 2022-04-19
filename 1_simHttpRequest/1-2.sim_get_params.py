# -*- coding:utf-8 -*-
"""
模块描述:
 上送get请求参数
作者：Sniper.ZH
"""
import requests


# 第一种get传参方法,直接写在url后面
# baidu_search_url = "https://www.baidu.com/s?wd=python"

# 第二种get传参方法,定义参数dict
baidu_search_url = "https://www.baidu.com/s"

# 定义请求头部参数，模拟成谷歌浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# 参数
params = {
    "wd": "python"
}

response = requests.get(baidu_search_url, params=params, headers=headers)

print(response.request.headers)

if response.status_code == 200:
    # 将得到的结果写入html文件
    with open("temp_wd.html", "wb") as wf:
        wf.write(response.content)
else:
    print("通讯异常:", response.status_code)

