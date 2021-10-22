import math
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class DrawingCoordinateSystem(QWidget):
	def __init__(self):
		super(DrawingCoordinateSystem, self).__init__()

		self.setWindowTitle("以窗口中心为原点画一个坐标系")
		self.resize(500, 500)

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)
		painter.setPen(Qt.red)
		windowSize = self.size()

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

		xRange = 20  # 用于调节箭头的的大小
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
			# x = windowSize.width()/2 + i*(windowSize.width()/1000)
			y = x - windowSize.width() / 2
			painter.drawPoint(x, y)

		for i in range(1000):
			x = windowSize.width() / 2 - xRange + (xRange / 1000) * i
			y = -x + windowSize.width() / 2
			painter.drawPoint(x, y)
		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = DrawingCoordinateSystem()
	mainWindow.show()
	sys.exit(app.exec_())
