import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QMetaObject, pyqtBoundSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class SignalAndSlot(QWidget):
	def __init__(self):
		super(SignalAndSlot, self).__init__()
		self.setWindowTitle("WorkTread and defSignal demo")
		self.resize(500, 500)

		self.send = Signal()
		self.slot = Slot()

		self.meta_object1 = self.send.signal1.connect(self.slot.slot1)
		print("5, self.send.signal1.connect(self.defSignal.slot1) = ", self.meta_object1)
		self.send.connect_and_emit_signal1()
		self.send.signal1.disconnect(self.slot.slot1)

		self.meta_object2 = self.send.signal2.connect(self.slot.slot2)
		print("6, self.send.signal2.connect(self.defSignal.slot2) = ", self.meta_object2)
		self.send.connect_and_emit_signal2()

		self.meta_object3_1 = self.send.signal3[int, str].connect(self.slot.slot3_1)
		print("7, self.send.signal3[int, str].connect(self.defSignal.slot3_1) = ", self.meta_object3_1)
		self.send.connect_and_emit_signal3_1()

		self.meta_object3_2 = self.send.signal3[str, int].connect(self.slot.slot3_2)
		print("8, self.send.signal3[str, int].connect(self.defSignal.slot3_2) = ", self.meta_object3_2)
		self.send.connect_and_emit_signal3_2()


class Signal(QObject):
	# 1. 定义信号
	signal1: pyqtBoundSignal  # 声明变量的类型，方便写程序时可以自动补全
	signal1 = pyqtSignal()                        # 信号名字为signal1，不带任何参数
	signal2 = pyqtSignal(int, str, name="aa")     # 信号名字为aa，带int和str两个参数
	signal3 = pyqtSignal([int, str], [str, int])  # 信号名字为signal3，带两个重载参数，两个中括号是或的关系

	def __init__(self):
		super(Signal, self).__init__()

	# 2. 定义发射信号的方法
	def connect_and_emit_signal1(self):
		self.signal1.emit()

	def connect_and_emit_signal2(self):
		self.signal2.emit(10, "十")

	def connect_and_emit_signal3_1(self):
		self.signal3[int, str].emit(10, "十")

	def connect_and_emit_signal3_2(self):
		self.signal3[str, int].emit("十一", 11)


class Slot(QObject):
	# 3. 创建槽函数
	@pyqtSlot()  # 声明下面的函数是槽函数
	def slot1(self):
		print("1. 执行slot1函数")

	@pyqtSlot(int, str)
	def slot2(self, int1, str2):
		print("2. signal2返回的两个整型数据为：%d, %s " % (int1, str2))

	@pyqtSlot(int, str)
	def slot3_1(self, int1, str1):
		print("3. signal3返回的两个数据为：%d, %s" % (int1, str1))

	@pyqtSlot(str, int)
	def slot3_2(self, str1, int1):
		print("4. signal3返回的两个整型数据为：%s, %d" % (str1, int1))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = SignalAndSlot()
	window.show()
	sys.exit(app.exec_())