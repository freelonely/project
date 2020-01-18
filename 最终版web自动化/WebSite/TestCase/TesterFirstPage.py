"""
-*- coding:utf-8 -*-
最终版web自动化
Author: Free
DataTime: 2020/1/16 15:49

"""

import unittest
from selenium import webdriver
from time import sleep
from WebSite.public.ReadConfig import readconfig


class FirstPage(unittest.TestCase):
    def setUp(self):
        self.b = webdriver.Chrome()
        url = readconfig('url', 'url')
        self.b.get(url)
        self.b.maximize_window()
        self.b.implicitly_wait(10)

    def test_pingtai(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[1]/dd[1]/a').click()
        sleep(3)
        assert self.b.current_url == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', '平台'

    def test_xieyi(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[1]/dd[2]/a').click()
        sleep(1)
        assert self.b.title == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', '协议'

    def test_tiaokuan(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[1]/dd[3]/a').click()
        sleep(1)
        assert self.b.title == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', '条款'

    def test_60kuangchi(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[2]/dd[1]/a').click()
        sleep(1)
        assert self.b.title == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', '矿池'

    def test_60zhiyuanzhe(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[2]/dd[2]/a').click()
        sleep(1)
        assert self.b.title == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', '志愿者'

    def test_feilv(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[3]/dd[1]/a').click()
        sleep(1)
        assert self.b.title == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', '费率说明'

    def test_newzhidao(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[3]/dd[2]/a').click()
        sleep(1)
        assert self.b.title == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', '新手指导'

    def test_apiwendang(self):
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div/dl[3]/dd[3]/a').click()
        sleep(1)
        assert self.b.title == '币君BJEX.CC | 全球最具潜力的加密资产投资平台', 'api文档'

    def tearDown(self) -> None:
        self.b.close()
        self.b.quit()
