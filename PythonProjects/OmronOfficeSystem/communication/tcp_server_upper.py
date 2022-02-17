import socket
import threading
import time

import test


def deal(link, client):
    print('当前连接的客户端IP为 %s，端口号为：%s' % (client[0], client[1]))
    while True:
        try:
            # 网络上传输的都是字节流
            data = link.recv(1024).decode()  # 接收到的数据用decode()解码，默认为UTF-8
            print('接收到客户端 %s 发送来的信息为 %s ' % (client, data))
        except OSError as e:  # 由于关闭服务器时先会把所有接受的连接都关掉，所以会报错
            if e.errno == 9:
                print("连接已被关闭。。。")
                break
        if data == 'exit':
            print('客户端(%s, %d)连接关闭...' % (client[0], client[1]))
            break

        res = data.upper()
        # conn.sendall(res.encode())  # 发送时要将字符串用encode()方法发送
    link.close()  # 关闭连接；


hostaddress = ('', 8889)

# 默认使用ipv4,创建TCP。socket.AF_INET表示ipv4，socket.SOCK_STREAM表示TCP
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket TCP对象
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(hostaddress)  # 绑定IP地址
sk.listen(1)  # 监听端口，5表示可监听的进程数
print('启动socket服务，等待客户端连接...')


def a():
    while True:
        conn, clientaddress = sk.accept()  # accept()阻塞等待客户端的链接；
                                            # 当有客户端链接时阻塞被打断，连上之后可以拿到客户端的连接对象和客户端的IP、端口号
        print('当前连接的客户端IP为 %s，端口号为：%s' % (clientaddress[0], clientaddress[1]))
        sub_thread = threading.Thread(target=deal, args=(conn, clientaddress))
        sub_thread.start()
        time.sleep(5)
        conn.close()

t = threading.Thread(target=a)
t.start()
time.sleep(10)
print("结束子进程")
test.stop_thread(t)
print(threading.enumerate())
time.sleep(100000)


