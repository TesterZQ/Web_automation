'''
个人用户页面方法封装

'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.indexPage_locator import IndexPageLocator as IP
from PageLocators.memberPage import MemberPageLLocator as MB
from Common.basepage import BasePage
class UserPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver


    #获取用户余额
    def get_userLeftMoney(self):
        name = "首页_我的账户"
        self.wait_eleVisible(IP.user_link,model_name=name)
    #点击我的账户
        self.click_element(IP.user_link,model_name=name)
        #self.driver.find_element(*IP.user_link).click()
    #获取账户余额
        money = self.get_element_text(MB.my_money)
        #money= self.driver.find_element(*MB.my_money).text
        money = money.split('元')[0]
        return float(money)

