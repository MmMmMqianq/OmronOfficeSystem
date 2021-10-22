import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication
import CoordinateSystemClass


class DrawingStraightLine(QWidget):
	"""
	使用QPainter.point()方法画出一条直线
	"""
	def __init__(self):
		super(DrawingStraightLine, self).__init__()

		self.setWindowTitle("绘制正比例函数")
		self.resize(500, 500)

	def paintEvent(self, event):
		CoordinateSystemClass.DrawingCoordinateSystem().paintEvent(self)
		painter = QPainter()
		painter.begin(self)

		painter.setPen(Qt.blue)

		windowSize = self.size()
		x = float()
		y = float()

		for i in range(1000):
			x = (windowSize.width()/1000)*i
			y = -x + (windowSize.width()+windowSize.height())/2
			painter.drawPoint(x, y)

		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = DrawingStraightLine()
	widget.show()
	sys.exit(app.exec_())
