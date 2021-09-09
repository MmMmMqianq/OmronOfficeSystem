"""
QLineEdit控件与回显模式：

基本功能：输入单行文本

EchoMode(回显模式):
1.Normal
2.NoEcho
3.Password
4.PasswordEchoOnEdit
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt


class QLineEditEchoMode(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("这是一个QLineEdit EchoMode案例")

		self.line_edit_1 = QLineEdit(self)
		self.line_edit_1.setPlaceholderText("Normal")
		self.line_edit_1.setEchoMode(QLineEdit.Normal)

		self.line_edit_2 = QLineEdit(self)
		self.line_edit_2.setPlaceholderText("NoEcho")
		self.line_edit_2.setEchoMode(QLineEdit.NoEcho)

		self.line_edit_3 = QLineEdit(self)
		self.line_edit_3.setPlaceholderText("Password")
		self.line_edit_3.setEchoMode(QLineEdit.Password)

		self.line_edit_4 = QLineEdit(self)
		self.line_edit_4.setPlaceholderText("PasswordEchoOnEdit")
		self.line_edit_4.setEchoMode(QLineEdit.PasswordEchoOnEdit)

		self.form = QFormLayout(self)
		self.form.setFormAlignment(Qt.AlignCenter)
		self.form.addRow("Normal:", self.line_edit_1)
		self.form.addRow("NoEcho:", self.line_edit_2)
		self.form.addRow("Password:", self.line_edit_3)
		self.form.addRow("PasswordEcho:", self.line_edit_4)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QLineEditEchoMode()
	widget.show()
	sys.exit(app.exec_())
