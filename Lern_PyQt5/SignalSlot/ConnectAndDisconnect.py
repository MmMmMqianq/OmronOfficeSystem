import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QMetaObject, pyqtBoundSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class ConnectAndDisconnect(QWidget):
	def __init__(self):
		super(ConnectAndDisconnect, self).__init__()
		self.setWindowTitle("WorkTread and slot demo")
		self.resize(500, 500)

		# 信号和槽的连接和断开
		self.button = QPushButton(self)
		self.button.setText("点击执行clicked信号所连接的槽函数a")
		self.button.setEnabled(False)

		self.button3 = QPushButton(self)
		self.button3.move(0, 100)
		self.button3.setText("点击连接clicked信号所连接的槽函数")

		self.button2 = QPushButton(self)
		self.button2.setText("点击断开clicked信号所连接的槽函数")
		self.button2.move(0, 200)
		self.button2.setEnabled(False)

		self.button2.clicked.connect(self.disconnect)
		self.button3.clicked.connect(self.connect)

	def on_clicked(self):
		print("{}连接，执行了button按钮clicked信号所连接的槽函数a".format(self.meta_object))

	def connect(self):
		print("连接了button按钮clicked信号所连接的槽函数")
		self.meta_object = self.button.clicked.connect(self.on_clicked)  # 建立信号和槽的连接，并将获取连接
		print("self.button.clicked.connect(self.a)建立的连接为：", self.meta_object)
		self.button3.setEnabled(False)  # 如果不把建立连接的按钮设置为不可用，那么每点一次按钮就会建立一个信号和槽的连接
		self.button2.setEnabled(True)
		self.button.setEnabled(True)

	def disconnect(self):
		print("断开了button按钮clicked信号所连接的槽函数")
		self.button.clicked.disconnect(self.meta_object)  # 关闭建立的连接
		print("self.button.clicked.disconnect(self.a)断开的连接为：", self.meta_object)
		self.button3.setEnabled(True)
		self.button2.setEnabled(False)
		self.button.setEnabled(False)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ConnectAndDisconnect()
	window.show()
	sys.exit(app.exec_())