"""
QLabel 与伙伴关系:
QLabel对象.setText("显示文本（热键）")
QLabel对象.setBuddy(控件对象)
例：
self.name_label = QLabel(self.widget)
self.name_label.setText("name(&q)")  # Alt+q
self.name_line_edit = QLineEdit(self.widget)
self.name_label.setBuddy(self.name_line_edit

QGridLayout:
g_layout.addWidget(self.button_cancel, 3, 2, 1, 1)
g_layout.addWidget(控件对象, 开始行号, 开始列号, 所占行数, 所占列数)
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import QRect


class QLabelBuddy(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(QRect(400, 400, 400, 500))
		self.setWindowTitle("这是一个QLable伙伴关系")

		self.central_widget = QWidget(self)
		self.widget = QWidget(self.central_widget)

		self.name_label = QLabel(self.widget)
		self.name_label.setText("name(&q)")  # 设置热键Alt+q，如果写"&name",那么热键就是Alt+n
		self.name_line_edit = QLineEdit(self.widget)
		self.name_label.setBuddy(self.name_line_edit)

		self.password_label = QLabel(self.widget)
		self.password_label.setText("password(&w)")  # 设置热键Alt+w
		self.password_line_dit = QLineEdit(self.widget)
		self.password_label.setBuddy(self.password_line_dit)

		self.button_ok = QPushButton(self.widget)
		self.button_ok.setText("Confirm")

		self.button_cancel = QPushButton(self.widget)
		self.button_cancel.setText("Cancel")

		self.g_layout = QGridLayout(self.widget)
		self.g_layout.addWidget(self.name_label, 0, 0, 1, 1)
		self.g_layout.addWidget(self.name_line_edit, 0, 1, 1, 2)
		self.g_layout.addWidget(self.password_label, 1, 0, 1, 1)
		self.g_layout.addWidget(self.password_line_dit, 1, 1, 1, 2)
		self.g_layout.addWidget(self.button_ok, 3, 1, 1, 1)
		self.g_layout.addWidget(self.button_cancel, 3, 2, 1, 1)

		self.setCentralWidget(self.central_widget)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_window = QLabelBuddy()
	main_window.show()
	sys.exit(app.exec_())
