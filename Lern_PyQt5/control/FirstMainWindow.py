import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
	def __init__(self):
		super(FirstMainWin, self).__init__()

		# 设置主窗口标标题
		self.setWindowTitle("This is FirstMainWindow")

		# 设置主窗口大小
		self.resize(600, 500)
		self.status = self.statusBar()
		self.status.showMessage("只存在5秒的消息", 5000)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("./images/1.ico"))
	main = FirstMainWin()
	main.show()
	sys.exit(app.exec_())