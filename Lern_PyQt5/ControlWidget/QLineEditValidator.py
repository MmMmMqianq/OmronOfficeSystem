"""
QIntValidator:
例：
validator = QIntValidator(100, 999, self) #  如果不设置范围，那么默认的上下限为：-2147483648到2147483647
edit = QLineEdit(self)
edit.setValidator(validator)

Functions：
def bottom ()
def top ()
def setBottom (int)
def setTop (int)
def setRange (bottom, top)

Signals:
def bottomChanged (bottom)
def topChanged (top)

"""
import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QFormLayout, QPushButton
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator


class QLineEditValidator(QWidget):
	def __init__(self):
		super(QLineEditValidator, self).__init__()
		self.setWindowTitle("这是一个QLineEditValidator例子")

		self.line_edit_int = QLineEdit(self)
		self.line_edit_Double = QLineEdit(self)
		self.line_edit_reg = QLineEdit(self)

		self.form = QFormLayout(self)
		self.form.addRow("QIntValidator", self.line_edit_int)
		self.form.addRow("QDoubleValidator", self.line_edit_Double)
		self.form.addRow("QRegValidator", self.line_edit_reg)

		# IntValidator的使用
		self.int_validator = QIntValidator(self)  # 如果不设置范围，那么默认的上下限为：-2147483648到2147483647
		# 通过setBottom(int)和setTop(int)设置上限值
		self.int_validator.setBottom(100)
		self.int_validator.setTop(999)
		print(self.int_validator.bottom())
		print(self.int_validator.top())

		# 将整型数据验证器用于QLineEdit
		self.line_edit_int.setValidator(self.int_validator)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QLineEditValidator()
	widget.show()
	sys.exit(app.exec_())
