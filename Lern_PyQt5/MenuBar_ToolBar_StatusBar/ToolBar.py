import sys
from PyQt5.QtWidgets import QApplication, QToolBar, QMainWindow, QAction, QActionGroup, QCheckBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class ToolBarDemo(QMainWindow):
	def __init__(self):
		super(ToolBarDemo, self).__init__()

		self.resize(500, 300)

		# 创建一个工具栏
		self.toolBar = QToolBar()
		self.toolBar.setWindowTitle("工具栏")
		self.toolBar.setIconSize(QSize(16, 16))  # 设置图标大小
		self.toolBar.setFloatable(True)  # 设置toolBar是可以悬浮于窗口的任意位置
		self.toolBar.setMovable(True)    # 设置toolBar是否可以移动
		self.toolBar.setToolButtonStyle(Qt.ToolButtonFollowStyle)  # 设置toolBar中按钮的显示风格，默认是鼠标放到按钮时显示按钮名字
		self.toolBar.setAllowedAreas(Qt.LeftToolBarArea)  # 设置toolBar在被拖动后允许被放置到什么地方，本实例中只能被放到窗口左侧
		# 创建action
		self.action1 = QAction()
		self.action1.setText("工具1")
		self.action1.setIcon(QIcon("./images/b1.ico"))
		# 创建actionGroup
		self.actionG = QAction()
		self.actionGroup1 = QActionGroup(self)

		self.action2 = QAction("工具2")
		self.action2.setIcon(QIcon("./images/b5.png"))

		self.action3 = QAction()
		self.action3.setText("工具3")
		self.action3.setIcon(QIcon("./images/b8.png"))

		self.action4 = QAction()
		self.action4.setText("工具4")
		self.action4.setIcon(QIcon("./images/b9.png"))

		self.checkBox1 = QCheckBox("单选框")

		# 将toolBar添加到窗口
		self.addToolBar(self.toolBar)
		# 将action添加到toolBar，并且插入分隔符
		self.toolBar.addAction(self.action1)
		# self.toolBar.addAction(self.actionG)
		self.toolBar.insertSeparator(self.action2)
		self.toolBar.addAction(self.action2)
		self.toolBar.insertSeparator(self.action3)
		self.toolBar.addAction(self.action3)
		self.toolBar.insertSeparator(self.action4)
		self.toolBar.addAction(self.action4)
		self.toolBar.insertWidget(self.action4, self.checkBox1)

		self.toolBar.actionTriggered.connect(self.triggeredActionButton)  # 触发QToolBar.triggered信号执行槽函数时，会将被触发的action作为参数再传给槽函数

		print(self.toolBar.iconSize())

	def triggeredActionButton(self, triggeredAction: QAction):
		s = self.sender()
		print("%s 中的按钮被触发了" % s.windowTitle())
		print("%s 中 %s 按钮被触发了" % (s.windowTitle(), triggeredAction.text()))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ToolBarDemo()
	window.show()
	sys.exit(app.exec_())