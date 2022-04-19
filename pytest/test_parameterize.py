#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : test_parameterize.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/14 17:32
Desc:
"""
import pytest


@pytest.mark.parametrize("x,y,z", [(10, 20, 200), (20, 40, 200)])
def test_method(x, y, z):
    assert x*y == z