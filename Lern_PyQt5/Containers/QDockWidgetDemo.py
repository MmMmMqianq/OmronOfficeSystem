"""
QDockWidget:可停靠容器
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow, QDockWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt


class DockWidgetDemo(QMainWindow):
	def __init__(self):
		super(DockWidgetDemo, self).__init__()

		self.setWindowTitle("这是一个DockWidget实例")
		self.resize(500, 500)

		# 创建dock容器
		self.dock = QDockWidget()
		self.dock.setFloating(False)  # 设置初始状态是是否为悬浮

		# 创建容器内页面
		self.widget1 = QWidget()
		self.hLayout2 = QHBoxLayout(self.widget1)
		self.button1 = QPushButton("widget1")
		self.hLayout2.addWidget(self.button1)

		self.widget2 = QWidget()
		self.widget2.resize(100, 100)
		self.hLayout3 = QHBoxLayout(self.widget2)
		self.button2 = QPushButton("widget2")
		self.hLayout3.addWidget(self.button2)

		# 将widget添加的容器中
		self.dock.setWidget(self.widget1)
		self.dock.setWidget(self.widget2)

		self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DockWidgetDemo()
    window.show()
    sys.exit(app.exec_())