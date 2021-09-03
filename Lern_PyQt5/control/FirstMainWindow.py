import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import PyQt5.QtWidgets


class FirstMainWin(QMainWindow):
	def __init__(self, parent=None):
		super(FirstMainWin, self).__init__(parent)
		self.setWindowTitle("This is FirstMainWindow")
		self.resize(400, 500)
		self.status = self.statusBar()
		self.status.showMessage("只存在5秒的消息", 5000)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("/images/1.ico"))
	main = FirstMainWin()
	main.show()
	sys.exit(app.exec_())