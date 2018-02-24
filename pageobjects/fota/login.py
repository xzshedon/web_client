#!/usr/bin/python
# -*- coding: UTF-8 -*-

from framework.base_page import BasePage

class Login(BasePage):
    user = "id=>username"
    pwd = "id=>password"
    submit_m = "xpath=>//*[@id='fm1']/section/div/input[3]"

    def type_user(self, text):
        self.type(self.user, text)

    def type_pwd(self,text):
        self.type(self.pwd,text)

    def login(self):
        self.click_to_otherpage(self.submit_m)
        self.sleep(4)
        self.get_windows_img()
        self.sleep(2)