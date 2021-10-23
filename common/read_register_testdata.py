#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

import yaml

from config.conf import cm


class RegisterTestData:
    def __init__(self, name):
        self.filename = "{}.yaml".format(name)
        self.file = os.path.join(cm.TESTDATA_DIR, self.filename)
        if not os.path.exists(self.file):
            raise FileNotFoundError("{}.yaml文件不存在！".format(self.filename))
        with open(self.file, encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        data = self.data.get(item)
        return data


if __name__ == "__main__":
    testdata = RegisterTestData("testdata_register")
    print(testdata["企业名称"])
