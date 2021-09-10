import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QFormLayout, QAction
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator


class QLineEditValidator(QWidget):
	def __init__(self):

		super(QLineEditValidator, self).__init__()
		self.line = QLineEdit(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QLineEditValidator()
	widget.show()
	sys.exit(app.exec_())
