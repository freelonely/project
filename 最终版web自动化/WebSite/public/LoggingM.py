"""
-*- coding:utf-8 -*-
最终版web自动化
Author: Free
DataTime: 2020/1/10 19:03

"""

import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler


class LoggingMethod(object):
    def __init__(self, name):
        # 将日志输出到文件
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        self.logger = logging.getLogger(name)  # 实例化logger对象
        self.logger.setLevel(logging.DEBUG)
        # 创建filehandler
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        filename = os.path.dirname(os.path.abspath('.')) + '\\Log\\' + now + '-' + name + '.log'
        fh = TimedRotatingFileHandler(filename, when='S', encoding="utf-8")
        # fh = logging.FileHandler(filename, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s'))
        self.logger.addHandler(fh)

    def getlogger(self):
        return self.logger


if __name__ == '__main__':
    logger = LoggingMethod(__name__).getlogger()
    logger.info('这是test_login 中的init方法')
