import time

from PyQt5.QtCore import pyqtSignal, pyqtBoundSignal, QObject
import socket
import struct
import threading


class MyServer:

	def __init__(self, host, port):
		self.HOST = host
		self.PORT = port

		self.conn_pool = list()  # 保存服务器已接受的客户端信息, l为二维列表:[[0服务器监听状态, 1服务器编号, 2线程名, 3服务器IP, 4服务器端口号,
																		# 5客户端IP, 6客户端端口号, 7客户端连接, 8客户端编号, 9客户端连接状态], [], []...]
		self.server_No = int()  # 用于判断客户端时连接到哪个服务器的，从而更新tree显示
		self.listening = False  # 服务器是否处于监听中
		self.client_No = 0
		self.conn = socket.socket()
		self.addr = tuple()

		self.server_signal = ServerSignals()
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
					if e.errno == 53:  # 服务器打开还处于accept中，直接close掉服务器
						print("服务器已被关闭。。。")
						break
				else:
					self.conn_pool.append([self.listening, self.server_No, self.conn.getsockname()[0],
					                       self.conn.getsockname()[1], self.addr[0], self.addr[1], self.conn,
					                       self.client_No, True])
					self.t2 = threading.Thread(target=self.handle, args=(self.conn, self.conn_pool[-1][1],
					                                                     self.conn_pool[-1][7], self.conn_pool[-1][2],
					                                                     self.conn_pool[-1][3], self.addr[0], self.addr[1]))
					self.t2.start()
					self.conn_pool[-1].insert(2, self.t2.getName())
					self.server_signal.accepted_done.emit(self.conn_pool)
					self.client_No += 1

		self.s.listen()
		self.listening = True
		self.server_signal.listened_done.emit("listened_done")

		self.t = threading.Thread(target=accept1, daemon=True)
		self.t.start()

	def stop_listen(self):
		self.listening = False
		for i in self.conn_pool:
			# i[7].shutdown(socket.SHUT_RDWR)
			i[7].close()
			i[-1] = False
		self.conn_pool.clear()
		self.s.close()
		print("停止监听。。。")

	def handle(self, conn: socket.socket, server_num, client_num, server_ip, server_port, client_ip, client_port):
		# print(conn, server_num, client_num, server_ip, server_port, client_ip, client_port)
		while True:
			try:
				recv_data = conn.recv(1024)
			except ConnectionResetError as e:
				if e.errno == 54:
					print("客户端主动断开连接。。。")
					conn.close()
					self.server_signal.conn_closed_done.emit(["conn_closed_done", server_num, client_num, self.listening, server_num])
					break
			except OSError as e:  # 由于关闭服务器时先会把所有接受的连接都关掉，所以会报错
				if e.errno == 9:
					print("连接已被关闭。。。")
					self.server_signal.conn_closed_done.emit(["conn_closed_done", server_num, client_num, self.listening, server_num])
					break
			else:
				if recv_data != b'':
					print(recv_data)
					for i in range(len(self.conn_pool)):
						if self.conn_pool[i][8] == client_num:
							client_index = i
							break
					ts = time.time()
					info = [ts, server_ip, server_port, server_num, client_ip, client_port, client_index, len(recv_data), recv_data]
					self.server_signal.receive_data_done.emit(info, "receive_data_done")
				else:
					conn.close()
					print("服务器主动关闭客户端连接。。。")
					self.server_signal.conn_closed_done.emit(["conn_closed_done", server_num, client_num, self.listening, server_num])
					break


class MyClient:
	def __init__(self, server_ip, server_port):
		self.server_ip = server_ip
		self.server_port = server_port
		self.client_No = int()  # 用于判断是哪个top item对应的客户端执行的连接操作
		self.info = [self.client_No, "--", "--", self.server_ip, self.server_port, 0]  # 1表正常连接，-1表示连接出错，0表示客户端未进行连接操作

		self.client_signal = ClientSignals()
		self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.optVal = struct.pack("ii", 1, 0)
		self.c.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, self.optVal)

	def client_connect(self):
		try:
			self.c.connect((self.server_ip, self.server_port))
		except TimeoutError as e:
			self.info = [self.client_No, "-1", -1, self.server_ip, self.server_port, -1]
			self.client_signal.connect_error.emit(self.info, "connect_error")
			if e.errno == 60:
				print("通信超时，没能连上服务器。。。")
			if e.error == 56:
				print("[Errno 56] Socket is already connected.")
			if e.errno == 9:
				print("[Errno 9] Bad file descriptor")  # 服务器侧关闭连接，客户端再点连接时报错
		else:
			self.client_ip = self.c.getsockname()[0]
			self.client_port = self.c.getsockname()[1]
			self.t = threading.Thread(target=self.handle, daemon=True)
			self.t.start()
			self.info = [self.client_No, self.client_ip, self.client_port, self.server_ip, self.server_port, 1]
			self.client_signal.connect_done.emit(self.info, "connect_done")

	def handle(self):
		while True:
			try:
				recv_data = self.c.recv(1024)
			except OSError as e:
				if e.errno == 9:
					print("[Errno 9] Bad file descriptor,"+"连接已被关闭。。。")
					break
			if recv_data != b"":
				pass
			else:
				self.c.close()
				self.client_signal.conn_closed_done.emit([self.client_No, "--", "--",
				                                          self.server_ip, self.server_port, 0], "conn_closed_done")
				print("服务器以主动关闭，客户端关闭。。。")
				break


class ServerSignals(QObject):
	accepted_done: pyqtBoundSignal
	listened_done: pyqtBoundSignal
	conn_closed_done: pyqtBoundSignal
	receive_data_done: pyqtBoundSignal
	send_data_done: pyqtBoundSignal

	accepted_done = pyqtSignal(list)
	listened_done = pyqtSignal(str)
	conn_closed_done = pyqtSignal(list)
	receive_data_done = pyqtSignal(list, str)
	send_data_done = pyqtSignal(list, str)


class ClientSignals(QObject):
	connect_done: pyqtBoundSignal
	connect_error: pyqtBoundSignal
	conn_closed_done: pyqtBoundSignal
	receive_data_done: pyqtBoundSignal
	send_data_done: pyqtBoundSignal

	connect_done = pyqtSignal(list, str)
	connect_error = pyqtSignal(list, str)
	conn_closed_done = pyqtSignal(list, str)
	receive_data_done = pyqtSignal(list, str)
	send_data_done = pyqtSignal(list, str)


def get_local_ip(messageBox):
	ip = str()
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		optVal = struct.pack("ii", 1, 0)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, optVal)
		s.connect(("8.8.8.8", 80))
		ip = s.getsockname()[0]
	except OSError as e:
		if e.errno == 51:
			print("请检查网络！")
			messageBox.show()
	finally:
		s.close()
	return ip