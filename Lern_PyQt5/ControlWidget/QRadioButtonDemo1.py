import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox


class QRadioButtonDemo(QWidget):
	def __init__(self):
		super(QRadioButtonDemo, self).__init__()
		self.setWindowTitle("这是一个QRadioButton案例")
		self.resize(300, 300)

		self.label_male = QLabel("男")
		self.radio_button_male = QRadioButton()

		self.label_female = QLabel("女")
		self.radio_button_female = QRadioButton()

		self.label_male1 = QLabel("男1")
		self.radio_button_male1 = QRadioButton()

		self.label_female1 = QLabel("女1")
		self.radio_button_female1 = QRadioButton()

		self.group_box_1 = QGroupBox(self)
		self.h_layout = QHBoxLayout(self.group_box_1)
		self.h_layout.addWidget(self.label_male)
		self.h_layout.addWidget(self.radio_button_male)

		self.label_male.setParent(self.group_box_1)
		self.radio_button_male.setParent(self.group_box_1)
		self.h_layout.setParent(self.group_box_1)

		self.g_layout = QGridLayout(self)
		self.g_layout.addWidget(self.label_male, 0, 0, 1, 1)
		self.g_layout.addWidget(self.radio_button_male, 0, 1, 1, 1)
		self.g_layout.addWidget(self.label_female, 0, 2, 1, 1)
		self.g_layout.addWidget(self.radio_button_female, 0, 3, 1, 1)

		self.g_layout.addWidget(self.label_male1, 1, 0, 1, 1)
		self.g_layout.addWidget(self.radio_button_male1, 1, 1, 1, 1)
		self.g_layout.addWidget(self.label_female1, 1, 2, 1, 1)
		self.g_layout.addWidget(self.radio_button_female1, 1, 3, 1, 1)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QRadioButtonDemo()
	widget.show()
	sys.exit(app.exec_())
