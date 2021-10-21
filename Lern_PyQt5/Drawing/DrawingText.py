import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import Qt, QPoint


class DrawingText(QWidget):
	def __init__(self):
		super(DrawingText, self).__init__()

		self.setWindowTitle("这是绘制文本实例")
		self.resize(300, 300)

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)

		painter.setPen(Qt.blue)
		painter.setFont(QFont("SimSum", 25))

		painter.drawText(QPoint(50, 80), "你好啊哦哈啦")

		painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = DrawingText()
	mainWindow.show()
	sys.exit(app.exec_())
