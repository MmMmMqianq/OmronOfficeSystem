import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class WindowPattern(QWidget):
	def __init__(self):
		super(WindowPattern, self).__init__()

		self.setWindowTitle("窗口最大化和最小化")
		self.resize(500, 500)

		self.maximumButton = QPushButton("最大化窗口")
		self.minimumButton = QPushButton("最小化窗口")
		self.fullScreenButton = QPushButton("窗口全屏")
		self.normalButton = QPushButton("常规窗口")

		self.vLayout = QVBoxLayout(self)
		self.vLayout.addWidget(self.maximumButton)
		self.vLayout.addWidget(self.minimumButton)
		self.vLayout.addWidget(self.fullScreenButton)
		self.vLayout.addWidget(self.normalButton)

		self.maximumButton.clicked.connect(self.showMaximized)
		self.minimumButton.clicked.connect(self.showMinimized)
		self.fullScreenButton.clicked.connect(self.showFullScreen)
		self.normalButton.clicked.connect(self.showNormal)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = WindowPattern()
	window.show()
	sys.exit(app.exec_())