import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer
import threading
import time

def b():
	print(1)


def a(count):
	c = 0

	def d():
		threading.Timer(1, function=d).start()
		nonlocal c
		if c > 0:
			b()
		if c >= count:
			print(threading.enumerate())
			for i in threading.enumerate():
				if threading.enumerate().index(i) != 0:
					i.cancel()
			return
		c += 1
	d()
a(5)
