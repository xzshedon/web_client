#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.fota.manage_test_imei import ManageIMEI


class TestDeleteIMEI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        config = {
            "browserName": "Chrome",
            "cookieData": "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data",
            "URL": "https://i.neffos.com/FOTA/to_imei",
            "downloaddir": "E:\\Users\\Administrator\\Documents\\Office\\download"
        }
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls, config)

    def tearDown(self):
        self.driver.quit()

    def test_delete_imei(self):
        manage_imei = ManageIMEI(self.driver)
        res = manage_imei.delete_imei("123456789012345")
        manage_imei.assert_True(res)


