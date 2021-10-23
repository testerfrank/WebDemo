#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from base.basepage import BasePage
from common.readelement import ReadElement
from page.index.register_page import Register

login_element = ReadElement("login")


class Login(BasePage):
    """登录页面"""

    def scan_rc(self):
        """
        扫描二维码
        :return:企业微信首页
        """
        pass

    def goto_register(self):
        """
        点击企业注册
        :return: 注册页面
        """
        self.find_and_click(login_element["企业注册"])
        return Register(self._driver)



