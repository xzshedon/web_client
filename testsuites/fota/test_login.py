#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.fota.login import Login

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_fota_login(self):
        fota_login = Login(self.driver)
        fota_login.type_user("zengyuzhou")
        fota_login.type_pwd("Test123")
        fota_login.login()