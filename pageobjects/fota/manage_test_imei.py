#!/usr/bin/python
# -*- coding: UTF-8 -*-

from framework.base_page import BasePage

class ManageIMEI(BasePage):
    add = "id=>button_add"
    file = "xpath=>/html/body/div[2]/form/div[4]/div[2]/input"
    imeiGroup = "xpath=>/html/body/div[2]/form/div[2]/div[2]/input"
    submit = "xpath=>/html/body/div[2]/form/div[5]/div[1]/div"
    submit_m = "xpath=>//*[@id='fm1']/section/div/input[3]"
    imei_template_download = "xpath=>/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[3]/a"
    item_input = "id=>select_project_name"
    item_search = "xpath=>/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/button"
    batch_delete_imei = "id=>button_delAll"
    imei_input = "id=>imeiInput"
    imei_search = "xpath=>/html/body/div[5]/div[2]/div[2]/div[3]/div"
    delete_all = "xpath=>/html/body/div[5]/div[2]/div[3]/div[2]/div[1]/span[2]"

    def upload(self,name,file):
        self.click(self.submit_m)
        self.sleep(4)
        self.click(self.add)
        self.sleep(2)
        self.type(self.imeiGroup,name)
        self.type(self.file,file)
        self.click(self.submit)
        self.sleep(5)
        alert = self.accept_alert()
        self.sleep(4)
        if alert.startswith(u"本次 IMEI 去重后成功添加"):
            return True
        else:
            return False


    def download_imei_template(self):
        self.click(self.submit_m)
        self.sleep(4)
        self.click(self.imei_template_download)
        self.sleep(10)

    def search_imei_set(self,project):
        self.type(self.item_input,project)
        self.click(self.item_search)

    def delete_imei(self,imei):
        self.click(self.submit_m)
        self.click(self.batch_delete_imei)
        self.sleep(5)
        self.type(self.imei_input,imei)
        self.sleep(5)
        self.click(self.imei_search)
        self.click(self.delete_all)
        res = self.accept_alert()
        if res.startswith("批量删除IMEI成功"):
            return True
        else:
            return False

