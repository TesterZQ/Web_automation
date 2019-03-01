'''

首页方法封装
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.indexPage_locator import IndexPageLocator as loc
from Common.basepage import BasePage
class IndexPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def isExist_quitEle(self):
        try:
            self.wait_eleVisible(loc.exit,model_name="首页_退出")
            #等待这个元素出现并定位
            #WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//a[text()="退出"]')))
            return True
        except:
            return False
    #获取页面第一个抢投标元素，点击进入投标页面
    def click_firstBid(self):
        #等待
        name = "首页_标元素"
        self.wait_eleVisible(loc.bid_button,model_name=name)
        #WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((loc.bid_button)))
        #点击抢投标按钮
        self.click_element(loc.bid_button,model_name=name)
        #self.driver.find_element(*loc.bid_button).click()