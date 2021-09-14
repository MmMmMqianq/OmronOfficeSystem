import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication, QVBoxLayout


class QLineEditDemo(QWidget):
	def __init__(self):
		super(QLineEditDemo, self).__init__()
		self.setWindowTitle("这是一个QLineEditDemo")

		self.line_edit_1 = QLineEdit(self)
		self.line_edit_1.setPlaceholderText("input:")
		print("1. " + self.line_edit_1.placeholderText())

		self.v_layout = QVBoxLayout(self)
		self.v_layout.addWidget(self.line_edit_1)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QLineEditDemo()
	widget.show()
	sys.exit(app.exec_())
