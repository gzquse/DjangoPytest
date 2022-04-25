# -*- coding:utf-8 -*-
"""
模块描述:

作者：Sniper.ZH
"""
import unittest


class TestCase1(unittest.TestCase):

    def test_1(self):
        print("TestCase1 test_1")

    def test_2(self):
        print("TestCase1 test_2")

    def test_3(self):
        print("TestCase1 test_3")
        a = 1
        b = 2
        self.assertEqual(a, b)

    def test_4(self):
        print("TestCase1 test_4")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestCase1("test_1"))
    suite.addTest(TestCase1("test_2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
