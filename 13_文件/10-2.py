#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：10-2.py
时间：2021/06/11
"""
from ch10.appConfig import config_data

print("数据库地址：{0}".format(config_data['db_url']))
print("数据库端口：{0}".format(config_data['db_port']))
print("数据库用户：{0}".format(config_data['db_user']))
print("数据库密码：{0}".format(config_data['db_password']))
