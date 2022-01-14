import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class QProgressBarExample(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.progressbar_obj1 = QProgressBar(self)
		self.progressbar_obj1.setGeometry(30, 40, 200, 25)
		self.button_obj1 = QPushButton(u'开始', self)
		self.button_obj1.move(40, 80)
		self.button_obj1.clicked.connect(self.on_button_clicked)

		self.timer_obj1 = QBasicTimer()
		self.step = 0
		# 窗口的大小,前面两个参数是位置信息
		# 后面两个参数是宽度和高度信息
		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle(u'QProgressBar的演示程序')
		self.show()

	# 定时器处理函数
	def timerEvent(self, e):
		if self.step >= 100:
			self.timer_obj1.stop()
			self.button_obj1.setText(u'重新开始')
			return
		self.step = self.step + 1
		self.progressbar_obj1.setValue(self.step)

	def on_button_clicked(self):  # 按钮被单击后的处理函数
		# 已经走到头了，重新启动起来
		if self.progressbar_obj1.value() >= 100:
			self.step = 0
			self.progressbar_obj1.setValue(0)
			self.timer_obj1.start(100, self)
			self.button_obj1.setText(u'暂停')
		else:
			if self.timer_obj1.isActive():  # 如果正在运行中，那么暂停
				self.timer_obj1.stop()
				self.button_obj1.setText(u'继续')
			else:  # 如果处于暂停状态，那么启动起来
				self.timer_obj1.start(100, self)
				self.button_obj1.setText(u'暂停')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_win = QProgressBarExample()
	sys.exit(app.exec_())