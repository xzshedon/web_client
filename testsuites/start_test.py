#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os
import time

from framework import HTMLTestRunner
from testsuites.fota.test_login import TestLogin
from testsuites.fota.download_imei import TestDownloadIMEI
from testsuites.fota.test_delete_imei import TestDeleteIMEI

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_reports/' + now

# 设置报告名称格式
HtmlFile = report_path + "/report.html"
fp = file(HtmlFile, "wb")

suite = unittest.TestSuite()
# suite.addTest(TestSearch('test_baidu_search'))
# suite.addTest(TestUploadIMEI('test_upload_file'))
suite.addTest(TestDeleteIMEI('test_delete_imei'))
# suite.addTest(TestDownloadIMEI('test_download_file'))
# suite.addTest(GetPageTitle('test_get_title'))

# 构建suite
# suite = unittest.TestSuite(unittest.makeSuite(TestSearch))
#suite(unittest.makeSuite(GetPageTitle))

# suite = unittest.TestLoader().discover("testsuites")

if __name__== '__main__':
    # 执行用例
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)