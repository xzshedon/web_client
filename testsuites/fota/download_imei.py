#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.fota.manage_test_imei import ManageIMEI

class TestDownloadIMEI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        cls.config = {
            "browserName": "Chrome",
            "cookieData": "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data",
            "URL": "https://i.neffos.com/FOTA/to_imei",
            "downloaddir": "E:\\Users\\Administrator\\Documents\\Office\\download"
        }
        # config = {
        #     "browserName": "Firefox",
        #     "cookieData": "C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\mihzvroy.default",
        #     # "cookieData": "C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\Profiles\\rvizmnhc.selenium",
        #     # "cookieData":"",
        #     "URL": "https://i.neffos.com/FOTA/to_imei",
        #     "downloaddir": "E:\\Users\\Administrator\\Documents\\Office\\download"
        # }
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls,cls.config)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_download_file(self):
        manage_imei = ManageIMEI(self.driver)
        manage_imei.download_imei_template()





