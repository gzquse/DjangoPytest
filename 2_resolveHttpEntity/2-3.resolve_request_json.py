# -*- coding:utf-8 -*-
"""
模块描述:
 请求时上送json数据
作者：Sniper.ZH
"""
import requests
import json


query_url = 'http://127.0.0.1:8001/orderQueryApi/'
json_params = {
    "page": 1,
    "limit": 30,
    "order_dep": "003",
    "order_type": "change",
    "order_date": "2021-05-21"
}

# # 第一种，json数据请求的方法
# # 必须要指定Content-type
# headers = {
#     "Content-Type": "applycation/json"
# }
# # 必须要将参数字典转换成json字符串
# response = requests.post(query_url, data=json.dumps(json_params), headers=headers)

# 第二种方法
response = requests.post(query_url, json=json_params)

print(response.status_code)
response.encoding = 'utf-8'
print(response.text)

print(json.dumps(response.json(), indent=2, ensure_ascii=False))
