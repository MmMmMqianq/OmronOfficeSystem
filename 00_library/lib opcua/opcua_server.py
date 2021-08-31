#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：opcua_server.py
时间：2021/06/28
"""
import opcua
import random
import time

server = opcua.Server()
url = "opc.tcp://192.168.10.107:4841"
server.set_endpoint(url)

name = 'OPC UA SIMULATION SERVER'
add_space = server.register_namespace(name)

node = server.get_objects_node()

param = node.add_object(add_space, "PARAMETERS")

temp = param.add_variable(add_space, "Temperature", 0)
temp.set_writable()

server.start()
print('server started at {}'.format(url))

while True:
    temperature = random.randint(10, 50)
    temp.set_value(temperature)

    time.sleep(1)
