#!/opt/anaconda3/envs python
# coding:utf-8
"""
Name : 3_Testassert.py
Author  : Martin
Contect : ziqguo@cisco.com
Time    : 2022/4/20 18:12
Desc:
"""
import unittest


class MyTestCase(unittest.TestCase):

    def test_1(self):
        a = 11
        b = 2 - 1

        self.assertEqual(a, b)
        self.assertNotEqual(a, b)
        self.assertTrue(a > 0, 'expect a > 0')

    def test_assertIn(self):
        x = 'py'
        y = 'python'
        self.assertIn(x, y)

    def myDiv(self, a, b):
        return a/b

    def test_assertRaise(self):
        self.assertRaises(ZeroDivisionError, self.myDiv, 3, 0)

    def test_assertListEqual(self):
        a = [1,2,3]
        b = [x for x in range(1,6)]
        self.assertListEqual(a,b)
        a = 11
        b = 2-1
        self.assertNotEqual(a,b,'ab not equal')

    def assertUserLegal(self, user):
        differ = None
        if user.get("id", 0) == 0:
            differ = "not 0"
        if differ is None:
            local_user = {'id': 13, 'name': 'admin'}
            if user.get('name', None)!= local_user['name']:
                differ = 'user name %s != %s'%(user.get('name', None), local_user['name'])
        if differ is not None:
            self.fail(differ)

    def test_assert_user(self):
        user = {'id': '1231', 'name': 'admin'}
        self.assertUserLegal(user)


if __name__ == '__main__':
    unittest.main()
