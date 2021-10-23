#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import signal
import subprocess
from typing import List

import allure
import pytest
from _pytest.config.argparsing import Parser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.edge.service import Service as ES
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.ie.service import Service as IS

from common.readconfig import ini
from config.conf import cm
from page.index.index_page import Index
from utils.times import sleep

_driver = None


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    """初始化浏览器"""
    global _driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = Options()
        # 无痕模式
        options.add_argument("incognito")
        # 无界面模式
        # options.add_argument("headless")
        # 允许自动化控制，且不提示
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 远程调试模式
        # options.debugger_address = "127.0.0.1:9222"
        service = CS(cm.CHROMEDIVER_PATH)
        _driver = webdriver.Chrome(options=options, service=service)
    elif browser == "firefox":
        service = FS(cm.GECKODRIVER_PATH)
        _driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = ES(cm.EDGEDRIVER_PATH)
        _driver = webdriver.Edge(service=service)
    elif browser == "ie":
        service = IS(cm.IEDIVER_PATH)
        _driver = webdriver.Ie(service=service)
    env = request.config.getoption("--env")
    if env == "dev":
        _driver.get(ini.dev_url)
    elif env == "main":
        _driver.get(ini.main_url)
    elif env == "baseline":
        _driver.get(ini.baseline_url)

    yield _driver
    sleep(5)
    _driver.quit()


@pytest.fixture(scope="function", autouse=True)
def index(browser):
    """初始化首页"""
    browser.maximize_window()
    index = Index(browser)
    return index


def pytest_addoption(parser: Parser):
    """添加命令行参数"""
    my_group = parser.getgroup("my_group")
    my_group.addoption("--env", action="store", default="dev", dest="env", help="设置运行环境，可选项：dev,main,baseline")
    my_group.addoption("--browser", action="store", default="chrome", dest="browser",
                       help="设置运行浏览器，可选项：chrome,firefox,edge,ie")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    # 倒序执行 items里面的测试用例
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """获取每个用例状态的钩子函数"""
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = "(%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        fail_picture()


def fail_picture():
    """截图"""
    file = cm.screenshot_file
    _driver.save_screenshot(cm.screenshot_file)
    allure.attach.file(file, "失败用例截图:{}".format(file), allure.attachment_type.PNG)

# 视频文件可以生成，但allure报告不展示视频附件，先注释，后续再研究
# @pytest.fixture(scope="function", autouse=True)
# def record():
#     """录屏"""
#     file = cm.screencap_file
#     cmd = f"ffmpeg -f gdigrab -i desktop {file}"
#     p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
#     yield file
#     p.stdin.write("q".encode(encoding="utf-8"))
#     sleep(3)
#     allure.attach.file(file, "用例视频:{}".format(file), allure.attachment_type.MP4)
