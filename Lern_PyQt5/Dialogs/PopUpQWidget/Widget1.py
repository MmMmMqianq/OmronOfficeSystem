from PyQt5.QtWidgets import QDialog, QPushButton, QApplication, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
import sys


class Window1(QWidget):
	def __init__(self):
		super(Window1, self).__init__()
		self.setWindowTitle("弹窗")
		self.resize(200, 100)
		self.setWindowModality(Qt.ApplicationModal)  # 设置窗口的模态


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = Window1()
	mainWindow.show()
	sys.exit(app.exec_())