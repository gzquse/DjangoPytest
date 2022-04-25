#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : test_skip.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/20 18:53
Desc:
"""
import unittest


class MyTestCase(unittest.TestCase):
    step = 100
    result = {'step': 100}

    # @unittest.skip('i just want to skip')
    def test_1(self):
        # self.step = 100
        print('do test 1')

    @unittest.skipIf(step == 200, 'skip if true')
    def test_2(self):
        if MyTestCase.result['step'] == 100:
            return
        print('do test 2')
        print(self.step)


if __name__ == '__main__':
    unittest.main()
