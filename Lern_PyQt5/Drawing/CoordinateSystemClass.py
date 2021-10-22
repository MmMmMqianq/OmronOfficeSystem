import math
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class DrawingCoordinateSystem():
	def paintEvent(self, window: QWidget):
		painter = QPainter()
		painter.begin(window)
		painter.setPen(Qt.red)
		windowSize = window.size()

		# 画X轴
		for i in range(windowSize.width()):
			xAxis = i
			yAxis = windowSize.height()/2
			painter.drawPoint(xAxis, yAxis)

		# 画Y轴
		for i in range(windowSize.height()):
			xAxis = windowSize.width()/2
			yAxis = i
			painter.drawPoint(xAxis, yAxis)

		xRange = 5  # 用于调节箭头的的大小
		# 画X轴箭头
		for i in range(1000):
			x = windowSize.width() - xRange + (xRange / 1000) * i
			y = x + (windowSize.height() - 2 * windowSize.width()) / 2
			painter.drawPoint(x, y)

		for i in range(1000):
			x = windowSize.width() - xRange + (xRange / 1000) * i
			y = -x + (windowSize.height() + 2 * windowSize.width()) / 2
			painter.drawPoint(x, y)

		# 画Y轴箭头
		for i in range(1000):
			x = windowSize.width() / 2 + (xRange / 1000) * i
			y = x - windowSize.width() / 2
			painter.drawPoint(x, y)

		for i in range(1000):
			x = windowSize.width() / 2 - xRange + (xRange / 1000) * i
			y = -x + windowSize.width() / 2
			painter.drawPoint(x, y)
		painter.end()

