import sys
from PyQt5.QtWidgets import QApplication, QStatusBar, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QCursor, QMouseEvent


class StatusBarDemo(QMainWindow):
	def __init__(self):
		super(StatusBarDemo, self).__init__()
		self.resize(500, 300)
		self.setWindowTitle("这是一个StatusBar实例")

		self.button1 = QPushButton("按钮1", self)
		self.button1.setToolTip("状态栏消息显示3秒")
		print(id(self.button1))

		self.button2 = QPushButton("按钮2", self)
		self.button2.setToolTip("状态栏消息显示3秒")
		self.button2.move(0, 50)

		self.button3 = QPushButton("清除状态栏消息", self)
		self.button3.resize(150, 30)
		self.button3.move(0, 100)

		self.centralWidget = QWidget(self)
		vLayout = QVBoxLayout(self.centralWidget)
		vLayout.addWidget(self.button1)
		vLayout.addWidget(self.button2)
		vLayout.addWidget(self.button3)
		self.setCentralWidget(self.centralWidget)

		self.statusBar = QStatusBar()
		self.statusBar.setWindowTitle("状态栏")
		self.setStatusBar(self.statusBar)

		self.button1.clicked.connect(self.showButtonInfo)
		self.button2.clicked.connect(self.showButtonInfo)
		self.button3.clicked.connect(self.clearStatusBarMessage)

		# 开启鼠标追踪
		self.setMouseTracking(True)
		self.centralWidget.setMouseTracking(True)

	def mouseMoveEvent(self, event: QMouseEvent):  # 当鼠标追踪被开启时移动鼠标执行该事件，如果没有开启鼠标追踪鼠标点击时也会触发该事件
		# self.mouse = QCursor()
		# print(self.mouse.pos())
		if self.statusBar.currentMessage().find("按钮") == -1:
			windowPosX = event.windowPos().x()
			windowPosY = event.windowPos().y()
			self.statusBar.showMessage("x:%f y:%f" % (windowPosX, windowPosY))
		else:
			event.ignore()

	def mousePressEvent(self, event: QMouseEvent):
		self.statusBar.showMessage("鼠标被按下了")

	def mouseReleaseEvent(self, event: QMouseEvent):
		self.statusBar.showMessage("鼠标被松开了")

	def mouseDoubleClickEvent(self, event: QMouseEvent):
		self.statusBar.showMessage("鼠标被双击了")

	def showButtonInfo(self):
		sender = self.sender()
		buttonName = sender.text()
		buttonHeight = sender.size().height()
		buttonWidth = sender.size().width()
		message = buttonName + "被触发，" + "宽度为：" + str(buttonWidth) + "，高度为：" + str(buttonHeight)
		if sender == self.button1:
			self.statusBar.showMessage(message, 3000)  # QStatusBar.showMessage(str, int)  # int为显示的时间，默认为0表示一直显示
		else:
			self.statusBar.showMessage(message, 0)

	def clearStatusBarMessage(self):
		self.statusBar.clearMessage()
		self.statusBar.showMessage("状态栏消息已被清除", 1000)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = StatusBarDemo()
	window.show()
	sys.exit(app.exec_())
