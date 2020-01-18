"""
-*- coding:utf-8 -*-
最终版web自动化
Author: Free
DataTime: 2020/1/18 10:21

"""

import configparser
import os


def readconfig(tagname, name):
    cf = configparser.ConfigParser()
    cfpath = os.path.dirname(os.path.abspath('.')) + '\\config\\config.ini'
    cf.read(cfpath)
    res_name = cf.get(tagname, name)
    return res_name


