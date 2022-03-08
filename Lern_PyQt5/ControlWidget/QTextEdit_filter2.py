import sys
import string
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit
from PyQt5.QtCore import QEvent, QObject


# 首先创建一个KeyPressEster类，用于拦截监控对象的按键
class KeyPressEster(QObject):
	def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:  # a0为当前监控的对象，a1为触发的事件
		if a1.type() == QEvent.KeyPress:
			print("按键：", a1.text())
			if a1.text() in string.hexdigits:  # 只能输入16进制的数
				a0.textCursor().insertText(a1.text())
			if a1.key() == 16777219:  # 当按下推个键时，删除字符
				a0.textCursor().deletePreviousChar()
			return True
		else:
			return QObject.eventFilter(self, a0, a1)


class FilterDemo(QWidget):
	def __init__(self):
		super(FilterDemo, self).__init__()
		self.resize(500, 500)
		self.te = QTextEdit(self)
		keyPressEster = KeyPressEster(self)
		self.te.installEventFilter(keyPressEster)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = FilterDemo()
	window.show()
	sys.exit(app.exec_())
