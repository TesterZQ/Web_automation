# -*- coding:utf-8 -*-
#@Time      :15:37
#@Auther    :ZhangQiang
#@Name      :conftest.py
import pytest
import py
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage

from TestDatas import common_datas as CD
from TestDatas import login_datas as TD
import pytest
'''
定义：
1.函数名称前面加pytest.fixture    #scope决定作用域，默认是function(函数)
2.前置后置的区分“yield”

调用：测试类或者测试用例当中，主动通过 fixture的函数名称 来调用fixture
      不需要再测试文件中引用

2.测试用例如何接收fixture的返回值
    1.fixture的函数名称，就是代表他的返回值
    2.在测试用例中。fixture函数名称作为测试用例的参数
'''
from PageObjects.login_page import LoginPage
from TestDatas import login_datas as TD
from PageObjects.index_page import IndexPage
# driver = None
@pytest.fixture(scope="class")#
def prepare_nev():
    # global driver
    #潜质条件
    print("==============测试类级别======================")
    driver = webdriver.Chrome()
    driver.get(CD.login_url)
    driver.maximize_window()
    #前置、后置分隔符
    yield driver
    #后置条件
    driver.quit()

@pytest.fixture()
def refresh_page(prepare_nev):
    print("==============测试用例级别======================")
    # global driver
    yield
    prepare_nev.refresh()

@pytest.fixture(scope="class")
def init_login(prepare_nev):
    LoginPage(prepare_nev).login(CD.user,CD.passwd)