from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
import sys
import Widget1


class MainWindow(QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setWindowTitle("弹出QWidget窗口")
		self.resize(300, 200)

		self.button = QPushButton("弹出窗口", self)
		self.button.clicked.connect(self.popUpWindow)
		self.window1 = Widget1.Window1()  # 必须为类的属性(加self),变量会被自动销毁，窗口只会显示一次

	def popUpWindow(self):
		self.window1.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())