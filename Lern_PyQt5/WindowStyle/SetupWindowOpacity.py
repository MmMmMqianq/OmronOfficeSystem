"""
通过滑块设置窗口透明度
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QSlider, QGraphicsOpacityEffect, QPushButton
from PyQt5.QtCore import Qt


class WindowOpacity(QWidget):
	def __init__(self):
		super(WindowOpacity, self).__init__()

		self.setWindowTitle("设置窗口模式")
		self.resize(500, 500)

		self.button = QPushButton("按钮", self)

		self.slider = QSlider(self)
		self.slider.setOrientation(Qt.Horizontal)
		self.slider.setRange(0, 100)
		self.slider.setValue(100)
		self.slider.resize(200, 30)
		self.slider.move(100, 250)
		self.slider.sliderMoved.connect(self.setOpacity)

	def setOpacity(self, position: int):
		# 设置窗口透明度
		self.setWindowOpacity(0.8)  # 透明度范围为0.0-1.0

		# 设置控件透明度，可以用setWindowOpacity或者下面方法，也可以通过QSS设置
		self.opacity = QGraphicsOpacityEffect()
		self.opacity.setOpacity(position/100)
		self.button.setGraphicsEffect(self.opacity)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = WindowOpacity()
	window.show()
	sys.exit(app.exec_())
