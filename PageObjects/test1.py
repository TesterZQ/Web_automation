'''
练习模块
'''

from ddt import ddt
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
a = webdriver.Chrome()
a.get("https://blog.csdn.net/u013218587/article/details/80590878")
a.find_element_by_xpath().click()
a.split()

class A:

    def __init__(self):
        self.a = webdriver.Chrome()
        self.a.get("https://blog.csdn.net/u013218587/article/details/80590878")
    def a(self):
        WebDriverWait()
