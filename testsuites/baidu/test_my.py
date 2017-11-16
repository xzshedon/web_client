#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Webpage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(8)
        self.browser.get("http://www.baidu.com")

    def tearDown(self):
        self.browser.quit()

    def testBaidu(self):
        self.browser.find_element_by_id("kw").send_keys(u"淘宝")
        self.browser.find_element_by_id("su").submit()
        time.sleep(2)
        # result = EC.title_is(u'淘宝_百度搜索')(self.driver)
        # self.assertTrue(result)
        try:
            assert u"淘宝" in self.browser.title
            print "Test Pass"
        except Exception as e:
            print ("Test Fail.",format(e))


        '''在10秒内等待某个按钮被定位到，再去点击。
        就是每隔0.5秒内调用一下until里面的表达式或者方法函数，
        要么10秒内表达式执行成功，要么10秒后抛出超时异常。
        '''
        # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("某个按钮")).click()
        ''' 10秒钟等待浏览器弹出的对话框，如果出现，就点击确定按钮'''
        # WebDriverWait(chromedriver, 10).until(EC.alert_is_present()).accept()

if __name__=='__main__':
    unittest.main()