#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : test1.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/19 17:28
Desc:
"""

import unittest


class MyTestCase(unittest.TestCase):

    def test_0(self):
        print("do test 0")

    def test_1(self):
        print("do test 1")

    def test_2(self):
        print("do test 2")

    def test_3(self):
        print("do test 3")

    def testMethod(self):
        print("do test")


if __name__ == '__main__':
    unittest.main()