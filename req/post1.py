#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : post1.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/5 19:09
Desc:
"""
import requests

login_url = "http://127.0.0.1:8001/dologin/"

params = {
    'username': 'admin',
    'pwd': '123456',
    'randomCode': '0372',
}
session = requests.session()
res = session.post(login_url, data=params)
# cookies = res.cookies
if res.status_code == 200 and res.json()['code'] == 0:
    print(res.text)

    apply_url =  'http://127.0.0.1:8001/commit_order/'
    params = {
        'order_dep': '001',
        'order_date': '2022-04-05',
        'order_name': '555',
        'order_sys': '111',
        'order_type': 'new',
        'order_desc': '123',
    }

    res = session.post(apply_url, data=params,)
    res.encoding = 'utf-8'
    print(res.text)