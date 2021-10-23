#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging

from config.conf import cm


class Log:
    def __init__(self):
        # 创建日志对象
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            # 创建handler写入文件
            fh = logging.FileHandler(cm.log_file, encoding="utf-8")
            fh.setLevel(logging.INFO)
            # 创建handler输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            # 定义日志格式
            formatter = logging.Formatter(self.fmt)
            # 给handler绑定日志格式
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            # 给日志对象添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return "%(asctime)s\t%(levelname)s\t%(filename)s:[%(funcName)s:%(lineno)d]\t%(message)s"


log = Log().logger
if __name__ == "__main__":
    log.info("hello world")
