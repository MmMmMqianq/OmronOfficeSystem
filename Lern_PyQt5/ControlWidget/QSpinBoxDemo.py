from PyQt5.QtWidgets import QSpinBox, QPushButton, QGridLayout, QApplication, QWidget
import sys


class QSpinBoxDemo(QWidget):
	def __init__(self):
		super(QSpinBoxDemo, self).__init__()
		self.widget = QWidget()
		self.widget.setWindowTitle("这是一个QSpinBox实例")

		self.spin_box = QSpinBox()
		self.spin_box.setRange(-100, 100)
		self.spin_box.setSingleStep(1)
		self.spin_box.setPrefix("您输入的是")
		self.spin_box.setSuffix("cm")
		self.spin_box.setValue(50)

		self.clean_button = QPushButton()
		self.clean_button.setText("获取值")

		self.g_layout = QGridLayout(self)
		self.g_layout.addWidget(self.spin_box, 0, 0, 1, 2)
		self.g_layout.addWidget(self.clean_button, 1, 1, 1, 1)

		self.clean_button.clicked.connect(self.clean_spin_box)
		self.spin_box.valueChanged.connect(lambda: print("3. QSpinBox值发生了变化啦！"))

	def clean_spin_box(self):
		sender = self.widget.sender()
		print("1. ", sender.text(), " 按钮被触发了")
		print("2. ", self.spin_box.cleanText())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QSpinBoxDemo()
	widget.show()
	sys.exit(app.exec_())