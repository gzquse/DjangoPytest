#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : test_runner.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/25 09:00
Desc:
"""
import unittest

from testCase1 import MyTestCase
from testCase2 import MyTestCase2

suite = unittest.TestSuite()
suite.addTest(MyTestCase2("test_2"))
suite.addTest(MyTestCase("test_1"))

# cases = [
#     MyTestCase("test_0"),
#     MyTestCase("test_3"),
#     MyTestCase2("test_2"),
#     MyTestCase2("test_3"),
#
# ]
#
# suite.addTests(cases)
#

# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
# suite.addTests(unittest.TestLoader().loadTestsFromNames(['testCase1.MyTestCase']))
# suite.addTests(unittest.TestLoader().loadTestsFromModule(testCase2))
# module_path = './'
# suite = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="testCasdadadadadase*")

runner = unittest.TextTestRunner()
runner.run(suite)
