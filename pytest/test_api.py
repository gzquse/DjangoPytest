#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : test_api.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/14 17:38
Desc:
"""
import json

import requests


main_url = "https://reqres.in"


def test_valid_login():
    url = main_url + "/api/login/"
    data = {
        "email": "eve.holssst@reqres.in",
        "password": "cityslicka"
    }
    res = requests.get(url, data=data)
    token = json.loads(res.text)
    assert res.status_code == 200
    assert token['page'] == 1
