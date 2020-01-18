"""
-*- coding:utf-8 -*-
最终版web自动化
Author: Free
DataTime: 2020/1/10 16:26
TODO 开始运行的执行通道
在此运行所有用例

"""

import unittest
import time
import HTMLTestRunnerCN

report_dir = './TestReport'
test_dir = './TestCase'

print('开始执行用例')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='Tester*.py')  # TODO 填写需要测试的类名
suite = unittest.TestSuite()
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + '测试报告.html'

print('生成报告中。。。')
suite.addTest(discover)
f = open(report_name, 'wb')  # wb 二进制文件的写操作
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f, title='币君测试报告', description='PC端')
runner.run(suite)
