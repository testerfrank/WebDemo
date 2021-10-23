#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

from utils.times import dt_strftime


class ConfigManager:
    """项目目录管理"""
    # 项目目录
    BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_DIR = os.path.join(BASEDIR, "page_element")

    # 测试报告目录
    REPORT_DIR = os.path.join(BASEDIR, "report")

    # 测试数据目录
    TESTDATA_DIR = os.path.join(BASEDIR, "test_data")

    # 浏览器驱动目录
    DIVER_PATH = os.path.join(BASEDIR, "driver")

    # 谷歌浏览器驱动
    CHROMEDIVER_PATH = os.path.join(DIVER_PATH, "chromedriver.exe")

    # 火狐浏览器驱动
    GECKODRIVER_PATH = os.path.join(DIVER_PATH, "geckodriver.exe")

    # IE浏览器驱动
    IEDIVER_PATH = os.path.join(DIVER_PATH, "IEDriverServer.exe")

    # Edge浏览器驱动
    EDGEDRIVER_PATH = os.path.join(DIVER_PATH, "msedgedriver.exe")

    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(ConfigManager.BASEDIR, "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        logfile = os.path.join(log_dir, "{}.log".format(dt_strftime("%Y%m%d")))
        return logfile

    @property
    def screenshot_file(self):
        """错误截图目录"""
        screenshot_dir = os.path.join(ConfigManager.BASEDIR, "screenshot")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        now_time = dt_strftime("%Y%m%d%H%M%S")
        screeshotfile = os.path.join(screenshot_dir, "{}.png".format(now_time))
        return screeshotfile

    @property
    def screencap_file(self):
        """错误录屏目录"""
        screencap_dir = os.path.join(ConfigManager.BASEDIR, "screencap")
        if not os.path.exists(screencap_dir):
            os.makedirs(screencap_dir)
        now_time = dt_strftime("%Y%m%d%H%M%S")
        screencapfile = os.path.join(screencap_dir, "{}.mp4".format(now_time))
        return screencapfile

    @property
    def ini_file(self):
        """config.ini配置文件"""
        ini_file = os.path.join(ConfigManager.BASEDIR, "config", "config.ini")
        if not os.path.exists(ini_file):
            raise FileNotFoundError("{}配置文件不存在".format(ini_file))
        return ini_file


cm = ConfigManager()
if __name__ == "__main__":
    print("项目目录:{}".format(ConfigManager.BASEDIR))
    print("页面元素目录:{}".format(ConfigManager.ELEMENT_DIR))
    print("测试报告目录:{}".format(ConfigManager.REPORT_DIR))
    print("测试数据目录:{}".format(ConfigManager.TESTDATA_DIR))
