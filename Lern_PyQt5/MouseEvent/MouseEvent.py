import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QPointF


class MouseEvent(QWidget):
	def __init__(self):
		super(MouseEvent, self).__init__()
		self.resize(500, 500)
		self.setMouseTracking(False)  # 如果设置为True只要鼠标移动就会执行mouseMoveEvent事件，设置为False时需要点击鼠标右键才会执行改事件

	def mouseMoveEvent(self, a0: QMouseEvent):
		# 在mouseMoveEvent事件中，button()返回NoButton,即0
		print("鼠标在移动")
		pass

	def mousePressEvent(self, a0: QMouseEvent):
		print("执行了press事件，点击鼠标的按钮为：", a0.button())
		print("a0.windowPos().x() = ", a0.windowPos().x(), "，a0.windowPos().y() = ", a0.windowPos().y())
		print("a0.x() = ", a0.x(), "，a0.y() = ", a0.y())
		print("a0.pos().x() = ", a0.pos().x(), "，a0.pos().y() = ", a0.pos().y())
		print("a0.globalX() = ", a0.globalX(), "，a0.globalY() = ", a0.globalY())
		print("a0.screenPos().x() = ", a0.screenPos().x(), "，a0.screenPos().y() = ", a0.screenPos().y())
		print("a0.localPos().x() = ", a0.localPos().x(), "，a0.localPos().y() = ", a0.localPos().y())

	def mouseReleaseEvent(self, a0: QMouseEvent):
		print("执行了release事件，点击鼠标的按钮为：", a0.button())
		print(a0.flags())

	def mouseDoubleClickEvent(self, a0: QMouseEvent):
		print("执行了DoubleClick事件，点击鼠标的按钮为：", a0.button())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MouseEvent()
	window.show()
	sys.exit(app.exec_())