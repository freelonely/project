"""
-*- coding:utf-8 -*-
最终版web自动化
Author: Free
DataTime: 2020/1/10 18:32

"""
from WebSite.public.ReadConfig import readconfig
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains


class BiBiTest(unittest.TestCase):

    def setUp(self):
        self.b = webdriver.Chrome()
        url = readconfig('url', 'url')
        self.b.get(url)
        self.b.maximize_window()
        self.b.implicitly_wait(10)

    def codeBi(self):

        while True:
            sleep(1)
            self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[6]/button').click()
            sleep(2)
            element = self.b.find_element_by_xpath('//*[@id="mpanel1"]/div[2]/div/div')
            ActionChains(self.b).click_and_hold(on_element=element).perform()
            ActionChains(self.b).move_to_element_with_offset(to_element=element, xoffset=43,
                                                             yoffset=0).perform()
            sleep(0.8)
            ActionChains(self.b).release().perform()
            sleep(1)
            if self.b.current_url == 'http://staging.bjex2018.com:881/cn/#/login/':
                self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/img').click()
                continue
            else:
                break

    def test_bibi_login(self):
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[1]/div[1]').click()
        sleep(2)
        user = readconfig('login', 'user')
        password = readconfig('login', 'password')
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[4]/div/input').send_keys(
            user)
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[5]/div/input').send_keys(
            password)
        sleep(2)
        self.codeBi()
        sleep(1)
        assert self.b.find_element_by_xpath('/html/body/div[2]').text == "登录成功", '预期不一致登陆失败'

    def test_bibi_betray(self):
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[1]/div[1]').click()
        sleep(2)
        user = readconfig('login', 'user')
        password = readconfig('login', 'password')
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[4]/div/input').send_keys(
            user)
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[5]/div/input').send_keys(
            password)
        sleep(2)
        self.codeBi()
        sleep(1)
        # 币币交易按钮
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[6]/div/div[1]').click()
        # 交易对
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[1]/div').click()
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[1]/div[3]').click()
        sleep(2)
        # 输入框输入币
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[2]/input').send_keys('DCCB')
        sleep(3)
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[4]/div[27]').click()
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]').click()
        sleep(2)
        # 点击挂单中卖20号
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[1]/div[1]/div[4]/div[20]/div[2]').click()
        sleep(2)
        # 输入币的数量
        # self.b.find_element_by_xpath(
        #     '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[8]/input').send_keys('15')
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[9]/div/div[4]').click()
        sleep(2)
        # 点击卖
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div').click()
        sleep(2)
        self.assertIsNotNone(
            self.b.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[3]/div[2]/div[3]/table/tr[2]").text)

    def test_bibi_cancel(self):
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[1]/div[1]').click()
        sleep(2)
        user = readconfig('login', 'user')
        password = readconfig('login', 'password')
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[4]/div/input').send_keys(
            user)
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[5]/div/input').send_keys(
            password)
        sleep(2)
        self.codeBi()
        sleep(1)
        # 币币交易按钮
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[6]/div/div[1]').click()
        # 交易对
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[1]/div').click()
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[1]/div[3]').click()
        sleep(2)
        # 输入框输入币
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[2]/input').send_keys('DCCB')

        # js = 'window.scrollTo(0,document.body.scrollHeight)'
        # self.b.execute_script(js)
        sleep(3)
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[4]/div[28]/div[2]').click()
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]').click()
        sleep(2)
        # 点击挂单中卖20号
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[1]/div[1]/div[4]/div[20]/div[2]').click()
        sleep(2)
        # 输入币的数量
        # self.b.find_element_by_xpath(
        #     '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[8]/input').send_keys('15')
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[9]/div/div[4]').click()
        sleep(2)
        # 点击卖
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div').click()
        sleep(2)
        # 取消
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[2]/div[3]/table/tr[2]/td[9]/div').click()
        sleep(2)
        self.b.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[1]').click()
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[2]/div[3]/table/tr[2]/td[9]/div').click()
        sleep(2)
        self.b.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[2]/span').click()
        sleep(2)

        assert self.b.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[3]/div[2]/div[3]/table/tr[2]").text == '', '有数据，取消失败'

    def test_bibi_buy(self):
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[1]/div[1]').click()
        sleep(2)
        user = readconfig('login', 'user')
        password = readconfig('login', 'password')
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[4]/div/input').send_keys(
            user)
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[5]/div/input').send_keys(
            password)
        sleep(2)
        self.codeBi()
        sleep(1)
        # 币币交易按钮
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/ul/li[6]/div/div[1]').click()
        # 交易对
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[1]/div').click()
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[1]/div[3]').click()
        sleep(2)
        # 输入框输入币
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[2]/input').send_keys('DCCB')

        # js = 'window.scrollTo(0,document.body.scrollHeight)'
        # self.b.execute_script(js)
        sleep(3)
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[6]/div[4]/div[27]').click()
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]').click()
        sleep(2)
        # 点击挂单中卖20号
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[1]/div[1]/div[4]/div[20]/div[2]').click()
        sleep(2)
        # 输入币的数量
        # self.b.find_element_by_xpath(
        #     '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[8]/input').send_keys('15')
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.b.execute_script(js)
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[1]/div[9]/div/div[4]').click()
        sleep(2)
        # 点击卖
        self.b.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div').click()
        sleep(2)
        # 取消
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[2]/div[3]/table/tr[2]/td[9]/div').click()
        sleep(2)
        self.b.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[1]').click()
        sleep(2)
        self.b.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div/div[3]/div[2]/div[3]/table/tr[2]/td[9]/div').click()
        sleep(2)
        self.b.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button[2]/span').click()
        sleep(2)

    def tearDown(self) -> None:
        self.b.close()
        self.b.quit()
