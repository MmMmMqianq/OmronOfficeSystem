"""
异形窗口只有Windows下是有效的
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QBitmap, QPaintEvent, QPainter, QPixmap
from PyQt5.Qt import QRect


class IrregulaiWindow(QWidget):
	def __init__(self):
		super(IrregulaiWindow, self).__init__()

		self.setWindowTitle("异形窗口")
		# 创建一个异形蒙板，PNG格式
		self.bitMap = QBitmap(r"/Users/qianshaoqing/Documents/Python/Lern_PyQt5/WindowStyle/images/11.png")
		# 将窗口大小和蒙板图片大小设置为相同
		self.resize(self.bitMap.size())
		# 将蒙板应用到窗口, QWidget.setMask(QBitMap/QRegion)
		self.setMask(self.bitMap)

	def paintEvent(self, a0: QPaintEvent):
		self.painter = QPainter()

		self.painter.begin(self)
		# 绘制窗口图片，图片会自动应用窗口设置的蒙板
		self.painter.drawPixmap(QRect(0, 0, self.width(), self.height()), QPixmap(r"/Users/qianshaoqing/Documents/"
		                                                                          r"Python/Lern_PyQt5/WindowStyle/images/22.jpg"))
		self.painter.end()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = IrregulaiWindow()
	window.show()
	sys.exit(app.exec_())