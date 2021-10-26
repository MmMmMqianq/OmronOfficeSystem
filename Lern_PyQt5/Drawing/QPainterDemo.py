import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygonF, QImage, QPixmap, QStaticText, QFont
from PyQt5.QtCore import Qt, QRectF, QPointF, QSizeF, QRect


class QPainterDemo(QWidget):
	def __init__(self):
		super(QPainterDemo, self).__init__()

		self.setWindowTitle("这是一个QPainter实例")
		self.resize(620, 400)

		self.eraseButton = QPushButton(self)
		self.eraseButton.setText("擦除填充")
		self.eraseButton.resize(80, 30)
		self.eraseButton.move(500 + int((100 - self.eraseButton.width()) / 2), 360)
		self.eraseButton.setCheckable(True)
		# self.eraseButton.toggled.connect(self.update)  # QWidget.update()/repaint()会自动调用paintEvent事件
		self.eraseButton.toggled.connect(self.repaint)

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
		print("1. ", painter.device())  # 获取在什么地方绘画,由painter.begin(self)指定，本实例是在QPainterDemo上绘画
		print("2. painter.isActive() = ",painter.isActive())

		painter.setPen(pen1)
		# 画直线
		painter.drawLine(20, 50, 100, 50)
		# 画矩形
		painter.drawRect(120, 20, 100, 100)

		# 画弧线，以指定的矩形的中心作为圆心画弧线
		painter.setPen(pen2)
		painter.drawRect(QRect(240, 20, 50, 100))
		painter.setPen(pen1)
		painter.drawArc(QRect(240, 20, 50, 100), 0, 90*16)

		# 画带弦的弧线
		painter.setPen(pen2)
		painter.drawRect(QRect(360, 20, 50, 100))
		painter.setPen(pen1)
		painter.drawChord(QRect(360, 20, 50, 100), 0, 90*16)
		# 画凸多边形
		point1 = QPointF(500.00, 20.00)
		point2 = QPointF(560.00, 20.00)
		point3 = QPointF(580.00, 70.00)
		point4 = QPointF(560.00, 120.00)
		point5 = QPointF(500.00, 120.00)
		point6 = QPointF(480.00, 70.00)
		polygon1 = QPolygonF([point1, point2, point3, point4, point5, point6])
		painter.drawConvexPolygon(polygon1)
		# 画多边形
		point7 = QPointF(40.00, 140.00)
		point8 = QPointF(100.00, 140.00)
		point9 = QPointF(120.00, 190.00)
		point10 = QPointF(100.00, 240.00)
		point11 = QPointF(40.00, 240.00)
		point12 = QPointF(20.00, 190.00)
		polygon2 = QPolygonF([point7, point8, point9, point10, point11, point12])
		painter.drawPolygon(polygon2, Qt.OddEvenFill)

		# 画椭圆
		rect1 = QRectF(140.00, 170.00, 100.00, 40.00)
		painter.setPen(pen2)
		painter.drawRect(rect1)
		painter.setPen(pen1)
		painter.drawEllipse(rect1)

		# 画image
		rect2 = QRectF(260.00, 140.00, 100.00, 100.00)
		painter.setPen(pen2)
		painter.drawRect(rect2)
		image = QImage("./images/2.png")
		painter.drawImage(rect2, image)

		# 画pixmap
		rect3 = QRect(380, 140, 100, 100)
		painter.setPen(pen2)
		painter.drawRect(rect3)
		pixmap = QPixmap("./images/1.ico")
		painter.drawPixmap(rect3, pixmap)  # 只能为QRect，不能为QRectF

		# 画扇形
		rect4 = QRect(500, 140, 100, 100)
		painter.setPen(pen2)
		painter.drawRect(rect4)
		painter.setPen(pen1)
		painter.drawPie(rect4, 0, 90 * 16)

		# 画折线
		point13 = QPointF(20.00, 260.00)
		point14 = QPointF(40.00, 320.00)
		point15 = QPointF(80.00, 290.00)
		point16 = QPointF(120.00, 360.00)
		painter.setPen(pen1)
		painter.drawPolyline(point13, point14, point15, point16)

		# 画圆角矩形
		rect5 = QRectF(140.00, 260.00, 100.00, 100.00)
		painter.drawRoundedRect(rect5, 20, 20)

		# 画静态文字
		staticText = QStaticText("你好啊")
		point17 = QPointF(260.00, 260.00)
		painter.setPen(pen1)
		painter.drawStaticText(point17, staticText)

		# 画文字
		point18 = QPointF(380.00, 270.00)
		painter.drawText(point18, "哈哈哈哈")

		# 擦除矩形填充
		self.rect6 = QRect(500, 260, 100, 100)
		painter.drawRect(self.rect6)
		painter.fillRect(self.rect6, brush)
		if self.eraseButton.isChecked():
			painter.eraseRect(self.rect6)
			self.eraseButton.setText("填充颜色")
		else:
			self.eraseButton.setText("擦除填充")

		painter.end()
		print("3. painter.isActive() = ", painter.isActive())

	# def update(self):
	# 	painter = QPainter()
	# 	painter.begin(self)
	# 	painter.drawRect(120, 400, 100, 100)
	# 	painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QPainterDemo()
	window.show()
	sys.exit(app.exec_())
