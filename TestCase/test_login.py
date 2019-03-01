'''
登录页面测试用例
'''

import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
import ddt

from TestDatas import common_datas as CD
from TestDatas import login_datas as TD
import pytest
@ddt.ddt

@pytest.mark.login
class TestLogin(unittest.TestCase):
    @classmethod #修饰性，页面调用时不需要实例化
    def setUpClass(cls):
        #调用Google浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.login_url)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
    #用例1.登录成功
    #TD引入login_datas内的登录成功数据
    #通过pytest给测试用例加标签，可以重复加标签
    @pytest.mark.smoke
    def test_loogin_1_success(self):
        #调用登录类内的方法，并传参
        #对象调用类方法
        LoginPage(self.driver).login(TD.succ_data["user"],TD.succ_data["password"])
        #断言，通过首页元素断言登录是否成功
        self.assertTrue(IndexPage(self.driver).isExist_quitEle())

    #用例2：密码为空
    @ddt.data(*TD.datas)
    def test_login_0_errorDatas(self,data):
        #1.步骤：登录页面功能
        lp = LoginPage(self.driver)
        lp.login(data["user"],data["password"])
        #2.断言
        self.assertEqual(data["check"],lp.get_errorMsg_from_loginArea())#assertEqual通过实际给出的提示，与get_errorMsg_from_loginArea方法定位的提示是否一致，一致用例通过

    # #用例3：账户为空时
    # def test_login_noUser(self):
    #     lp = LoginPage(self.driver)
    #     lp.login('','python')
    #     self.assertEqual("请输入手机号",lp.get_errorMsg_from_loginArea())
    # #用例4：账户少于11位
    #     lp = LoginPage(self.driver)
    #     lp.login('186847', 'python')
    #     self.assertEqual("请输入正确手机号", lp.get_errorMsg_from_loginArea())