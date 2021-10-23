#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from base.basepage import BasePage
from common.readelement import ReadElement
from page.index.login_page import Login
from page.index.register_page import Register

index_element = ReadElement("index")


class Index(BasePage):
    """index页面"""

    def goto_login(self):
        """
        点击登录按钮
        :return: 登录页面
        """
        self.find_and_click(index_element["登录"])
        return Login(self._driver)

    def goto_register(self):
        """
        点击注册按钮
        :return: 注册页面
        """
        self.find_and_click(index_element["注册"])
        return Register(self._driver)

    def goto_help_guide(self):
        """
        点击【使用手册】
        :return: 使用手册
        """
        self.find_and_click(index_element["使用手册"])



