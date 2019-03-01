# -*- coding:utf-8 -*-
#@Time      :14:48
#@Auther    :ZhangQiang
#@Name      :path.py

import os
real_path=os.path.realpath(__file__)
#根目录路径
basic_path=os.path.split(os.path.split(real_path)[0])[0]
#日志目录
log_dir=os.path.join(basic_path,"result","logs")
#截屏路径
screen=os.path.join(basic_path,"result","screenshot")
#测试报告
testreport_path=os.path.join(basic_path,'result','report','test_report.html')