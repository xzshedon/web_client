#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger

# create a logger instance
logger_instance = Logger(logger="BasePage")
logger = logger_instance.getlog()
report_dir = logger_instance.report_path()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器，结束测试
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        保存窗口图片到\test_reports下
        """
        screen_name = report_dir + '/screenshot.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to report folder")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        """
         根据=>来切割字符串
        :param selector:
        :return: element
        """
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        try:
            if selector_by == "i" or selector_by == 'id':
                element = self.driver.find_element_by_id(selector_value)
            elif selector_by == "n" or selector_by == 'name':
                element = self.driver.find_element_by_name(selector_value)
            elif selector_by == "c" or selector_by == 'class_name':
                element = self.driver.find_element_by_class_name(selector_value)
            elif selector_by == "l" or selector_by == 'link_text':
                element = self.driver.find_element_by_link_text(selector_value)
            elif selector_by == "p" or selector_by == 'partial_link_text':
                element = self.driver.find_element_by_partial_link_text(selector_value)
            elif selector_by == "t" or selector_by == 'tag_name':
                element = self.driver.find_element_by_tag_name(selector_value)
            elif selector_by == "x" or selector_by == 'xpath':
                element = self.driver.find_element_by_xpath(selector_value)
            elif selector_by == "css" or selector_by == 'css_selector':
                element = self.driver.find_element_by_css_selector(selector_value)
            else:
                raise NameError("Please enter a valid type of targeting elements.")
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()
            return None

        return element

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            logger.info("The element \' %s \' will be clicked." % el.get_attribute("value"))
            el.click()
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 点击元素跳转到新的页面，返回新页面的driver
    def click_to_otherpage(self, selector):
        handles = self.driver.window_handles
        self.click(selector)
        for handle in self.driver.window_handles:
            if not handle in handles:
                self.driver.switch_to_window(handle)
        return self.driver

    # 或者网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    def assert_True(self,expr, msg=None):
        if expr is False:
            logger.warning("assertion failed! ")
            raise AssertionError(msg)

    def assert_IsNotNone(self, obj, msg=None):
        ele  = self.find_element(obj)
        if ele is None:
            logger.warning("assertion failed! ")
            raise AssertionError(msg)

    def assert_False(self,expr, msg=None):
        if expr is True:
            logger.warning("assertion failed! ")
            raise AssertionError(msg)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        logger.info(alert.text.replace("\n",""))
        alertlog = alert.text
        alert.accept()
        return alertlog