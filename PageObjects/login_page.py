'''

登录页面方法封装
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locators import LoginPageLocator as loc
from Common.basepage import BasePage
import time
class LoginPage(BasePage):


    # def __init__(self,driver):
    #     self.driver = driver
    #登录功能
    def login(self,username,password):
        name = "登录页面_登录功能"
        self.wait_eleVisible(loc.user_input,model_name=name)
        #WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((loc.user_input)))
        #用户名定位.
        #定义参数，调用该方法时，传对应的参数
        self.input_text(loc.user_input,username,model_name=name)
        #self.driver.find_element(*loc.user_input).send_keys(username)
        #用户密码定位
        self.input_text(loc.user_password,password,model_name=name)
        #self.driver.find_element(*loc.user_password).send_keys(password)
        #点击登录
        self.click_element(loc.login_buuton,model_name=name)
        #self.driver.find_element(*loc.login_buuton).click()

    #获取错误提示，账户、密码为空
    def get_errorMsg_from_loginArea(self):
        #等待
        name = "登录页面_账户密码为空"
        self.wait_eleVisible(loc.errorMsg_from_loginArea,model_name=name)
        #WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((loc.errorMsg_from_loginArea)))
        #通过return返回错误信息
        return self.get_element_text(loc.errorMsg_from_loginArea,model_name=name)
        #return self.driver.find_element(*loc.errorMsg_from_loginArea).text

    #页面弹窗错误提示定位：//div[@class="layui-layer-content"]
    def get_errorMsg_from_pageCenter(self):
        #等待
        name = "登录页面_页面弹窗错误提示定位"
        self.wait_eleVisible(loc.errorMsg_from_pageCenter,model_name=name)
        #WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((loc.errorMsg_from_pageCenter)))
        # 页面弹窗错误提示定位：//div[@class="layui-layer-content"]
        #获取错误文本后，返回
        return self.get_element_text(loc.errorMsg_from_pageCenter,model_name=name)
        #return self.driver.find_element(*loc.errorMsg_from_pageCenter).text