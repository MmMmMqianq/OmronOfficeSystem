import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QObject, pyqtSignal, pyqtBoundSignal
from PyQt5.QtCore import QSize, Qt
import time
import threading


class QPushButtonDemo(QWidget):
	def __init__(self):
		super(QPushButtonDemo, self).__init__()
		self.setWindowTitle("这是一个QPushButton案例")
		self.setWindowIcon(QIcon("./images/1.ico"))
		self.resize(500, 500)

		self.s = TcpSignals()
		self.s.conn_closed_done.connect(self.a)

		self.t = threading.Thread(target=self.handle)
		# self.t.start()

		self.push_button = QPushButton(self)
		self.push_button.setText("按钮Off")
		self.push_button.setCheckable(True)  # 如果设置为True按钮按下去不会弹起来的，处于被选中的状态
		# self.push_button.setChecked(True)

		# self.push_button.pressed.connect(self.pressed_button)  # 按下去松开为clicked
		self.push_button.clicked.connect(self.clicked_button)  # 按下去为pressed
		# self.push_button.released.connect(self.released_button)  # 松开按钮为released
		# self.push_button.toggled.connect(self.toggled_button)

	def clicked_button(self):
		print(111)
		print(self.push_button.isChecked())
		# self.push_button.setChecked(True)
		# print(self.push_button.isChecked())

	def pressed_button(self):
		self.push_button.setChecked(True)
		self.push_button.setText("按钮on")

	def released_button(self):
		print("按钮released")

	def toggled_button(self):
		print("按钮toggled")

	def handle(self):
		time.sleep(5)
		self.s.conn_closed_done.emit([123])

	def a(self):
		self.push_button.setChecked(True)
		self.push_button.setText("按钮on")


class TcpSignals(QObject):
	conn_closed_done: pyqtBoundSignal
	conn_closed_done = pyqtSignal(list)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QPushButtonDemo()
	widget.show()
	sys.exit(app.exec_())
