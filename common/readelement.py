#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

import yaml

from config.conf import cm


class ReadElement:
    def __init__(self, name):
        self.filename = "{}.yaml".format(name)
        self.element_path = os.path.join(cm.ELEMENT_DIR, self.filename)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("{}.yaml文件不存在！".format(self.filename))
        with open(self.element_path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        data = self.data.get(item)
        if data:
            name, value = data["by"], data["value"]
            return name, value
        raise ArithmeticError("{}中不存在关键字:{}".format(self.filename, item))


if __name__ == "__main__":
    index = ReadElement("index")
    print(index.data)
    print(index["登录"])
