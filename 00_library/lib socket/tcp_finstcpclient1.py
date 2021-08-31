#  -*- coding:utf-8 -*-
"""
客户端接收的反馈为bytes给是
作者：钱少青
文件名：tcp_finstcpclient1.py
时间：2021/06/22
"""
import binascii
import socket


serveraddress = ('192.168.10.2', 9600)  # 服务器的端口号和IP地址

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket对象
# sk.settimeout(2.0)
sk.connect(serveraddress)  # 连接服务器
# sk.gettimeout()



# 握手
fth = 0x46494E530000000C00000000000000000000006B  # 握手命令
fth = hex(fth)
fth = fth[2::]
print(fth)
fth = binascii.a2b_hex(fth)  # 返回由十六进制字符串 hexstr 表示的二进制数据。此函数功能与 b2a_hex() 相反。
                             # hexstr 必须包含偶数个十六进制数字（可以是大写或小写），否则会引发 Error 异常。
                             # 函数hexlify和b2a_hex实际是一个函数，建议使用hexlify。作用是返回的二进制数据的十六进制表示。
                             # 每一个字节的数据转换成相应的2位十六进制表示。因此产生的字串是源数据两倍长度。
                             # a2b_hex和unhexlify则执行反向操作。
# print('转换后的字节流为：{}'.format(fth))
sk.sendall(fth)

recv_msg_hand1 = sk.recv(1024)
# recv_msg_hand = process_receive_massage(recv_msg_hand1)
recv_msg_hand = binascii.b2a_hex(recv_msg_hand1)
print('接受到服务器握手反馈的数据为：%s' % recv_msg_hand, type(recv_msg_hand))

while True:
    # data = input("请输入发送的数据：")
    # sk.sendall(data.encode())
    #
    # if data == 'exit':
    #     break

    ft = '46494e530000001a0000000200000000800002000200006b00000101820064000001'
    ft = binascii.a2b_hex(ft)
    # print(ft)
    sk.sendall(ft)

    recv_msg1 = sk.recv(1024)
    recv_msg = binascii.b2a_hex(recv_msg1)  # 返回二进制数据 data 的十六进制表示形式。 data 的每个字节都被转换为相应的2位十六进制表示形式。
                                            # 因此返回的字节对象的长度是 data 的两倍。
    print('接受到服务器的数据为：%s' % recv_msg)

    input('asd:')
sk.close()
