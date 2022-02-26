import time

from PyQt5.QtCore import pyqtSignal, pyqtBoundSignal, QObject
import socket
import struct
import threading
import test


class MyServer:

	def __init__(self, host, port):
		self.HOST = host
		self.PORT = port

		self.conn_pool = list()  # 保存服务器已接受的客户端信息, l为二维列表:[[0服务器监听状态, 1服务器编号, 2线程名, 3服务器IP, 4服务器端口号,
																		# 5客户端IP, 6客户端端口号, 7客户端连接, 8客户端编号, 9客户端连接状态], [], []...]
		self.server_No = int()  # 用于判断客户端时连接到哪个服务器的，从而更新tree显示
		self.listening = False  # 服务器是否处于监听中
		self.client_num = 0
		self.conn = socket.socket()
		self.addr = tuple()

		self.server_signal = TcpSignals()
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# optVal = struct.pack("ii", 1, 0)
		# self.s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, optVal)
		self.s.bind((self.HOST, self.PORT))

	def my_accept(self):
		def accept1():
			while True:
				print("等待客户端连接...")
				try:
					self.conn, self.addr = self.s.accept()
				except ConnectionAbortedError as e:
					if e.errno == 53:
						break
				else:
					self.conn_pool.append([self.listening, self.server_No, self.conn.getsockname()[0],
					                       self.conn.getsockname()[1], self.addr[0], self.addr[1], self.conn,
					                       self.client_num, True])
					self.t2 = threading.Thread(target=self.handle, args=(self.conn, self.addr, self.conn_pool[-1][1],
					                                                     self.conn_pool[-1][7]))
					self.t2.start()
					self.conn_pool[-1].insert(2, self.t2.getName())
					self.server_signal.accepted_done.emit(self.conn_pool)
					self.client_num += 1

		self.s.listen()
		self.listening = True
		self.server_signal.listened_done.emit("auto_listened_done")

		self.t = threading.Thread(target=accept1, daemon=True)
		self.t.start()

	def stop_listen(self):
		self.listening = False
		for i in self.conn_pool:
			i[7].shutdown(socket.SHUT_RDWR)
			i[7].close()
			i[-1] = False
		self.conn_pool.clear()
		self.s.close()
		print(self.conn_pool)
		print("停止监听。。。")

	def handle(self, conn: socket.socket, addr, server_num, client_num):
		print(client_num)
		while True:
			try:
				recv_data = conn.recv(1024)
			except ConnectionResetError as e:
				if e.errno == 54:
					print("客户端已经断开。。。")
					conn.close()
					self.server_signal.conn_closed_done[str, int].emit("conn_closed_done", client_num)
					break
			except OSError as e:  # 由于关闭服务器时先会把所有接受的连接都关掉，所以会报错
				if e.errno == 9:
					print("连接已被关闭。。。")
					break
			else:
				if recv_data == '':
					print(recv_data)
				else:
					conn.close()
					print("客户端已主动关闭连接。。。")
					self.server_signal.conn_closed_done.emit(["conn_closed_done", server_num, client_num])
					break


class MyClient:
	def __init__(self, host, port):
		self.HOST = host
		self.PORT = port
		self.c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.optVal = struct.pack("ii", 1, 0)

	def client_connect(self):
		self.c.connect((self.HOST, self.PORT))
		self.t = threading.Thread(target=self.handle)
		self.t.start()

	def handle(self):
		pass


class TcpSignals(QObject):
	accepted_done: pyqtBoundSignal
	listened_done: pyqtBoundSignal
	conn_closed_done: pyqtBoundSignal
	accepted_done = pyqtSignal(list)
	listened_done = pyqtSignal(str)
	conn_closed_done = pyqtSignal(list)


def get_local_ip():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		optVal = struct.pack("ii", 1, 0)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, optVal)
		s.connect(("8.8.8.8", 80))
		ip = s.getsockname()[0]
	except OSError as e:
		if e.errno == 51:
			print("请检查网络！")
	finally:
		s.close()
	return ip