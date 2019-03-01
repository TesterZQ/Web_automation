'''我的页面封装'''
from selenium.webdriver.common.by import By
class MemberPageLLocator:
    #我的页面账户可用余额
    my_money =(By.XPATH,'//li[@class="color_sub"]')