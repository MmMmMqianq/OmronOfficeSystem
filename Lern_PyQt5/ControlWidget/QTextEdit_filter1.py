import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit
from PyQt5.QtGui import QKeyEvent
import string


class KeyEventDemo(QWidget):
	def __init__(self):
		super(KeyEventDemo, self).__init__()
		self.resize(500, 500)
		self.setMouseTracking(False)
		self.te = TextEdit()
		self.te.setParent(self)


class TextEdit(QTextEdit):
	def __init__(self):
		super(TextEdit, self).__init__()

	def keyPressEvent(self, e: QKeyEvent) -> None:
		QTextEdit.keyPressEvent(self, e)
		# 下面写自己需要过滤的代码
		if e.text() not in string.hexdigits:  # 只有当输入的字符为a时才能显示在QTextEdit中
			if e.key() != 16777219:
				self.textCursor().deletePreviousChar()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = KeyEventDemo()
	window.show()
	sys.exit(app.exec_())
