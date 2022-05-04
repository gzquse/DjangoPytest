# -*- coding:utf-8 -*-
"""
模块描述:
执行器脚本
作者：Sniper.ZH
"""
import unittest
import os

# from HtmlTestRunner import HTMLTestRunner
from MyHTMLTestRunner import HTMLTestRunner

from MyTestCase1 import TestCase1
from MyTestCase2 import TestCase2
import MyTestCaseModule



# 测试套件和测试执行器
# 测试套件要写在单独的文件中

# 实例化一个测试套件
suite = unittest.TestSuite()
# 增加测试方法、测试用例
# 第一种方法:添加单个的测试方法
# suite.addTest(TestCase1("test_1"))
# suite.addTest(TestCase1("test_2"))
# suite.addTest(TestCase2("test_3"))
# suite.addTest(TestCase2("test_4"))

# 第二种方法：批量添加多个测试方法
# cases = [
#     TestCase1("test_1"),
#     TestCase1("test_2"),
#     TestCase2("test_3"),
#     TestCase2("test_4")
# ]
# # list tuple set
# # 推荐直接使用list []来组合我们的测试方法
# cases1 = [
#     TestCase1("test_1"),
#     TestCase1("test_2"),
#     TestCase1("test_3"),
#     TestCase2("test_2"),
#     TestCase2("test_3"),
#     TestCase2("test_4")
# ]
# suite.addTests(cases1)

# 第三种方法：按照测试用例的级别来添加
# TestLoader
# 等于执行unittest.main()
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase2))
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase1))
# suite.addTests(unittest.TestLoader().loadTestsFromName("MyTestCase1.TestCase1"))
# suite.addTests(unittest.TestLoader().loadTestsFromNames(["MyTestCase1.TestCase1", "MyTestCase2.TestCase2"]))
# suite.addTests(unittest.TestLoader().loadTestsFromModule(MyTestCaseModule))

# 实例化测试执行器
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 第四种方法：遍历目录，来获取所有的测试模块和测试方法
# 要指定一个目录
# module_path = "./"
# discorver = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="MyTest*.py")
# runner = unittest.TextTestRunner()  # 这也是一种测试报告
# runner.run(discorver)

# html文件
# 第一种：html-testrunner三方库
# pip install html-testrunner
# 如果你的环境是windows 要修改模板文件中的编码方式为gbk
# 需要找一个2.2.4版本的jquery库，重新修改js文件地址
# module_path = "./"
# discorver = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="MyTest*.py")
# runner = HTMLTestRunner(
#     output="htmlreports",
#     combine_reports=True,
#     report_title="测试报告的演示实例",
#     report_name="Unittest_report",
#     add_timestamp=False
# )
# runner.run(discorver)

# 第二种测试报告：HTMLTestRunner
# 个人开发的三方模块
# http://tungwaiyip.info/software/HTMLTestRunner.html
# 第94行： import StringIO 改为 import io
# 第539行：self.outputBuffer = StringIO.StringIO() 改为self.outputBuffer = io.BytesIO()
# 第642行：if not rmap.has_key(cls): 改为 if not cls in rmap:
# 第772行：ue = e.decode('latin-1') 改成 ue = e
# 第766行：uo = o.decode ('latin-1') 改成 uo=o
# 第768行：uo = o 改成 uo = o.decode('utf-8')
# 第774行：ue = e 改成 ue = e.decode('utf-8')
# 第631行：print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime) 改成 print('\nTime Elapsed: %s' % (self.stopTime-self.startTime),file=sys.stderr)
# 第118行：self.fp.write(s) 改为 self.fp.write(bytes(s,'UTF-8'))

report_path = "./reports/"
# report_file = report_path + "html_report.html"
report_file = report_path + "html_report_cust.html"

# 如果目录不存在，创建
if not os.path.exists(report_path):
    os.mkdir(report_path)
#
with open(report_file, "wb") as reportFile:
    module_path = "./"
    discorver = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="MyTest*.py")
    runner = HTMLTestRunner(title="演示测试报告", description="描述一下测试场景和环境", stream=reportFile)
    runner.run(discorver)

# 更多的html测试报告执行器，可以自定义或者去找资源

# module_path = "./"
# discover = unittest.defaultTestLoader.discover(start_dir=module_path, pattern="MyTest*.py")
# runner = HTMLTestRunner(output="htmlreports",
#                         combine_reports=True,
#                         add_timestamp=False,
#                         report_name="report test",
#                         report_title='demo of report')
# runner.run(discover)
