#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : test_fixtrue.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/14 17:29
Desc:
"""
import pytest


@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]


@pytest.mark.xfail
def test_method(numbers):
    x = 15
    assert numbers[0] == x


@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert numbers[1] == y


def test_method3(numbers):
    z = 25
    assert numbers[2] == z