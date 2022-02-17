"""
作者：钱少青
文件名：tcp_client1.py
时间：2021/06/15

客户端的建立:
1.txt. 服务器的端口号和IP地址；
2. 建立socket对象；
3. 连接服务器；
4. 收发数据处理；
5. socket关闭

client_uppers升级内容：
可以多次收发数据，在用户输入‘exit’时关闭socket客户端；
"""
import socket
import struct


serveraddress = ('192.168.10.105', 8889)  # 服务器的端口号和IP地址

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket对象
optVal = struct.pack("ii", 1, 0)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, optVal)  # 关闭TIME_WAIT
sk.connect(serveraddress)  # 连接服务器


while True:
    data = input("请输入发送的数据：")
    sk.sendall(data.encode())

    if data == '2':
        break

    answer = sk.recv(1024).decode()
    print('接受到服务器的数据为：%s' % answer)

sk.close()
