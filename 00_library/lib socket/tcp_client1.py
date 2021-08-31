#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：tcp_client1.py
时间：2021/06/15
"""
# 使用socket.create_connection()创建一个客户端

import socket
import time

server_addr = ('192.168.10.107', 8888)  # 服务器的端口号和IP地址

source_addr = ('192.168.10.107', 8882)

client = socket.create_connection(address=server_addr, timeout=5.0, source_address=source_addr)  # 如果 host 是非数字主机名，它将尝试从 AF_INET 和 AF_INET6 解析它，然后依次尝试连接到所有可能的地址，直到连接成功。

print('4. ', client.gettimeout())

print('1.txt. ', client, type(client))                                                                    # source_address不写默认为本机的IP，自动分配一个端口

print('2. ', client.getsockname())


client.close()