'''首页元素定位封装'''

from selenium.webdriver.common.by import By
class IndexPageLocator:
    # 用户昵称
    user_link = (By.XPATH,'//a[@href="/Member/index.html"]')
    #抢投标按钮
    bid_button = (By.XPATH,'//a[@class="btn btn-special"]')
    #首页退出元素
    exit = (By.XPATH,'//a[text()="退出"]')
