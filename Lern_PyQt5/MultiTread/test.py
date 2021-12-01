import sys, time
from PyQt5.QtCore import QTimer, QDateTime, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout


def doIt(do):
	global count
	do.start()
	count += 1
	print(count, ", ", do.isRunning())


class Do(QThread):
	startSignal = pyqtSignal()
	finishedSignal = pyqtSignal()

	def __init__(self):
		super(Do, self).__init__()

	def run(self):
		time.sleep(2)
		self.startSignal.emit()
		time.sleep(2)
		print("11")
		self.finishedSignal.emit()

count = 0

app = QApplication(sys.argv)

win = QWidget()

btn = QPushButton("按钮")
btn2 = QPushButton("按钮2")
btn3 = QPushButton("按钮3")
vLayout = QVBoxLayout(win)
vLayout.addWidget(btn)
vLayout.addWidget(btn2)
vLayout.addWidget(btn3)
do = Do()
do1 = Do()
do2 = Do()
btn.clicked.connect(lambda: doIt(do))
btn2.clicked.connect(lambda: doIt(do1))
btn3.clicked.connect(lambda: print(do.isRunning()))

do.startSignal.connect(lambda: print("开始"))
do.finishedSignal.connect(lambda: print("完成"))
print("qqq", do.startSignal)

win.show()
sys.exit(app.exec_())
