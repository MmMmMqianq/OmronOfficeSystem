import socket
import struct
import threading


class MyServer:
	def __init__(self, host, port):
		self.HOST = host
		self.PORT = port

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# optVal = struct.pack("ii", 1, 0)
		# self.s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, optVal)
		self.s.bind((self.HOST, self.PORT))

	# self.s.listen()

	def my_accept(self):
		self.s.listen()

		def accept1():
			while True:
				print("等待客户端连接...")
				self.conn, self.addr = self.s.accept()
				print("开始监听，addr=%s, port=%d" % (self.addr[0], self.addr[1]))
				self.t2 = threading.Thread(target=self.handle, args=(self.conn, self.addr))
				self.t2.start()
				print(self.t2.getName())

		self.t = threading.Thread(target=accept1, daemon=True)
		self.t.start()

	def handle(self, conn: socket.socket, addr):
		while True:
			try:
				recv_data = conn.recv(1024)
				print(recv_data)
			except ConnectionResetError as e:
				if e.errno == 54:
					print("客户端已经断开。。。")
					conn.close()
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
