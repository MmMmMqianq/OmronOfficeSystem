import sys
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QCloseEvent


class QuitApplication(QMainWindow):
	def __init__(self):
		super(QuitApplication, self).__init__()
		self.resize(400, 500)
		self.setWindowTitle("这是一个退出应用程序的实例")

		# 添加一个Button用于退出APP
		self.button = QPushButton("退出应用程序")
		self.button.clicked.connect(self.onClicked_Button)
		# 创建一个水平布局，并将button放到水平布局中
		layout = QHBoxLayout()
		layout.addWidget(self.button)
		# 创建一个Widget，将水平布局放到Widget中
		mainFrame = QWidget()
		mainFrame.setLayout(layout)
		# 将mainFrame充满整个窗口
		self.setCentralWidget(mainFrame)

	# 添加一个槽，按下button按钮时关闭APP
	def onClicked_Button(self):
		sender = self.sender()
		print(sender.text() + "被按下")
		# self.statusBar().showMessage(sender.text() + " was pressed")
		app = QApplication.instance()
		# 退出应用程序
		app.quit()

	def closeEvent(self, a0: QCloseEvent):
		# 应用程序关闭时触发的事件，点击叉号关闭窗口
		# close()也可以触发
		print(123)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = QuitApplication()
	main.show()
	sys.exit(app.exec_())
