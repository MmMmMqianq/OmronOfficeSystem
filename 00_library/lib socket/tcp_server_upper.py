
#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：tcp_server.py
时间：2021/06/15

服务器建立步骤：
1.txt. 服务器IP地址和端口号；
2. 创建socket TCP对象；
3. 绑定IP地址；
4. 监听端口，5表示可监听的进程数；
5. 阻塞等待客户端的链接；
6. 收发数据的处理；
7. 关闭连接；

server_upper升级内容：
1.txt. 可以多次的接受和发送数据；
2. 多线程，多个客户端可以连接盖服务器；
"""
import socket
import threading


def deal(link, client):
    print('当前连接的客户端IP为 %s，端口号为：%s' % (client[0], client[1]))
    while True:
        # 网络上传输的都是字节流
        data = conn.recv(1024).decode()  # 接收到的数据用decode()解码，默认为UTF-8
        print('接收到客户端 %s 发送来的信息为 %s ' % (client, data))

        if data == 'exit':
            print('客户端(%s, %d)连接关闭...' % (client[0], client[1]))
            break

        res = data.upper()
        # conn.sendall(res.encode())  # 发送时要将字符串用encode()方法发送
    link.close()  # 关闭连接；


hostaddress = ('', 8889)

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket TCP对象
sk.bind(hostaddress)  # 绑定IP地址
sk.listen(5)  # 监听端口，5表示可监听的进程数
print('启动socket服务，等待客户端连接...')

i = 0
while True:
    conn, clientaddress = sk.accept()  # accept()阻塞等待客户端的链接；
                                        # 当有客户端链接时阻塞被打断，连上之后可以拿到客户端的连接对象和客户端的IP、端口号
    sub_thread = threading.Thread(target=deal, args=(conn, clientaddress))
    sub_thread.start()
