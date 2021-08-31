#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：opcua_client.py
时间：2021/06/29
"""
import time
import opcua

url = 'opc.tcp://192.168.10.107:4841'
client = opcua.Client(url)
client.connect()

while True:
    temp = client.get_node("ns=2;i=2")  # 暂时不清楚啥意思
    temp_value = temp.get_value()
    print(temp_value)
    time.sleep(1)
