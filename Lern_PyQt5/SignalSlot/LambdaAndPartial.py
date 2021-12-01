import sys
import functools
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QMetaObject, pyqtBoundSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QCheckBox


class AutoConnectSignalAndSlot(QWidget):
	a = pyqtSignal()

	def __init__(self):
		super(AutoConnectSignalAndSlot, self).__init__()
		self.setWindowTitle("AutoConnectSignalAndSlot demo")
		self.resize(500, 500)

		self.button = QPushButton(self)
		self.button.setObjectName("okButton")
		self.button.setText("ok")

		# 使用lambda和functools.partial为槽函数添加参数
		self.button.clicked.connect(lambda: self.okButtonClicked(10, "asd"))
		self.button.pressed.connect(functools.partial(self.okButtonPressed, 5, "asd"))

	@pyqtSlot(int, int)
	def okButtonClicked(self, a, b):
		print(a, b)

	@pyqtSlot(int, str)
	def okButtonPressed(self, a, b):
		print(a, b)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = AutoConnectSignalAndSlot()
	window.show()
	sys.exit(app.exec_())