import socket
import threading


class MyServer():
	def __init__(self, host, port):
		self.HOST = host
		self.PORT = port

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((self.HOST, self.PORT))
		self.s.listen()

	def my_accept(self):
		def accept1():
			while True:
				conn, addr = self.s.accept()
				t2 = threading.Thread(target=self.handle, argv=(conn, addr))
				t2.start()
		t = threading.Thread(target=accept1)
		t.start()

	def handle(self):
		pass