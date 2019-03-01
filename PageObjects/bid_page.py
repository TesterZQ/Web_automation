'''
投标页面方法封装

'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.bidPage_locator import BidPageLocator as loc
from Common.basepage import BasePage

class BidPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    #获取用户余额
    def get_userLeftMoney(self):
        #调用元素等待封装的方法，传参（传要等待的元素参数）
        self.wait_eleVisible(loc.money_input,model_name="标页面_获取用户余额")
        # 等待用户输入框出现
        #WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((loc.money_input)))
        #"*"表示为解析BidPageLocator内money_input元组，解释出定位方式与定位元素
        #get_attribute获取元素标签内容函数，查找元素，在获取元素属性
        #return self.driver.find_element(*loc.money_input).get_attribute("data-amount")#元素属性
        return self.get_element_attribute(loc.money_input,"data-amount",model_name="标页面_获取金额输入框的data-amount属性")

    #投资操作
    def invest(self,money):
        model="标页面_投资操作"
        self.wait_eleVisible(loc.money_input,model_name=model)
        #等待操作，等待用户输入框出现
        # WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((loc.money_input)))
        #输入框中输入金额
        self.input_text(loc.money_input,money,model_name=model)
        #self.driver.find_element(*loc.money_input).send_keys(money)
        #点击投标按钮
        self.click_element(loc.invest_button,model_name=model)#二次封装方法
        #self.driver.find_element(*loc.invest_button).click()


    #投资成功弹出框、点击查看并激活
    def click_activeButton_on_investSuccess_popup(self):
        #等待二次封装方法
        name ="标页面_投资成功弹出框_点击查看并激活"
        self.wait_eleVisible(loc.active_button_on_successPop,model_name=name)
        #等待弹出框出现
        #WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((loc.active_button_on_successPop)))
        #投资成功弹出框 - 查看并激活按钮
        self.click_element(loc.active_button_on_successPop,model_name=name)
        #self.driver.find_element(*loc.active_button_on_successPop).click()

    #错误提示框-页面中间
    def get_errorMsg_from_pageCenter(self):
        #获取文本内容
        #关闭弹出框
        name = "标页面_页面中间错误提示框"
        self.wait_eleVisible(loc.invest_failed_popup,model_name=name)
        #等待
        #WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((loc.invest_failed_popup)))
        #获取文本
        msg = self.get_element_text(loc.invest_failed_popup,model_name=name)
        #获取错误提示文本
        #msg = self.driver.find_element(*loc.invest_failed_popup).text
        #关闭弹框
        self.click_element(loc.invest_failed_popup,model_name=name)
        #self.driver.find_element(*loc.invest_failed_popup).click()
        return msg

    def get_button_text(self):
        # name = "标页面_输入内容小于100，页面按钮置灰"
        #等待
        # self.wait_eleVisible(loc.invest_fial_button_no10,model_name=name)
        #获取按钮文本
        msg = self.get_element_text(loc.invest_fial_button_no10)
        return msg
    #投资金额输入
    def bid(self,bid):
        self.input_text(loc.money_input,bid,model_name="投资金额输入框")

