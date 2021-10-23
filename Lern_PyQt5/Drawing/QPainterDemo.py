import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygonF
from PyQt5.QtCore import Qt, QRectF, QPointF, QSizeF


class QPainterDemo(QWidget):
	def __init__(self):
		super(QPainterDemo, self).__init__()

		self.setWindowTitle("这是一个QPainter实例")
		self.resize(600, 800)

	def paintEvent(self, event):
		painter = QPainter()

		pen1 = QPen()
		pen1.setColor(Qt.red)
		pen1.setWidthF(1.5)
		pen1.setStyle(Qt.SolidLine)
		pen1.setCapStyle(Qt.RoundCap)
		pen1.setJoinStyle(Qt.RoundJoin)

		pen2 = QPen()
		pen2.setColor(Qt.black)
		pen2.setWidthF(0.5)
		pen2.setStyle(Qt.DashLine)
		pen2.setCapStyle(Qt.RoundCap)
		pen2.setJoinStyle(Qt.RoundJoin)

		brush = QBrush()
		brush.setColor(Qt.cyan)
		brush.setStyle(Qt.SolidPattern)

		painter.begin(self)

		painter.setPen(pen1)
		# 画直线
		painter.drawLine(20, 50, 100, 50)
		# 画矩形
		painter.drawRect(120, 20, 100, 100)
		# 画弧线，以指定的矩形的中心作为圆心画弧线
		painter.setPen(pen2)
		painter.drawRect(QRectF(240.00, 20.00, 50.00, 100.00))
		painter.setPen(pen1)
		painter.drawArc(QRectF(240.00, 20.00, 50.00, 100.100), 0.0, 90.00*16.00)
		# 画带弦的弧线
		painter.setPen(pen2)
		painter.drawRect(QRectF(360.00, 20.00, 50.00, 100.00))
		painter.setPen(pen1)
		painter.drawChord(QRectF(360.00, 20.00, 50.00, 100.100), 0.0, 90.00*16.00)
		# 画多边形
		point1 = QPointF(500.00, 20.00)
		point2 = QPointF(560.00, 20.00)
		point3 = QPointF(580.00, 70.00)
		point4 = QPointF(560.00, 120.00)
		point5 = QPointF(500.00, 120.00)
		point6 = QPointF(480.00, 70.00)
		polygon1 = QPolygonF([point1, point2, point3, point4, point5, point6])
		painter.drawConvexPolygon(polygon1)
		# 画凸多边形
		point7 = QPointF(40.00, 140.00)
		point8 = QPointF(100.00, 140.00)
		point9 = QPointF(120.00, 190.00)
		point10 = QPointF(100.00, 240.00)
		point11 = QPointF(40.00, 240.00)
		point12 = QPointF(20.00, 190.00)
		polygon2 = QPolygonF([point7, point8, point9, point10, point11, point12])
		painter.drawPolygon(polygon2, Qt.OddEvenFill)

		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QPainterDemo()
	window.show()
	sys.exit(app.exec_())
