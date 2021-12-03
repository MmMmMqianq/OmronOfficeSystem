import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QComboBox, QApplication, QHBoxLayout, QLabel, QStyleFactory
from PyQt5.QtCore import Qt


class WindowPattern(QMainWindow):
	def __init__(self):
		super(WindowPattern, self).__init__()

		self.setWindowTitle("设置窗口模式")
		self.resize(500, 500)

		# setWindowFlags(Qt.WindowType)
		self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

		self.setObjectName("MainWindow")
		self.setStyleSheet("#MainWindow{border-image:url(images/1.jpg);}")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = WindowPattern()
	window.show()
	sys.exit(app.exec_())
