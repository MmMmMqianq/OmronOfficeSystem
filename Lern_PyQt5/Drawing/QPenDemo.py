import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt


class QPenDemo(QWidget):
	def __init__(self):
		super(QPenDemo, self).__init__()

		self.setWindowTitle("QPen画不同风格的线")
		self.resize(500, 500)

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)

		brush = QBrush()
		# brush.setColor(Qt.blue)
		brush.setStyle(Qt.CrossPattern)
		pen = QPen()
		pen.setBrush(brush)
		# pen.setColor(Qt.blue)  # 经测试QPen在设置QBrush时，不要设置QPen的颜色，否则QBrush的纹理会被覆盖掉，可以给QBrush设定颜色，从而设定线的颜色
		pen.setStyle(Qt.SolidLine)  # 设置线的风格为实线
		pen.setWidth(15)  # 设置线的宽度
		pen.setCapStyle(Qt.RoundCap)  # 设置线为圆角
		pen.setJoinStyle(Qt.BevelJoin)  # 设置两条线之间的连接样式，线的宽度大于1是才有用
		painter.setPen(pen)
		painter.drawLine(10, 20, 490, 20)

		pen.setColor(Qt.red)
		pen.setStyle(Qt.DashLine)
		pen.setWidth(8)
		pen.setCapStyle(Qt.FlatCap)
		pen.setJoinStyle(Qt.RoundJoin)
		painter.setPen(pen)
		painter.drawLine(20, 40, 490, 40)

		pen.setColor(Qt.black)
		pen.setStyle(Qt.CustomDashLine)  # 自定义线的样式
		pen.setDashPattern([2, 5, 4, 6])  # 设置线的样式，2表示第一个虚线点的长度，5表示空格长度，以此类推
		pen.setWidth(8)
		pen.setCapStyle(Qt.FlatCap)
		pen.setJoinStyle(Qt.RoundJoin)
		painter.setPen(pen)
		painter.drawLine(20, 60, 490, 60)

		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QPenDemo()
	window.show()
	sys.exit(app.exec_())
