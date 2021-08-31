#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：web_server.py
时间：2021/08/25
"""
import socket
import threading

RESPONSE_DIR = "responsefiles"


def handle(link, linkaddr):
    """处理客户端请求"""
    print("客户端的IP: %s，端口号: %d" % (linkaddr[0], linkaddr[1]))
    print(type(link))
    # 接收客户端请求
    request_data = link.recv(1024).decode()
    print("request data: ", request_data)

    # 解析请求报文
    request_data_lines = request_data.splitlines()
    request_first_line = request_data_lines[0].split()
    request_dir = request_first_line[1]
    print(RESPONSE_DIR+request_dir)

    # 构造响应数据
    response = b''
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_server = "Server: QSQSQSQ\r\n"
    response_body_start = "\r\n"
    try:
        with open(RESPONSE_DIR+request_dir, "rb") as file:
            response_body = file.read()
    except IOError:
        response = "HTTP/1.1 400 NOT FOUND\r\nServer: QSQSQSQ\r\n\r\nfile is not found".encode()
        print("未找到对应文件！")
    else:
        if isinstance(response_body, bytes):
            response = (response_start_line + response_server + response_body_start).encode()+response_body
        elif isinstance(response_body, str):
            response = (response_start_line + response_server + response_body_start + response_body).encode(encoding="GBK")
    finally:
        # 发送响应数据
        link.sendall(response)

        # 关闭子进程连接
        link.close()
        print("*" * 20)


webser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
webser.bind(('', 80))
webser.listen(5)
print("等待客户端连接...")
while True:
    conn, clientaddr = webser.accept()
    sub_thread = threading.Thread(target=handle, args=(conn, clientaddr))
    sub_thread.start()
