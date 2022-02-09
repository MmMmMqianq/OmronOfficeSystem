import socket
import time

serveraddress = ('192.168.10.105', 8889)  # 服务器的端口号和IP地址

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
i = 0
sk_list = list()
while i < 100:
	# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket对象
	sk_list.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

	sk_list[i].connect(serveraddress)  # 连接服务器
	print(sk_list)
	print(i)
	i = i+1
	time.sleep(0.1)
time.sleep(100000)


# while True:
#     data = input("请输入发送的数据：")
#     sk.sendall(data.encode())
#
#     if data == 'exit':
#         break
#
#     answer = sk.recv(1024).decode()
#     print('接受到服务器的数据为：%s' % answer)
#
# sk.close()