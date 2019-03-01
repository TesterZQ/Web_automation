'''
登录页面元素定位封装
'''

from selenium.webdriver.common.by import By
class LoginPageLocator:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    user_password = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_buuton = (By.XPATH, '//button[text()="登录"]')
    # 错误提示框
    errorMsg_from_loginArea = (By.XPATH, '//div[@class="form-error-info"]')
    # 错误提示框-页面弹窗
    errorMsg_from_pageCenter = (By.XPATH, '//div[@class="layui-layer-content"]')