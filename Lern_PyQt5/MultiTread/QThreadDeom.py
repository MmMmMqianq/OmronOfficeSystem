import sys
import time
from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QGridLayout, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal, pyqtBoundSignal


class LcdDisplyNumber(QWidget):

	def __init__(self):
		super(LcdDisplyNumber, self).__init__()

		self.setWindowTitle("这是一个多线程实例")
		self.resize(300, 200)

		self.lcd = QLCDNumber()
		self.button = QPushButton("开始计数")
		self.button1 = QPushButton("isRunning")
		self.gLayout = QGridLayout(self)
		self.gLayout.addWidget(self.lcd, 0, 0, 1, 3)
		self.gLayout.addWidget(self.button, 1, 2, 1, 1)
		self.gLayout.addWidget(self.button1, 1, 1, 1, 1)

		self.workThread = WorkThread()  # 调用自定义的 WorkThread 类

		self.button.clicked.connect(self.startThread)
		self.workThread.displayNumber.connect(self.lcdDisplay)
		self.workThread.started.connect(self.buttonDisable)
		self.workThread.finished.connect(self.buttonEnable)

		self.button1.clicked.connect(self.button1Clicked)

	def button1Clicked(self):
		print(self.workThread.isRunning())

	def buttonDisable(self):
		self.button.setEnabled(False)

	def buttonEnable(self):
		self.button.setEnabled(True)
		self.workThread.number = 0

	def startThread(self):
		self.workThread.start()  # 线程开始

	def lcdDisplay(self, number):
		self.lcd.display(number)


class WorkThread(QThread):
	number = 0
	displayNumber: pyqtBoundSignal
	displayNumber = pyqtSignal(int)  # 自定义个信号

	def __init__(self):
		super(WorkThread, self).__init__()

	def run(self):
		while True:
			if self.number == 3:
				self.quit()
			if self.number == 5:
				self.displayNumber.emit(self.number)
				break
			else:
				self.displayNumber.emit(self.number)
				time.sleep(1)
				self.number += 1


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = LcdDisplyNumber()
	window.show()
	sys.exit(app.exec_())
