import sys
import time
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QDateTimeEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal, pyqtBoundSignal, pyqtSlot, QDateTime
import MainWindow


class Window(QDialog):
	def __init__(self):
		super(Window, self).__init__()

		self.setWindowTitle("window2")

		self.countLineEdit = QLineEdit("0")

		self.dateTimeEdit = QDateTimeEdit()
		self.dateTimeEdit.setDisplayFormat("yy-MM-dd hh:mm:ss")

		self.vLayout = QVBoxLayout(self)
		self.vLayout.addWidget(self.countLineEdit)
		self.vLayout.addWidget(self.dateTimeEdit)

		self.workTread = WorkTread()
		self.workTread.countSignal.connect(self.showCount)

	@pyqtSlot(int)
	def showCount(self, number):
		self.countLineEdit.setText(str(number))

	@pyqtSlot(str)
	def showDateTime(self, datetime):
		self.dateTimeEdit.setDateTime(QDateTime.fromString(datetime, "yy-MM-dd hh:mm:ss"))


class WorkTread(QThread):
	countSignal: pyqtBoundSignal
	countSignal = pyqtSignal(int)

	def __init__(self):
		super(WorkTread, self).__init__()
		self.number = 0

	def run(self):
		while 1:
			self.countSignal.emit(self.number)
			time.sleep(1)
			self.number += 1


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())