import sys
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget


class ShowTime(QMainWindow):
	def __init__(self):
		super(ShowTime, self).__init__()

		self.setWindowTitle("显示时钟")

		self.label = QLabel()
		self.label2 = QLabel()
		self.startButton = QPushButton("start")
		self.stopButton = QPushButton("stop")

		# 1. 定义一个定时器
		self.timer1 = QTimer()
		self.timer2 = QTimer()  # 用于显示timer1定时器的剩余时间
		# self.timer1.setInterval(1000)  # 也可以通过QTimer.start(1000)来设置定时时间
		# self.timer1.setSingleShot(True)  # 设置为True时，启动QTimer.start只进行一次定时就结束了
		self.timer1.setTimerType(Qt.PreciseTimer)  # 设置定时器的类型，Qt.PreciseTimer毫秒定时器，Qt.CoarseTimer 误差为5%的毫秒定时器，Qt.VeryCoarseTimer 秒定时器

		self.timer1.timeout.connect(self.showDateTime)  # 在定时时间到时产生一个信号
		self.timer2.timeout.connect(self.showRemainingTime)

		self.centralwidget = QWidget()
		self.gLayout = QGridLayout(self.centralwidget)
		self.gLayout.addWidget(self.label, 0, 0, 1, 3)
		self.gLayout.addWidget(self.startButton, 1, 0, 1, 1)
		self.gLayout.addWidget(self.label2, 1, 1, 1, 1)
		self.gLayout.addWidget(self.stopButton, 1, 2, 1, 1)
		self.setCentralWidget(self.centralwidget)

		self.startButton.clicked.connect(self.startTimer)
		self.stopButton.clicked.connect(self.stopTimer)

	def showDateTime(self):
		currentDateTime = QDateTime.currentDateTime()
		self.label.setText(currentDateTime.toString("yyyy-MM-dd  HH:mm:ss  dddd"))

	def showRemainingTime(self):
		self.label2.setText(str(self.timer1.remainingTime())+"ms")

	def startTimer(self):
		currentDateTime = QDateTime.currentDateTime()
		self.label.setText(currentDateTime.toString("yyyy-MM-dd  HH:mm:ss  dddd"))
		# 2. 开始定时
		self.timer1.start(1000)  # 设置定时的时间，单位为1ms
		self.timer2.start(1)
		print("1. timer1定时器ID为：", self.timer1.timerId())  # 如果定时器正在运行则返回定时器的ID，如果没有运行则返回-1
		print("2. timer2定时器ID为：", self.timer2.timerId())
		print("3. time1.isActive() = ", self.timer1.isActive())
		self.startButton.setEnabled(False)
		self.stopButton.setEnabled(True)

	def stopTimer(self):
		# 3.停止定时
		self.timer1.stop()  # 停止定时器
		self.timer2.stop()
		self.startButton.setEnabled(True)
		self.stopButton.setEnabled(False)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ShowTime()
	window.show()
	sys.exit(app.exec_())
