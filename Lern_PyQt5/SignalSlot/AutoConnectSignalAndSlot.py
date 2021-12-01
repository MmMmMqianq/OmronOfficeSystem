"""
自动将信号和槽关联上：
1. 用QObject.setObjectName设置控件的名字
2. 创建槽函数，函数名字为 on_<object name>_<WorkTread name>(<WorkTread parameters>)
3. 用QMetaObject.connectSlotByName()自动连接信号和槽，递归搜索给定对象的所有子对象，并将来自它们的匹配信号连接到槽。
"""

import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QMetaObject, pyqtBoundSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QCheckBox


class AutoConnectSignalAndSlot(QWidget):
	a = pyqtSignal()

	def __init__(self):
		super(AutoConnectSignalAndSlot, self).__init__()
		self.setWindowTitle("WorkTread and slot demo")
		self.resize(500, 500)

		self.button = QPushButton(self)
		self.button.setObjectName("okButton")
		self.button.setText("ok")

		QMetaObject.connectSlotsByName(self)

	@pyqtSlot()
	def on_okButton_clicked(self):
		print("asdadasdas")

	@pyqtSlot()
	def on_okButton_pressed(self):
		print("asdadasdas")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = AutoConnectSignalAndSlot()
	window.show()
	sys.exit(app.exec_())