#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import configparser

from config.conf import cm


class ReadConfig:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(cm.ini_file, encoding="utf-8")

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, "w", encoding="utf-8") as f:
            self.config.write(f)

    @property
    def dev_url(self):
        return self._get("environment", "dev_url")

    @property
    def main_url(self):
        return self._get("environment", "main_url")

    @property
    def baseline_url(self):
        return self._get("environment", "baseline_url")


ini = ReadConfig()
if __name__ == "__main__":
    print(ini.dev_url)
    print(ini.main_url)
    print(ini.baseline_url)
