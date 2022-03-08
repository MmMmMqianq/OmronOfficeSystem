#  -*- coding:utf-8 -*-
"""
客户端接收的反馈为字符串格式
作者：钱少青
文件名：tcp_finstcpclient1.py
时间：2021/06/22
"""
import binascii
import socket
import time


def process_receive_massage(message):
    receive_massage = ''
    print('接受到服务器未转换前的数据为：%s' % message)
    for message1 in message:
        # print(hex(answer2))
        if hex(message1)[2::] in ['1.txt', '2', '3', '4', '5', '6', '7', '8', '9']:
            recv_msg2 = '0'
            receive_massage = receive_massage + recv_msg2 + hex(message1)[2::]
        else:
            receive_massage = receive_massage + hex(message1)[2::]
    return receive_massage


# print('接受到服务器握手反馈的数据为：%s' % answer2, type(answer2))

serveraddress = ('192.168.10.2', 9600)  # 服务器的端口号和IP地址

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket对象

# sk.connect(serveraddress)  # 连接服务器

# 握手
fth = 0X46494E530000000C00000000000000000000006B  # 握手命令
print(fth, type(fth))
fth = hex(fth)
fth = fth[2::]
print(fth, type(fth))
fth = binascii.a2b_hex(fth)  # 返回由十六进制字符串 hexstr 表示的二进制数据。此函数功能与 b2a_hex() 相反。
                             # hexstr 必须包含偶数个十六进制数字（可以是大写或小写），否则会引发 Error 异常。
                             # 函数hexlify和b2a_hex实际是一个函数，建议使用hexlify。作用是返回的二进制数据的十六进制表示。
                             # 每一个字节的数据转换成相应的2位十六进制表示。因此产生的字串是源数据两倍长度。
                             # a2b_hex和unhexlify则执行反向操作。
print('转换后的字节流为：{}'.format(fth))

aa = b'FINS\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00k'
print(aa)

time.sleep(100000)
sk.sendall(fth)

recv_msg_hand1 = sk.recv(1024)
recv_msg_hand = process_receive_massage(recv_msg_hand1)
print('接受到服务器握手反馈的数据为：%s' % recv_msg_hand, type(recv_msg_hand))

while True:
    # workbook = input("请输入发送的数据：")
    # sk.sendall(workbook.encode())
    #
    # if workbook == 'exit':
    #     break

    ft = '46494e530000001a0000000200000000800002000200006b00000101820064000001'
    ft = binascii.a2b_hex(ft)
    # print(ft)
    sk.sendall(ft)

    recv_msg1 = sk.recv(1024)
    recv_msg = process_receive_massage(recv_msg1)
    print('接受到服务器的数据为：%s' % recv_msg)

    input('asd:')
sk.close()

