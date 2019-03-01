'''

投标页面元素定位数据封装
'''

from selenium.webdriver.common.by import By

class BidPageLocator:

    #金额输入框
    money_input = (By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")
    #投标按钮
    invest_button = (By.XPATH,'//button[text()="投标"]')
    #投资成功弹出框 - 查看并激活按钮
    active_button_on_successPop = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败 - 弹出框 - 提示信息
    invest_failed_popup = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]')
    # 投资失败 - 弹出框 - 关闭弹出框
    invest_close_failed_popup_button = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//a')
    #投资小于100元按钮置灰，无法点击
    invest_fial_button_no10 = (By.XPATH,'//button[@class="btn btn-special height_style"]')#//button[@class="btn btn-special height_style"]