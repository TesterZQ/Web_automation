#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/2/18 20:09

#自动化测试帐号的独立性。
#1、用例列出 == 前置、步骤、断言
#2、明确有哪些页面

#用例1：成功投资场景
"""
前置：1、登陆成功状态；登陆页面 - 首页
      2、可用余额应该大于你要投资的金额；1000
         如何保证在自动化的运行过程中，余额可用。不需要我经常来看用户余额有多少。
         1）充值一笔：33：每次充投资的金额-1000；  ---利用接口直接充值。
         2）暂时充一大笔钱：1个亿。
         3）判断当前用户的余额是否大于投资金额，如果小于，我就大充一笔。如果大于，不用处理。
         要不要查数据库？接口？网页获取？   ---利用接口。
      3、有可投资的标。---在页面就可辨别标是否可投资。---利用元素定位。
         1）新建一个标，并且将标为竞标状态。---接口。
         2）达到1）很复杂。利用现有的环境。
步骤：
    1、首页 - 选标投资。默认选第一个标。
    2.0 标页面 - 金额 输入框中，获取用户的当前余额
    2、标页面 - 金额输入，投资操作。
    3、标页面 - 投资成功的弹出框中，点击 查看并激活
断言：
    1、投资前的余额 - 现在的用户余额  = 投资的钱
    个人页面 - 获取用户可用余额

"""
#投资失败的场景：
#1、非100的整数倍
#2、非10的整数倍
#3、小数点-非数字-负数-空


#4、投资的金额(5万)  >  标当前可投的金额(4万)   标+用户的余额同时满足特殊的条件
#5、投资的金额(5万) >   帐户可用余额(2万)
import unittest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage
from selenium import webdriver
from TestDatas import common_datas as CD
from TestDatas import invest_datas as TD
import time
import pytest

@pytest.mark.usefixtures("prepare_nev")
@pytest.mark.usefixtures("refresh_page")
@pytest.mark.invest
class TestInvest:
    #投资失败
    @pytest.mark.noinvest
    def test_invest_failed_no100(self,prepare_nev):
        LoginPage(prepare_nev).login(CD.user,CD.passwd)
        #首页-抢投标按钮-进入投标页面
        IndexPage(prepare_nev).click_firstBid()
        #投标输入框,输入
        time.sleep(3)
        BidPage(prepare_nev).invest(110)
        #点击投标按钮
        a = BidPage(prepare_nev).get_errorMsg_from_pageCenter()
        #断言文本定位：//div[@class="text-center"]
        assert a,'投标金额必须为100的倍数'

    #投资失败
    @pytest.mark.noinvest1
    def test_invest_failed_no10(self,prepare_nev):
        time.sleep(5)
        LoginPage(prepare_nev).login(CD.user,CD.passwd)
        # 首页-抢投标按钮-进入投标页面
        IndexPage(prepare_nev).click_firstBid()
        # 投标输入框,输入
        time.sleep(3)
        BidPage(prepare_nev).bid(72)
        # 点击投标按钮
        a = BidPage(prepare_nev).get_button_text()
        # 投资为1的时候按钮定位：//button[@class="btn btn-special height_style"]
        assert a, '请输入10的整数倍'
    #投资失败，异常数据
    @pytest.mark.noinvest2
    def test_invest_failed_invalid_data(self,prepare_nev):
        time.sleep(5)
        LoginPage(prepare_nev).login(CD.user, CD.passwd)
        # 首页-抢投标按钮-进入投标页面
        IndexPage(prepare_nev).click_firstBid()
        # 投标输入框,输入
        time.sleep(3)
        input_clear=BidPage(prepare_nev).invest(00000)
        # 点击投标按钮
        a = BidPage(prepare_nev).get_errorMsg_from_pageCenter()
        # 断言文本定位：//div[@class="text-center"]
        assert a, '请正确填写投标金额'

#投资成功用例
    def test_invest_success(self,prepare_nev):
        LoginPage(prepare_nev).login(CD.user, CD.passwd)#self.driver对象调用setupClass内里的类方法传参
        #步骤
        # 1、首页 - 选标投资。默认选第一个标。
        IndexPage(prepare_nev).click_firstBid()
        # 2.0标页面 - 金额输入框中，获取用户投标前的余额
        bp = BidPage(prepare_nev)
        userMoney_beforeInvest = bp.get_userLeftMoney()
        # 2、标页面 - 金额输入，投资操作。
        bp.invest(TD.money)
        # 3、标页面 - 投资成功的弹出框中，点击查看并激活
        bp.click_activeButton_on_investSuccess_popup()
        #断言
        userMoney_afterInvest = UserPage(prepare_nev).get_userLeftMoney()
        assert float(userMoney_beforeInvest),userMoney_afterInvest+TD.money
