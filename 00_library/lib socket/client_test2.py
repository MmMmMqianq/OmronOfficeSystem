import socket
import struct
import time

serveraddress = ('192.168.10.105', 8889)  # 服务器的端口号和IP地址

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket对象
a = struct.pack("ii", 1, 0)
sk.setsockopt(socket.SOL_SOCKET,socket.SO_LINGER, a)  # 关闭TIME_WAIT
sk.connect(serveraddress)  # 连接服务器
time.sleep(10000)


# while True:
#     data = input("请输入发送的数据：")
#     sk.sendall(data.encode())
#
#     if data == '2':
#         break
#
#     answer = sk.recv(1024).decode()
#     print('接受到服务器的数据为：%s' % answer)
#
# sk.close()