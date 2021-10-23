#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

import win32con
import win32gui
from _pytest import config
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config.conf import cm
from utils.logger import log
from utils.times import sleep


class BasePage:
    """基类"""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

    def get_url(self, url):
        """
        打开网址
        """
        self._driver.maximize_window()
        try:
            self._driver.get(url)
            self._driver.implicitly_wait(60)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开{}超时，请检查网络或者链接网址是否可用！".format(url))

    def wait_for_element(self, locator):
        """显示等待"""
        log.info(f"wait_for_element: {locator}")
        WebDriverWait(self._driver, 10).until(lambda x: x.find_element(*locator))

    def condition(self, locator):
        """
        为了等待A元素，可以先判断点击A元素后返回的页面元素B是否可点击,locator为B元素
        """
        element_len = len(self.finds(locator))
        if element_len <= 0:
            self.find_and_click(locator)
        return element_len > 0

    def wait_for_condition(self, condition):
        """等待元素"""
        log.info("等待元素")
        WebDriverWait(self._driver, 10).until(condition)

    def find(self, locator):
        """
        查找单个元素
        """
        log.info(f"查找元素:{locator}")
        element = self._driver.find_element(*locator)
        self.high_light_element(element)
        return element

    def finds(self, locator):
        """
        查找一组元素
        """
        log.info(f"查找元素:{locator}")
        return self._driver.find_elements(*locator)

    def find_and_click(self, locator):
        """点击元素"""
        log.info(f"查找并点击:{locator}")
        self.find(locator).click()

    def find_and_send(self, locator, txt):
        """输入文本"""
        log.info(f"查找并输入文本:{locator},{txt}")
        self.find(locator).send_keys(txt)

    def find_and_clear(self, locator):
        """清空文本"""
        log.info(f"查找并清空文本:{locator}")
        self.find(locator).clear()

    def move_to_element(self, locator):
        """鼠标悬停在某个元素上"""
        log.info(f"鼠标悬停:{locator}")
        ActionChains(self._driver).move_to_element(self.find(*locator)).perform()

    def drag_and_drop(self, locator1, locator2):
        """拖动元素"""
        log.info(f"拖动元素:source:{locator1},target:{locator2}")
        ActionChains(self._driver).drag_and_drop(self.find(locator1), self.find(locator2)).perform()

    def get_text(self, locator):
        """获取元素文本"""
        _text = self.find(locator).text
        log.info(f"获取文本:{locator}:{_text}")
        return _text

    @property
    def current_window_handle(self):
        """获取当前窗口句柄"""
        current_handle = self._driver.current_window_handle
        log.info(f"当前窗口句柄:{current_handle}")
        return current_handle

    @property
    def window_handles(self):
        """获取浏览器所有窗口句柄"""
        handles = self._driver.window_handles
        log.info(f"浏览器所有窗口句柄:{handles}")
        return handles

    def switch_window(self, handle):
        """切换窗口句柄"""
        log.info(f"切换窗口句柄:{handle}")
        self._driver.switch_to.window(handle)

    def switch_frame(self, frame_id):
        """切换frame"""
        log.info(f"切换frame:{frame_id}")
        self._driver.switch_to.frame(frame_id)

    def switch_default_content(self):
        """切换到主页面"""
        log.info("切换到主页面")
        self._driver.switch_to.default_content()

    def switch_parent_frame(self):
        """切换到上一层frame"""
        log.info("切换到上一层frame")
        self._driver.switch_to.parent_frame()

    def alert_text(self):
        """获取alert弹窗的文本"""
        text = self._driver.switch_to.alert.text
        log.info(f"获取弹窗文本:{text}")
        return text

    def alert_send(self, text):
        """弹窗中输入文本"""
        log.info(f"弹窗中输入文本:{text}")
        self._driver.switch_to.alert.send_keys(text)

    def alert_accept(self):
        """确认弹窗"""
        log.info("确认弹窗")
        self._driver.switch_to.alert.accept()

    def alert_dismiss(self):
        """取消弹窗"""
        log.info("取消弹窗")
        self._driver.switch_to.alert.dismiss()

    @property
    def title(self):
        """获取浏览器窗口标签名"""
        _title = self._driver.title
        log.info()
        return _title

    @property
    def current_url(self):
        """获取当前窗口url"""
        _current_url = self._driver.current_url
        log.info(f"当前窗口url:{_current_url}")
        return _current_url

    @property
    def page_source(self):
        """获取网页资源"""
        return self._driver.page_source

    def back(self):
        """浏览器窗口回退"""
        log.info("浏览器窗口回退")
        self._driver.back()

    def forward(self):
        """浏览器窗口前进"""
        log.info("浏览器窗口前进")
        self._driver.forward()

    def refresh(self):
        """刷新页面"""
        log.info("刷新页面")
        self._driver.refresh()

    def close(self):
        """关闭页签"""
        log.info("关闭页签")
        self._driver.close()

    def quit(self):
        """退出浏览器"""
        log.info("退出浏览器")
        self._driver.quit()

    def select_option(self, locator):
        """获取下拉框所有选项"""
        options = Select(self.find(locator)).options
        log.info(f"获取下拉框所有选项:{options}")
        return options

    def select_all_selected_options(self, locator):
        """获取下拉框所有已选选项"""
        options = Select(self.find(locator)).all_selected_options
        log.info(f"获取下拉框所有已选选项:{options}")
        return options

    def select_by_index(self, locator, index):
        """选中选项"""
        log.info(f"选中选项:{index}")
        Select(self.find(locator)).select_by_index(index)

    def select_by_value(self, locator, value):
        """选中选项"""
        log.info(f"选中选项:{value}")
        Select(self.find(locator)).select_by_value(value)

    def select_by_text(self, locator, text):
        log.info(f"选中选项:{text}")
        Select(self.find(locator)).select_by_visible_text(text)

    def select_deselect_by_index(self, locator, index):
        """取消选项"""
        log.info(f"取消选项:{index}")
        Select(self.find(locator)).deselect_by_index(index)

    def select_deselect_by_value(self, locator, value):
        """取消选项"""
        log.info(f"取消选项:{value}")
        Select(self.find(locator)).deselect_by_value(value)

    def select_deselect_by_text(self, locator, text):
        """取消选项"""
        log.info(f"取消选项:{text}")
        Select(self.find(locator)).deselect_by_value(text)

    def select_deselect_all(self, locator):
        """取消所有选项"""
        log.info(f"取消所有选项")
        Select(self.find(locator)).deselect_all()

    def upload_file(self, locator, file_path):
        """非input标签的文件上传"""
        log.info("文件上传")
        self.find_and_click(locator)
        sleep(2)
        # 一级顶层窗口
        dialog = win32gui.FindWindow("#32770", "打开")
        # 二级窗口
        comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, "ComboBox", None)
        # 四级窗口 -- 文件路径输入区域
        edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)
        # 二级窗口 -- 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)
        # 1、输入文件路径
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        # 2、点击打开按钮
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    def screenshot(self):
        """截图"""
        log.info("截图")
        self._driver.save_screenshot(cm.screenshot_file)

    def js(self, js, *args):
        """执行JavaScript脚本"""
        log.info(f"执行JavaScript脚本:{js}")
        self._driver.execute_script(js, *args)

    def scroll(self, x, y):
        """滚动页面"""
        log.info(f"滚动页面:{x},{y}")
        self.js(f"window.scrollTo({x},{y})")

    def scroll_element(self, locator):
        """滚动查找元素"""
        log.info(f"滚动查找元素:{locator}")
        element = self.find(locator)
        self.js("arguments[0].scrollIntoView();", element)

    def display_element(self, locator):
        """显示隐藏的元素"""
        log.info(f"显示隐藏元素:{locator}")
        self.js(f'document.getElementById({locator}).style.display="block";')

    def high_light_element(self, element):
        """高亮显示正在操作的页面元素"""
        self.js("arguments[0].setAttribute('style',arguments[1]);", element,
                "border:2px solid red;")
        log.info(f"高亮显示正在操作的页面元素:{element}")
