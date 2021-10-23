#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import allure
import pytest
from pytest_assume.plugin import assume

from common.read_register_testdata import RegisterTestData
from page.index.index_page import Index
from utils.logger import log

testdata_register = RegisterTestData("testdata_register")


class TestRegister:
    """测试企业注册页面"""

    @allure.epic("【企业微信注册】")
    @allure.feature("注册表单")
    @allure.story("企业名称")
    @allure.title("输入框点击提示")
    def test_company_name(self, index: Index):
        """
        测试【企业名称】输入框点击提示
        1.点击输入框，验证提示信息
        2.点击【注册企业微信】，再次验证提示信息
        """
        register = index.goto_register()
        register.company_click()
        tips = register.company_tips()
        assume(tips == "填写企业、政府或组织名称")
        register.header_title_click()
        tips = register.company_tips()
        assume(tips == "由1-30个中文、英文、数字及合法字符组成")

    @allure.epic("【企业微信注册】")
    @allure.feature("注册表单")
    @allure.story("企业名称")
    @allure.title("输入框输入提示")
    @pytest.mark.parametrize("text", testdata_register["企业名称"])
    def test_company_name002(self, index: Index, text):
        """
        测试【企业名称】输入框输入提示
        1.有效等价类：字符数1-30个，中文、英文、数字、特殊符号、中文+英文+数字+特殊符号
        2.边界值：0，1，2，29，30，31
        3.无效等价类：字符数超过30个
        问题：中文+特殊字符且字符数1-30个，也不满足
        """
        register = index.goto_register()
        register.company_send(text)
        register.header_title_click()
        text = str(text).strip()
        if 1 <= len(text) <= 30:
            tips = register.company_tips()
            assume(tips == "填写企业、政府或组织名称")
        else:
            tips = register.company_tips()
            assume(tips == "由1-30个中文、英文、数字及合法字符组成")

    @allure.epic("【企业微信注册】")
    @allure.feature("注册表单")
    @allure.story("行业类型")
    @allure.title("行业类型")
    def test_industry(self, index: Index):
        """
        测试【行业类型】
        1.验证【行业类型】默认文本显示
        2.选择行业类型后，【行业类型】文本显示
        """
        register = index.goto_register()
        text = register.industry_text()
        assume(text == "选择行业类型")
        register.industry_select()
        text = register.industry_text()
        assume(text == "IT服务 互联网和相关服务")

    @allure.epic("【企业微信注册】")
    @allure.feature("注册表单")
    @allure.story("员工规模")
    @allure.title("员工规模")
    def test_company_size(self, index: Index):
        """
        测试【员工规模】
        1.验证【员工规模】默认文本显示
        2.选择行业类型后，【员工规模】文本显示
        """
        register = index.goto_register()
        text = register.company_size_text()
        assume(text == "选择员工规模")
        register.company_size_select()
        text = register.company_size_text()
        assume(text == "101-200人")

    @allure.epic("【企业微信注册】")
    @allure.feature("注册表单")
    @allure.story("管理员姓名")
    @allure.title("管理员姓名")
    def test_admin_name(self, index: Index):
        """测试【管理员姓名】"""
        pass


if __name__ == '__main__':
    pytest.main(["test_case/test_register.py"])
