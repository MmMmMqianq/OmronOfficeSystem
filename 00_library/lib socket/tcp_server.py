#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：tcp_server.py
时间：2021/06/15
"""
import socket

host_address = ('192.168.10.107', 8888)

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(host_address)  # 绑定IP地址
sk.listen(5)  # 监听端口，5表示可监听的进程数,未指定则自动设为合理的默认值;

print(sk.getblocking())  # 用于判断当前是否处于阻塞状态；
print('启动socket服务，等带客户端连接...')


conn, client_address = sk.accept()  # accept()可以拿到客户端连接的对象和客户端的IP、端口号
print(conn)

# 网络上传输的都是字节的数组
data = conn.recv(1024).decode()  # 接收到的数据用decode()解码，默认为UTF-8
print('接收到客户端 %s 发送来的信息为 %s ' % (client_address, data))

res = data.upper()
conn.sendall(res.encode())

# conn.shutdown(how='SHUT_RDWR')  # how 为 SHUT_RD，则后续不再允许接收。如果 how 为 SHUT_WR，则后续不再允许发送。如果 how 为 SHUT_RDWR，则后续的发送和接收都不允许。

conn.close()
