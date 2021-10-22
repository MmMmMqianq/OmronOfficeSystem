import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QPoint
import CoordinateSystemClass


class DrawingLineWithDrawLineDemo(QWidget):
	def __init__(self):
		super(DrawingLineWithDrawLineDemo, self).__init__()
		self.setWindowTitle("用QPainter.drawLine方法画一条直线")
		self.resize(500, 500)

	def paintEvent(self, event):
		CoordinateSystemClass.DrawingCoordinateSystem().paintEvent(self)

		painter = QPainter()
		painter.begin(self)

		painter.setPen(Qt.blue)
		painter.drawLine(20, 40, 300, 290)  # painter.drawLine(x1, y1, x2, y2)
		painter.drawLine(QPoint(20, 30), QPoint(300, 390))  # painter.drawLine(QPoint1, QPoint2)
		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = DrawingLineWithDrawLineDemo()
	window.show()
	sys.exit(app.exec_())
