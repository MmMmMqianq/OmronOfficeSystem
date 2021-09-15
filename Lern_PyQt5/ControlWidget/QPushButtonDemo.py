import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class QPushButtonDemo(QWidget):
	def __init__(self):
		super(QPushButtonDemo, self).__init__()
		self.setWindowTitle("这是一个QPushButton案例")

		self.push_button = QPushButton(self)
		self.push_button.setText("按钮1")

		self.v_layout = QVBoxLayout(self)
		self.v_layout.addWidget(self.push_button)

		self.push_button.setIcon(QIcon("./images/1.ico"))
		self.push_button.setIconSize(QSize(20, 20))
		print(self.push_button.iconSize())

		self.push_button.setCheckable(False)  # 如果设置为True按钮按下去不会弹起来的，处于被选中的状态
		print(self.push_button.isCheckable())
		self.push_button.setChecked(True)  # 将按钮设置为选中状态，只有当isCheckable() = True时改方法才有效
		print(self.push_button.isChecked())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QPushButtonDemo()
	widget.show()
	sys.exit(app.exec_())
