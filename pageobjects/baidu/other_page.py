# -*- coding: utf-8 -*-

from framework.base_page import BasePage


class otherPage(BasePage):

    def click_anything(self):
        self.click("xpath=>/html/body/div[4]/div[2]/div/div[2]/div[7]/div/div/ol/li[1]/span[2]/a")
        self.sleep(2)
