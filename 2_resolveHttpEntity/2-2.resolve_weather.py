# -*- coding:utf-8 -*-
"""
模块描述:
 实战：中国天气网接口查询
作者：Sniper.ZH
"""
import requests
import json

url = "http://wthrcdn.etouch.cn/weather_mini"
params = {
    'city': "北京"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.text)
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))

    print("查询到的状态码:", response.json()['status'])

    rjson = response.json()
    if response.json()['status'] == 1000:
        print("城市:", rjson['data']['city'])
        print("温度:", rjson['data']['wendu'], "℃")
        print("感冒提示:", rjson['data']['ganmao'])

        for day in rjson['data']['forecast']:
            # print(day)
            print(f"{day['date']}: {day['type']}, 温度{day['high']}~{day['low']}, 风力{day['fengli'][9:-3]}")

    else:
        print("查询失败:", rjson['status'], rjson['desc'])
else:
    print("通讯失败:", response.status_code)
