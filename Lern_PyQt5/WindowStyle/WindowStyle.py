import sys
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication, QHBoxLayout, QLabel, QStyleFactory
import LoadingGif

class WindowStyle(QWidget):
	def __init__(self):
		super(WindowStyle, self).__init__()

		self.setWindowTitle("设置窗口风格")

		self.label = QLabel("设置窗口风格")
		self.comboBox = QComboBox()
		self.hLayout = QHBoxLayout(self)
		self.hLayout.addWidget(self.label)
		self.hLayout.addWidget(self.comboBox)
		self.comboBox.addItems(QStyleFactory.keys())

		# 获取所有的窗口风格
		print(QStyleFactory.keys())

		self.comboBox.currentIndexChanged.connect(self.setWindowStyle)

	def setWindowStyle(self):
		# 设置窗口的风格
		QApplication.setStyle(self.comboBox.currentText())
		print("当前窗口风格为：", QApplication.style().objectName())  # 获取当前窗口的风格


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = WindowStyle()
	window.show()
	sys.exit(app.exec_())
