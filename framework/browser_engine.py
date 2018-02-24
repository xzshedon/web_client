#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger

# 打印浏览器控制log
logger = Logger(logger="BrowserEngine").getlog()

# 项目根目录下路径
base_path = os.path.dirname(os.path.abspath('.'))


class BrowserEngine(object):
    chrome_driver_path = base_path + '/tools/chromedriver.exe'

    # ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    # 通过config.ini确定使用那个浏览器, 并返回driver对象
    def open_browser(self, driver,conf):
        '''

        :param driver:
        :param conf: { "browserName":"Chrome","cookieData":"No","URL":"https://i.neffos.com/FOTA/to_imei"}
        :return:
        '''
        # config = ConfigParser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        # file_path = base_path + '/config/config.ini'
        # config.read(file_path)

        # browser = config.get("browserType", "browserName")
        browser = conf["browserName"]
        logger.info("You had select %s browser." % browser)
        # url = config.get("testServer", "URL")
        url = conf["URL"]
        logger.info("The test server url is: %s" % url)
        # userdata = config.get("browserUserData", "userdata")
        userdata = conf["cookieData"]
        logger.info("The userdata is :%s" % userdata)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            options = webdriver.ChromeOptions()
            if userdata != "No":
                options.add_argument(
                    "--user-data-dir=" + userdata)
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            # options.add_argument("--test-type", ["--ignore-certificate-errors"])
            driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=options)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
