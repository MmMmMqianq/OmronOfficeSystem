from PyQt5.QtWidgets import QSlider, QApplication, QWidget, QLineEdit, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import sys


class QSliderDemo(QWidget):
	def __init__(self):
		super(QSliderDemo, self).__init__()
		self.setWindowTitle("这是一个QSlider实例")

		self.slider = QSlider()
		self.slider.setMaximum(200)
		self.slider.setMinimum(0)
		self.slider.setOrientation(Qt.Horizontal)
		self.slider.setTickPosition(QSlider.TicksBelow)
		self.slider.setTracking(True)
		self.slider.setSingleStep(10)
		self.slider.setPageStep(20)
		self.slider.setValue(100)
		print("1. ", self.slider.sliderPosition())

		self.line_edit = QLineEdit()
		self.line_edit.setText(str(self.slider.value()))

		self.label = QLabel()
		self.label.setText("当前值为:")

		self.int_validator = QIntValidator()
		self.int_validator.setTop(200)
		self.int_validator.setBottom(0)
		self.line_edit.setValidator(self.int_validator)

		self.g_layout = QGridLayout(self)
		self.g_layout.addWidget(self.label, 0, 0, 1, 1)
		self.g_layout.addWidget(self.line_edit, 0, 1, 1, 2)
		self.g_layout.addWidget(self.slider, 1, 0, 1, 3)

		self.slider.valueChanged.connect(self.set_line_edit_text)
		self.slider.sliderMoved.connect(self.set_line_edit_text)
		self.line_edit.editingFinished.connect(self.set_slider_value)

	def set_line_edit_text(self):
		self.line_edit.setText(str(self.slider.value()))

	def set_slider_value(self):
		self.slider.setValue(int(self.line_edit.text()))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QSliderDemo()
	widget.show()
	sys.exit(app.exec_())
