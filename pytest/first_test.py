#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : first_test.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/14 17:15
Desc:
"""
import pytest


# @pytest.mark.one
def test_method1():
    x = 5
    y = 10
    assert x == y


# @pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b

# if __name__ == '__main__':
#     print("hello")
