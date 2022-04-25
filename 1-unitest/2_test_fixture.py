#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : 2_test_fixture.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/20 18:03
Desc:
"""
import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("-----setupClas----")
        cls.mysql_conn = '127.0.0.1:3306:demo'
        print("ooen database")

    @classmethod
    def tearDownClass(cls) -> None:
        print("----teardownClass------")

    def setUp(self) -> None:
        self.file = '/var/json'
        print('-----setup-----')

    def tearDown(self) -> None:
        print('-----teardown-----')

    def test_1(self):
        print(self.file)
        print('do test 1')


if __name__ == '__main__':
   unittest.main()
