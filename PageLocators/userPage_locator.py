'''
用户中心元素定位封装

'''

from selenium.webdriver.common.by import By

class UserPageLocator:

    #可用余额
    user_leftMoney = (By.XPATH,'//li[@class="color_sub"]')