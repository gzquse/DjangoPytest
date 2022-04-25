#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : ddt_1.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/21 14:34
Desc:
"""
import json
import unittest

import ddt
import yaml


def read_phones_txt(file_name):
    ret = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            ret.append(line.strip('\n'))
    return ret


def read_json(file_name):
    return json.load(open(file_name, 'r'))


def read_yaml(file_name):
    return yaml.load(open(file_name, 'r'), yaml.FullLoader)


@ddt.ddt
class FileTestCase(unittest.TestCase):

    @ddt.data(*read_phones_txt("datas/phones.txt"))
    @unittest.skip
    def test_1(self, phone):
        """mock a test"""
        # user = "admin"
        # passwd = "123456"
        #
        # ret = 'login success'
        # self.assertEqual('login success', ret)
        print(f"#使用手机号{phone}进行注册")

    # @ddt.data(*read_phones_txt("datas/userdatas.txt"))
    @ddt.file_data('datas/userdatas.yaml')
    def test_1(self, **kwargs):
        username = kwargs.get('name')
        print(username)
        """mock a test"""
        # user = "admin"
        # passwd = "123456"
        #
        # ret = 'login success'
        # self.assertEqual('login success', ret)
        # print(f"#使用手机号{}进行注册")
        # print(f'user: {username}, passwd: {password}')
        # print(f'kwargs: {kwargs["name"]}')


if __name__ == '__main__':
    unittest.main()
