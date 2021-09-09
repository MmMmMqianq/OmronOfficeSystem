import sys
from PyQt5.QtWidgets import QWidget, QLineEdit ,QApplication, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator


class QLineEditValidator(QWidget):
	def __init__(self):
		super(QLineEditValidator, self).__init__()

		self.line_edit_int = QLineEdit(self)
		self.line_edit_Double = QLineEdit(self)
		self.line_edit_reg = QLineEdit(self)

		self.form = QFormLayout(self)
		self.form.addRow("QIntValidator", self.line_edit_int)
		self.form.addRow("QDoubleValidator", self.line_edit_Double)
		self.form.addRow("QRegValidator", self.line_edit_reg)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QLineEditValidator()
	widget.show()
	sys.exit(app.exec_())