#!/usr/bin/python
# -*- coding: UTF-8 -*-

from framework.base_page import BasePage

class Login(BasePage):
    user = "id=>username"
    pwd = "id=>password"
    submit_m = "xpath=>//*[@id='fm1']/section/div/input[3]"
    fota_enter = "xpath=>/html/body/div[2]/div[3]/div/div[1]/div[2]"

    def type_user(self, text):
        self.type(self.user, text)

    def type_pwd(self,text):
        self.type(self.pwd,text)

    def login(self):
        self.click_to_otherpage(self.submit_m)
        self.sleep(4)
        self.get_windows_img()
        self.sleep(2)
        re = self.find_element(self.fota_enter)
        return False if re is None else True
