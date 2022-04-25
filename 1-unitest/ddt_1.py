#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : ddt_1.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/21 14:34
Desc:
"""
import unittest

import ddt


@ddt.ddt
class LoginTestCase(unittest.TestCase):

    @ddt.data("123456")
    def test_1(self, phone):
        """mock a test"""
        # user = "admin"
        # passwd = "123456"
        #
        # ret = 'login success'
        # self.assertEqual('login success', ret)
        print(f"#使用手机号{phone}进行注册")

    @ddt.data(['admin', '123456'], ['martin', '12345'])
    @ddt.unpack
    def test_2(self, username, password):
        print(f'username: {username}, password: {password}')


if __name__ == '__main__':
    unittest.main()
