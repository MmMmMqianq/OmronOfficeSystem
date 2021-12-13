"""
QPropertyAnimation(obj, property)，通过对象的属性来设置动画效果，对象的所有属性可以在Qt Designer里直观的看到
支持的QVariant：Int,UInt,Double,Float,QLine,QLineF,QPoint,QPointF,QSize,QSizeF,QRect,QRectF,QColor

QParallelAnimationGroup：设置并行动画组
QSequentialAnimationGroup：设置串行动画组
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QFont, QFontInfo
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSequentialAnimationGroup, QRect, QSize, QPoint, Qt, QEasingCurve


class Animation(QWidget):

	def __init__(self):
		super(Animation, self).__init__()

		self.setWindowTitle("动画")
		self.resize(400, 400)
		self.startButton1 = QPushButton("开始单个动画")
		self.stopButton2 = QPushButton("停止单个动画")

		self.startButton3 = QPushButton("开始并行动画")
		self.stopButton4 = QPushButton("停止并行动画")

		self.startButton5 = QPushButton("开始串行动画")
		self.stopButton6 = QPushButton("停止串行动画")

		self.gLayout = QGridLayout(self)
		self.gLayout.addWidget(self.startButton1, 0, 0, 1, 1)
		self.gLayout.addWidget(self.stopButton2, 0, 1, 1, 1)
		self.gLayout.addWidget(self.startButton3, 1, 0, 1, 1)
		self.gLayout.addWidget(self.stopButton4, 1, 1, 1, 1)
		self.gLayout.addWidget(self.startButton5, 2, 0, 1, 1)
		self.gLayout.addWidget(self.stopButton6, 2, 1, 1, 1)

		self.startButton1.clicked.connect(self.startSingleAnimation)
		self.stopButton2.clicked.connect(self.stopSingleAnimation)

		self.startButton3.clicked.connect(self.startParallelAnimation)
		self.stopButton4.clicked.connect(self.stopParallelAnimation)

		self.startButton5.clicked.connect(self.startSequentialAnimation)
		self.stopButton6.clicked.connect(self.stopSequentialAnimation)

		# 创建QPropertyAnimation类属性动画1
		self.animation = QPropertyAnimation(self, b"geometry")
		self.animation.setDuration(5000)  # 设置变化时间
		self.animation.setStartValue(QRect(300, 300, 150, 50))  # 设置开始值
		self.animation.setKeyValueAt(0.5, QRect(300, 300, 100, 200))  # setKeyValueAt(float, value),设置中间点，
		# float乘以setDuration(ms)设置的时间为该段变化的时间
		self.animation.setKeyValueAt(1, QRect(300, 300, 150, 200))
		self.animation.setEndValue(QRect(300, 300, 150, 400))  # 设置结束值
		self.animation.setEasingCurve(QEasingCurve.OutInQuart)  # 设置值变化的曲线
		self.animation.setLoopCount(-1)  # 动画循环次数，-1表示无限循环

		# 创建QPropertyAnimation类属性动画2
		self.animation1 = QPropertyAnimation(self.startButton1, b"geometry")
		self.animation1.setDuration(2000)
		self.animation1.setStartValue(QRect(0, 0, 50, 50))
		self.animation1.setKeyValueAt(0.5, QRect(100, 150, 50, 50))
		self.animation1.setKeyValueAt(1, QRect(300, 300, 150, 200))
		self.animation1.setEndValue(QRect(300, 300, 150, 400))
		self.animation1.setEasingCurve(QEasingCurve.OutInQuart)
		self.animation1.setLoopCount(-1)

	def startSingleAnimation(self):
		"""
		开始 QPropertyAnimation 动画
		"""
		self.animation.start()  # 开始动画

	def stopSingleAnimation(self):
		"""
		停止 QPropertyAnimation 动画
		"""
		self.animation.stop()  # 开始动画

	def startParallelAnimation(self):
		"""
		用QPropertyAnimation创建并行动画组，并将动画添加到组，开始并行组动画
		"""
		self.parallelGroup = QParallelAnimationGroup()
		self.animation.setLoopCount(1)  # 把动画循环设置为1次，如果无限循环的话第二个动画没法执行
		self.animation1.setLoopCount(1)
		self.parallelGroup.addAnimation(self.animation)  # 将动画对象添加到组
		self.parallelGroup.addAnimation(self.animation1)
		self.parallelGroup.setLoopCount(-1)  # 设置组循环
		self.parallelGroup.start()  # 开始并行组动画

	def stopParallelAnimation(self):
		"""
		停止并行组动画
		"""
		self.parallelGroup.stop()  # 停止并行组动画

	def startSequentialAnimation(self):
		"""
		用QSequentialAnimation创建串行动画组，并将动画添加到组，开始串行组动画
		"""
		self.sequentialGroup = QSequentialAnimationGroup()
		self.animation.setLoopCount(1)  # 把动画循环设置为1次，如果无限循环的话第二个动画没法执行
		self.animation1.setLoopCount(1)
		self.sequentialGroup.addAnimation(self.animation)  # 将动画对象添加到组
		self.sequentialGroup.addAnimation(self.animation1)
		self.sequentialGroup.setLoopCount(-1)
		self.sequentialGroup.addPause(2000)  # 当设置循环次数时，用来设置组之间的间隔
		self.sequentialGroup.insertPause(1, 2000)  # 在索引动画前加入延时，设置动画之间的间隔
		self.sequentialGroup.start()  # 开始串行组动画

	def stopSequentialAnimation(self):
		"""
		停止并行组动画
		"""
		self.sequentialGroup.stop()  # 停止串行组动画


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Animation()
	window.show()
	sys.exit(app.exec_())
