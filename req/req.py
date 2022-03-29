#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : req.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/3/28 8:52 PM
Desc:
"""

import requests as req

if __name__ == '__main__':
    baidu_url = "https://www.baidu.com/"
    res = req.get(baidu_url)
    res.encoding = 'utf-8'

    if res.status_code == 200:
        # print(res.content.decode('utf-8'))
        print(res.text)