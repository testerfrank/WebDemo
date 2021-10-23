#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from base.basepage import BasePage
from common.readelement import ReadElement

register_element = ReadElement("register")


class Register(BasePage):
    """企业注册页面"""

    def header_title_click(self):
        """点击【注册企业微信】"""
        self.find_and_click(register_element["注册企业微信"])

    def company_click(self):
        """
        点击【企业名称】输入框
        """
        self.find_and_click(register_element["企业名称"])

    def company_tips(self):
        """获取提示信息"""
        return self.get_text(register_element["企业名称输入提示"])

    def company_send(self, text):
        """【企业名称】输入文本"""
        self.find_and_send(register_element["企业名称"], text)

    def industry_text(self):
        """获取【行业类型】下拉框提示文本"""
        return self.get_text(register_element["行业类型"])

    def industry_select(self):
        """选择行业类型"""
        self.find_and_click(register_element["行业类型"])
        self.find_and_click(register_element["IT服务"])
        self.find_and_click(register_element["互联网和相关服务"])

    def company_size_text(self):
        """获取【员工规模】下拉框提示文本"""
        return self.get_text(register_element["员工规模"])

    def company_size_select(self):
        """选择员工规模"""
        self.find_and_click(register_element["员工规模"])
        self.find_and_click(register_element["101-200人"])

    def goto_help_center(self):
        """
        点击【帮助中心】按钮
        :return: 帮助中心
        """
        self.find_and_click(register_element["帮助中心"])
