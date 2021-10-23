#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import subprocess
import sys


def main():
    """主函数"""
    WIN = sys.platform.startswith("win")
    steps = [
        r"venv\Scripts\activate" if WIN else "source venv/bin/activate",
        r"pytest --alluredir report\allure-results --clean-alluredir",
        r"allure generate report\allure-results -c -o report\allure-report",
        # r"allure open report\allure-report"
    ]
    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == "__main__":
    main()
