import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt


class QBrushDemo(QWidget):
	def __init__(self):
		super(QBrushDemo, self).__init__()

		self.setWindowTitle("QPen画不同风格的线")
		self.resize(500, 500)

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)

		brush1 = QBrush()
		brush1.setColor(Qt.cyan)
		brush1.setStyle(Qt.CrossPattern)
		painter.setBrush(brush1)  # 用于填充矩形
		pen1 = QPen()
		pen1.setColor(Qt.darkCyan)
		painter.setPen(pen1)  # 用于描矩形的边
		painter.drawRect(20, 20, 50, 50)

		brush2 = QBrush()
		brush2.setColor(Qt.red)
		brush2.setStyle(Qt.CrossPattern)
		brush2.swap(brush1)  # 交换brush2和brush1
		painter.setBrush(brush2)  # 用于填充矩形
		pen2 = QPen()
		pen2.setColor(Qt.darkGreen)
		painter.setPen(pen2)  # 用于描矩形的边
		painter.drawRect(40, 40, 50, 50)

		painter.setBrush(brush1)  # 上面使用了brush2.swap(brush1)将两把刷子交换
		pen3 = QPen()
		pen3.setColor(Qt.blue)
		painter.setPen(pen3)  # 用于描矩形的边
		painter.drawRect(60, 60, 50, 50)

		brush3 = QBrush()
		brush3.setTexture(QPixmap("./images/1.ico"))  # 使用像素图作为填充
		painter.setBrush(brush3)
		painter.drawRect(80, 80, 50, 50)

		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QBrushDemo()
	window.show()
	sys.exit(app.exec_())
