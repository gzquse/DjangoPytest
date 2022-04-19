# -*- coding:utf-8 -*-
"""
模块描述:
 使用https协议注意事项
作者：Sniper.ZH
"""
import requests

# certifi这个库，帮我们记录了常用的https证书
# 如果，SSLError
# varify = False
# 尝试更新certifi requests库到最新版本
url = "https://www.baidu.com"

response = requests.get(url, varify=False)

print(response.status_code)

# 双向整数的请求方法
cert = ("证书的存放路径", "密钥文件存放位置")
# ssl 双向加密的算法， 非对称加密
response = requests.get(url, cert=cert)
