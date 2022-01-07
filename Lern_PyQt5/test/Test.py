import threading


class A():
	def __init__(self):

		self.t = threading.Thread(self.a)

	def a(self):
		print(1213)


aa = A()