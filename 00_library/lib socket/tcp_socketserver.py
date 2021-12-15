
#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：tcp_server.py
时间：2021/06/15

使用 socketserver 库实现socket通信：
1.txt. 新建类，该类继承socketserver.BaseRequestHandler;
2. 重写 handle;
3. 创建多线程 server 对象；
4.
"""

import socketserver


class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):  # 要处理的内容
        print('当前连接的客户端IP为 %s，端口号为：%s' % (self.client_address[0], self.client_address[1]))
        while True:
            # 网络上传输的都是字节的数组
            data = self.request.recv(1024).decode()  # 接收到的数据用decode()解码，默认为UTF-8
            print('接收到客户端 %s 发送来的信息为 %s ' % (self.client_address, data))

            if data == 'exit':
                print('客户端(%s, %d)连接关闭...' % (self.client_address[0], self.client_address[1]))
                break

            # res = workbook.upper()
            res = input('请输入要返回的数据：')
            self.request.sendall(res.encode())  # 发送时要将字符串用encode()方法发送
        self.request.close()  # 关闭连接；


if __name__ == '__main__':
    hostaddress = ('192.168.10.107', 8888)
    tcp_server = socketserver.ThreadingTCPServer(hostaddress, MyTcpHandler)  # ThreadingTCPServer()是异步多线程的框架模型
    tcp_server.daemon_threads = True  # 表示如果服务器停止，所有线程会被强行中断；
    print('启动socket服务，等待客户端连接...')
    tcp_server.serve_forever()


