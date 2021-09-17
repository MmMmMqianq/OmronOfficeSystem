import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QMenu, QAction
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QSize, Qt


class QPushButtonDemo(QWidget):
	def __init__(self):
		super(QPushButtonDemo, self).__init__()
		self.setWindowTitle("这是一个QPushButton案例")
		self.resize(300, 300)

		self.push_button = QPushButton(self)
		self.push_button.setText("按钮1")

		self.push_button_2 = QPushButton(self)
		self.push_button_2.setText("按钮2")

		self.v_layout = QVBoxLayout(self)
		self.v_layout.addWidget(self.push_button)
		self.v_layout.addWidget(self.push_button_2)

		self.push_button.setIcon(QIcon("./images/1.ico"))
		self.push_button.setIconSize(QSize(20, 20))
		print("1.", self.push_button.iconSize())

		self.push_button.setCheckable(False)  # 如果设置为True按钮按下去不会弹起来的，处于被选中的状态
		print("2.", self.push_button.isCheckable())
		self.push_button.setChecked(True)  # 将按钮设置为选中状态，只有当isCheckable() = True时改方法才有效
		print("3.", self.push_button.isChecked())

		self.push_button.setShortcut(QKeySequence(Qt.CTRL+Qt.Key_W))  # mac中ctrl时command键
		print("4.", self.push_button.shortcut().toString())  # QKeySequence.toString()将快捷键转换为字符串

		self.push_button.clicked.connect(self.clicked_button)  # 按下去松开为clicked
		self.push_button.pressed.connect(self.pressed_button)  # 按下去为pressed
		self.push_button.released.connect(self.released_button)  # 松开按钮为released
		self.push_button.clicked.connect(self.push_button_2.showMenu)  # 按下按钮1弹出按钮2上的菜单

		# 创建动作对象
		self.action1 = QAction(self)
		self.action1.setText("动作1")
		self.action1.triggered.connect(self.action1_triggered)
		# 创建菜单对象
		self.menu = QMenu()
		self.menu.addMenu("菜单1")
		self.menu.addMenu("菜单2").addAction(self.action1)
		# 将动作添加到菜单上
		self.menu.addAction(self.action1)
		# 将菜单设置到button上
		self.push_button_2.setMenu(self.menu)

	def clicked_button(self):
		print("按钮clicked")

	def pressed_button(self):
		print("按钮pressed")

	def released_button(self):
		print("按钮released")

	def action1_triggered(self):
		print("这是action1 triggered")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QPushButtonDemo()
	widget.show()
	sys.exit(app.exec_())
