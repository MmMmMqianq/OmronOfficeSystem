import math
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication
import CoordinateSystemClass


class DrawingPoints(QWidget):
	def __init__(self):
		super(DrawingPoints, self).__init__()

		self.setWindowTitle("绘制2周期的正弦函数")
		self.resize(500, 500)

	def paintEvent(self, event):
		CoordinateSystemClass.DrawingCoordinateSystem().paintEvent(self)
		painter = QPainter()
		painter.begin(self)
		painter.setPen(Qt.blue)
		windowSize = self.size()
		windowSize.width()

		# 绘制2周期的正弦函数
		for i in range(1000):
			x = windowSize.width()/2.0 + (math.pi * (-2.0) + (math.pi * 2.00 * i) / 500)
			y = -50 * math.sin(x - windowSize.width()/2.0) + windowSize.height()/2.0

			painter.drawPoint(x, y)
		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = DrawingPoints()
	mainWindow.show()
	sys.exit(app.exec_())
