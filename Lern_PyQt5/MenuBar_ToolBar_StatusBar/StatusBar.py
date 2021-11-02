import sys
from PyQt5.QtWidgets import QApplication, QStatusBar, QMainWindow, QPushButton, QVBoxLayout


class StatusBarDemo(QMainWindow):
	def __init__(self):
		super(StatusBarDemo, self).__init__()
		self.resize(500, 300)
		self.setWindowTitle("这是一个StatusBar实例")

		self.button1 = QPushButton("按钮1", self)
		self.button1.setToolTip("状态栏消息显示3秒")

		self.button2 = QPushButton("按钮2", self)
		self.button2.setToolTip("状态栏消息显示3秒")
		self.button2.move(0, 50)

		self.button3 = QPushButton("清除状态栏消息", self)
		self.button3.resize(150, 30)
		self.button3.move(0, 100)

		self.statusBar = QStatusBar()
		self.statusBar.setWindowTitle("状态栏")
		self.setStatusBar(self.statusBar)

		self.button1.clicked.connect(self.showButtonInfo)
		self.button2.clicked.connect(self.showButtonInfo)
		self.button3.clicked.connect(self.clearStatusBarMessage)

	def showButtonInfo(self):
		sender = self.sender()
		print(sender)
		buttonName = sender.text()
		buttonHeight = sender.size().height()
		buttonWidth = sender.size().width()
		message = buttonName + "被触发，" + "宽度为：" + str(buttonWidth) + "，高度为：" + str(buttonHeight)
		self.statusBar.showMessage(message, 3000)  # QStatusBar.showMessage(str, int)  # int为显示的时间，默认为0表示一直显示

	def clearStatusBarMessage(self):
		self.statusBar.clearMessage()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = StatusBarDemo()
	window.show()
	sys.exit(app.exec_())
