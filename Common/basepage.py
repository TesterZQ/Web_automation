'''
封装页面基本操作
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.dir_config import screenshot_dir
import logging
import time
import datetime

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #等待元素课件
    def wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5,model_name="model"):#locator元素定位参数、timeout等待时间，默认30秒、poll_frequency：周期间隔参数,model_name:模块名称
        logging.info("等待元素可见：{}".format(locator))
        try:
            #获取开始等待时间（自己操作）
            start_time= datetime.datetime.now()
            time.sleep(5)
            WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(EC.visibility_of_all_elements_located(locator))
            #获取结束等待的时间
            #获取等待的总时长-以秒为单位
            end_time = datetime.datetime.now()
            diff_time =(end_time-start_time).seconds
            logging.info("元素可见。等待元素可见总时长：开始等待的时间，等待结束的时间")
        except:
            #捕获异常，写进日志
            logging.exception("等待元素可见超市")#把报错信息写写进日志
            #截图-直接同过图片名称就知道截图是什么图片
            self.save_webimg(model_name)
            raise
    #查找元素
    def get_element(self,locator,model_name):
        logging.info("查找模块：{}下的元素：{}".format(model_name, locator))
        try:
            ele = self.driver.find_element(*locator)
            logging.info("查元素成功。")
            return ele
        except:
            # 写进日志
            logging.exception("查找元素失败。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    #点击元素
    def click_element(self,locator,model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("点击操作：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            ele.click()
        except:
            # 写进日志
            logging.exception("点击元素操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise
    #获取元素属性
    def get_element_attribute(self,locator,attr,model_name):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素属性：模块 {} 下的元素 {} 的属性 {}".format(model_name, locator, attr))
        try:
            return ele.get_attribute(attr)
        except:
            # 写进日志
            logging.exception("获取元素属性失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    #输入内容
    def input_text(self, locator, value, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("输入操作：模块 {} 下的元素 {}输入文本 {}".format(model_name, locator, value))
        try:
            ele.send_keys(value)
        except:
            # 写进日志
            logging.exception("元素输入操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素属性：模块 {} 下的元素 {} 的属性 {}".format(model_name, locator, attr))
        try:
            return ele.get_attribute(attr)
        except:
            # 写进日志
            logging.exception("获取元素属性失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise
    #获取元素文本内容
    def get_element_text(self,locator,model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素文本值：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            return ele.text
        except:
            # 写进日志
            logging.exception("获取元素文本值失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    #截图
    def save_webimg(self,model_name):
        # 文件名称=模块名称_当前时间.png
        filePath = screenshot_dir + "/{0}_{1}.png".format(model_name,time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截图成功，文件路径为：{}".format(filePath))
        except:
            logging.exception("截图失败！！")
#窗口切换。新的窗口，其它的窗口
    def switch_window(self,str="",index=None):
        if str == "new":
            #等待新窗口出现？
            time.sleep(2)
            windows = self.driver.window_handles
            #切换到窗口
            self.driver.switch_to.window(windows[-1])
        else:
            #获取所有的窗口
            windows = self.driver.window_handles
            if index != None and 0 <= int(index) < len(windows):
                self.driver.switch_to.window(windows[int(index)])
            #切换到index下标所有的窗口。


    #alert切换
    def switch_alert(self,action="accept"):
        #等待alert出现
        WebDriverWait(self.driver,10).until(EC.alert_is_present())
        #关闭alert弹框 - accept,dismiss
        alert = self.driver.switch_to.alert
        if action == "accept":
            alert.accept()   #查阅 alert类的accept函数
        else:
            alert.dismiss()   #查阅 alert类的dismiss函数

    #iframe切换
    def switch_iframe(self,iframe_refrence):
        try:
            #等待iframe出现 #切换 - WebDriverWait
            time.sleep(0.5)
        except:
            pass


    #上传
    def upload(self):
        pass

    #等待存在某个元素
    def wait_until_page_contains_element(self,locator):
        pass
        pass

    #页面应当存在某一个元素
    def page_should_contain_element(self,locator):
        pass

