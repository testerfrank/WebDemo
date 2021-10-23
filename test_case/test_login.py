#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import allure
import pytest

from page.index.index_page import Index


class TestLogin:
    """测试Login页面"""

    @allure.epic("【登录页面】")
    @allure.feature("企业注册")
    @allure.story("企业注册")
    @allure.title("企业注册")
    def test_goto_register(self, index: Index):
        """测试【企业注册】按钮"""
        index.goto_login().goto_register()
        current = index.current_url
        assert current == "https://work.weixin.qq.com/wework_admin/register_wx?from=myhome"


if __name__ == '__main__':
    pytest.main(['test_case/test_login.py'])
