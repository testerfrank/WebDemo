#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import datetime
import time
from functools import wraps


def timestamp():
    """时间戳"""
    return time.time()


def sleep(second=3):
    """休眠时间"""
    time.sleep(second)


def dt_strftime(fmt="%Y-%m-%d %H:%M:%S"):
    """格式化时间"""
    return datetime.datetime.now().strftime(fmt)


def run_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrappers(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("{}运行完成！耗时{}".format(func, timestamp() - start))
        return res

    return wrappers


if __name__ == "__main__":
    print(dt_strftime())
