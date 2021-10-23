#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import allure
import pytest

from page.index.index_page import Index


class TestIndex:
    """测试Index页面"""

    @allure.epic("【企业微信首页】")
    @allure.feature("企业登录")
    @allure.story("企业登录")
    @allure.title("企业登录")
    def test_goto_login(self, index: Index):
        """测试【企业登录】按钮"""
        index.goto_login()
        current_url = index.current_url
        assert current_url == "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"

    @allure.epic("【企业微信首页】")
    @allure.feature("立即注册")
    @allure.story("立即注册")
    @allure.title("立即注册")
    def test_goto_register(self, index: Index):
        """测试【立即注册】按钮"""
        index.goto_register()
        current_url = index.current_url
        assert current_url == "https://work.weixin.qq.com/wework_admin/register_wx?from=myhome"

    @allure.epic("【企业微信首页】")
    @allure.feature("底部导航栏")
    @allure.story("使用手册")
    @allure.title("使用手册")
    def test_goto_help_guide(self, index: Index):
        index.goto_help_guide()
        assert True


if __name__ == '__main__':
    pytest.main(['test_case/test_index.py'])
