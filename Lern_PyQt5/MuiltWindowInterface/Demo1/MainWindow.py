"""
使用QDialog返回值实现窗口间的通信
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
import Dialog1

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle("这是一个多窗口交互实例")
		self.centralwidget = QWidget()

		self.getTimeButton = QPushButton("点击获取时间")
		self.getDataButton = QPushButton("点击获取日期")

		# 设置label的背景颜色
		self.p = QPalette()
		self.p.setColor(QPalette.Base, Qt.cyan)

		self.timeLabel = QLabel("hh:mm:ss")
		self.timeLabel.setPalette(self.p)
		self.timeLabel.setBackgroundRole(QPalette.Base)
		self.timeLabel.setAutoFillBackground(True)

		self.dataLabel = QLabel("yyyy-MM-dd")
		self.dataLabel.setPalette(self.p)
		self.dataLabel.setBackgroundRole(QPalette.Base)
		self.dataLabel.setAutoFillBackground(True)

		self.gLayout = QGridLayout(self.centralwidget)
		self.gLayout.addWidget(self.getDataButton, 0, 0, 1, 1)
		self.gLayout.addWidget(self.dataLabel, 0, 1, 1, 1)
		self.gLayout.addWidget(self.getTimeButton, 1, 0, 1, 1)
		self.gLayout.addWidget(self.timeLabel, 1, 1, 1, 1)
		self.setCentralWidget(self.centralwidget)

		self.getDataButton.clicked.connect(self.getDateTime)
		self.getTimeButton.clicked.connect(self.getDateTime)

	def getDateTime(self):
		dialog = Dialog1.GetDateAndTime()
		self.result = dialog.exec_()

		if self.sender().text() == "点击获取日期":
			if self.result == 1:
				self.dataLabel.setText(dialog.dateTime.date().toString("yyyy-MM-dd"))

		if self.sender().text() == "点击获取时间":
			if self.result == 1:
				self.timeLabel.setText(dialog.dateTime.time().toString("hh:mm:ss"))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())