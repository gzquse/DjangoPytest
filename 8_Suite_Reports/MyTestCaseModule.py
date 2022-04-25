# -*- coding:utf-8 -*-
"""
模块描述:

作者：Sniper.ZH
"""
import unittest


class TestCase3(unittest.TestCase):

    def test_1(self):
        print("TestCase3 test_1")

    def test_2(self):
        print("TestCase3 test_2")

    def test_3(self):
        print("TestCase3 test_3")
        a = 10
        b = 0
        print(a/b)

    def test_4(self):
        print("TestCase3 test_4")


class TestCase4(unittest.TestCase):

    def test_1(self):
        print("TestCase4 test_1")
        a = 1
        b = 2
        self.assertEqual(a, b)

    def test_2(self):
        print("TestCase4 test_2")

    def test_3(self):
        print("TestCase4 test_3")

    def test_4(self):
        print("TestCase4 test_4")


if __name__ == '__main__':
    unittest.main()
