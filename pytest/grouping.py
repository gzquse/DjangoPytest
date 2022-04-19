#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : grouping.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/14 17:23
Desc:
"""


class TestClass:
    def Test_one(self):
        x = 'martin'
        assert 'r' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, "check")