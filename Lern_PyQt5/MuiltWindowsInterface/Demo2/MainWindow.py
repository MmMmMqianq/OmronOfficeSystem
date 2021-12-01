"""
用信号和槽的方法实现多窗口之间的通信
"""
import sys
import time

from PyQt5.QtWidgets import QApplication, QPushButton, QDateTimeEdit, QWidget, QVBoxLayout, QLineEdit, QDialog
from PyQt5.QtCore import pyqtSignal, pyqtBoundSignal, QThread, pyqtSlot, QDateTime
import Dialog1


class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()

		self.setWindowTitle("window1")
		self.countLineEdit = QLineEdit()
		self.dateTimeEdit = QDateTimeEdit()
		self.dateTimeEdit.setDisplayFormat("yy-MM-dd hh:mm:ss")
		self.popUpWindowButton = QPushButton("打开同步窗口")
		self.vLayout = QVBoxLayout(self)
		self.vLayout.addWidget(self.countLineEdit)
		self.vLayout.addWidget(self.dateTimeEdit)
		self.vLayout.addWidget(self.popUpWindowButton)

		self.popUpWindowButton.clicked.connect(self.popUpWindow)

	def popUpWindow(self):
		self.dialog = Dialog1.Window()
		# 子窗口向父窗口发送数据
		subWorkThread = Dialog1.WorkTread()
		subWorkThread.start()
		subWorkThread.countSignal.connect(self.showCount)

		# 父窗口向子窗口发送数据
		workTread = WorkThread()
		workTread.start()
		workTread.refreshDateTime.connect(self.a)
		workTread.refreshDateTime.connect(self.showDateTime)

		self.dialog.exec_()

	@pyqtSlot(int)
	def showCount(self, number):
		self.countLineEdit.setText(str(number))
		self.dialog.countLineEdit.setText(str(number))

	@pyqtSlot(str)
	def showDateTime(self, datetime):
		self.dateTimeEdit.setDateTime(QDateTime.fromString(datetime, "yy-MM-dd hh:mm:ss"))

	@pyqtSlot(str)
	def a(self, datetime):
		self.dialog.dateTimeEdit.setDateTime(QDateTime.fromString(datetime, "yy-MM-dd hh:mm:ss"))


class WorkThread(QThread):
	refreshDateTime: pyqtBoundSignal
	refreshDateTime = pyqtSignal(str)

	def __init__(self):
		super(WorkThread, self).__init__()

	def run(self):
		while 1:
			dateTime = QDateTime.currentDateTime().toString("yy-MM-dd hh:mm:ss")
			self.refreshDateTime.emit(dateTime)
			time.sleep(1)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
