"""
QLable 与伙伴关系
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QWidget, QGridLayout
from PyQt5.QtCore import QRect


class QlableBuddy(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(QRect(400, 400, 400, 500))
		self.setWindowTitle("这是一个QLable伙伴关系")

		self.central_widget = QWidget(self)
		self.widget = QWidget(self.central_widget)

		self.name_lable = QLabel("&name", self.widget)
		# self.name_lable.setText("name")
		self.name_line_edit = QLineEdit(self.widget)
		self.name_lable.setBuddy(self.name_line_edit)


		self.password_lable = QLabel("&password", self.widget)
		# self.password_lable.setText("name")
		self.password_line_dit = QLineEdit(self.widget)
		self.password_lable.setBuddy(self.password_line_dit)

		self.g_layout = QGridLayout(self.widget)
		self.g_layout.addWidget(self.name_lable, 0, 0, 1, 1)
		self.g_layout.addWidget(self.name_line_edit, 0, 1, 1, 2)
		self.g_layout.addWidget(self.password_lable, 1, 0, 1, 1)
		self.g_layout.addWidget(self.password_line_dit, 1, 1, 1, 2)

		self.setCentralWidget(self.central_widget)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_window = QlableBuddy()
	main_window.show()
	sys.exit(app.exec_())
