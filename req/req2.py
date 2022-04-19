#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : req2.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/5 18:57
Desc:
"""
import requests

baidu_url = "https://www.baidu.com/s"
headers ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
params = {
    "wd": "python"
}
res = requests.get(baidu_url, headers=headers, params=params)
print(res.request.headers)

if res.status_code == 200:
    with open('temp_wd.html', 'wb') as wf:
        wf.write(res.content)
else:
    print('error', res.status_code)


