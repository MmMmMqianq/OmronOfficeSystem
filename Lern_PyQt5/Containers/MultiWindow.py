"""
容纳多文档窗口，在QMdiArea中放置QMdiSubWindow
QMdiArea
QMdiSubWindow
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QMdiSubWindow, QMdiArea, QPushButton, \
	QHBoxLayout, QVBoxLayout, QWidget, QTabWidget
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt


class MultiWindow(QMainWindow):
	count = 0

	def __init__(self):
		super(MultiWindow, self).__init__()

		self.setWindowTitle("容纳多文档窗口实例")
		self.resize(500, 500)
		self.centralwidget = QWidget()
		self.setCentralWidget(self.centralwidget)

		self.menuBar = QMenuBar()
		self.menu = QMenu("File")
		self.menuBar.addMenu(self.menu)
		self.new = QAction("New")
		self.cascade = QAction("联级模式排列子窗口")
		self.title = QAction("标题平铺模式排列子窗口")
		self.menu.addActions([self.new, self.cascade, self.title])
		self.setMenuBar(self.menuBar)

		self.button1 = QPushButton("联级模式排列子窗口")
		self.button2 = QPushButton("标题平铺模式排列子窗口")
		self.button3 = QPushButton("添加窗口")
		self.button4 = QPushButton("切换到TabbedView")
		self.button4.setCheckable(True)
		self.vLayout1 = QVBoxLayout()
		self.vLayout1.addWidget(self.button4)
		self.vLayout1.addWidget(self.button3)
		self.vLayout1.addWidget(self.button1)
		self.vLayout1.addWidget(self.button2)

		# 创建mdiArea，并将其放入布局中
		self.mdiArea = QMdiArea()
		self.mdiArea.setBackground(QBrush(Qt.cyan))  # 设置QMdiArea的背景颜色
		# self.setCentralWidget(self.mdiArea)
		self.hLayout = QHBoxLayout(self.centralwidget)
		self.hLayout.addLayout(self.vLayout1)
		self.hLayout.addWidget(self.mdiArea)

		self.mdiArea.subWindowActivated.connect(self.subWinActivated)  # 当前关闭主程序窗口时会返回被激活的窗口为None

		self.menu.triggered.connect(self.useMenuBarShowSubWindow)

		self.button1.clicked.connect(self.useButtonShowSubWindow)
		self.button2.clicked.connect(self.useButtonShowSubWindow)
		self.button3.clicked.connect(self.useButtonShowSubWindow)
		self.button4.toggled.connect(self.changeViewMode)

	def useMenuBarShowSubWindow(self, action: QAction):
		if action.text() == "New":
			MultiWindow.count += 1
			# 创建子窗口，并将子窗口放到QMdiArea
			self.subWindow = QMdiSubWindow(self.mdiArea)
			# self.mdiArea.addSubWindow(self.subWindow)  # 这两中方式都可以将QMdiSubWindow添加到QMdiArea
			# self.subWindow.setParent(self.mdiArea)
			self.subWindow.setWidget(QPushButton("按钮"+str(MultiWindow.count)))
			self.subWindow.setWindowTitle("title"+str(MultiWindow.count))
			self.subWindow.show()
		elif action.text() == "联级模式排列子窗口":
			self.mdiArea.cascadeSubWindows()
		elif action.text() == "标题平铺模式排列子窗口":
			self.mdiArea.tileSubWindows()

	def useButtonShowSubWindow(self):
		print(self.sender().text())
		if self.sender().text() == "添加窗口":
			MultiWindow.count += 1
			self.subWindow = QMdiSubWindow(self.mdiArea)
			# self.mdiArea.addSubWindow(self.subWindow)  # 这两中方式都可以将QMdiSubWindow添加到QMdiArea
			# self.subWindow.setParent(self.mdiArea)
			self.subWindow.setWidget(QPushButton("按钮"+str(MultiWindow.count)))
			self.subWindow.setWindowTitle("title" + str(MultiWindow.count))
			self.subWindow.show()
		elif self.sender().text() == "联级模式排列子窗口":
			self.mdiArea.cascadeSubWindows()
		elif self.sender().text() == "标题平铺模式排列子窗口":
			self.mdiArea.tileSubWindows()

	def changeViewMode(self):
		if self.button4.isChecked():
			self.mdiArea.setViewMode(QMdiArea.TabbedView)
			self.button4.setText("切换到SubWindowView")
			# self.mdiArea.setDocumentMode(True)  # 在选项卡形式下显示，可设置为文当模式
			self.mdiArea.setTabsMovable(True)  # 选项卡形式下显示，设置选显卡是否可以移动
			self.mdiArea.setTabPosition(QTabWidget.North)
			self.mdiArea.setTabShape(QTabWidget.Triangular)
		else:
			self.mdiArea.setViewMode(QMdiArea.SubWindowView)
			self.button4.setText("切换到TabbedView")

	def windowChanged(self, oldWindow, newWindow):
		print(oldWindow, newWindow)

	def subWinActivated(self, win: QMdiSubWindow):
		if win is not None:  # 当前关闭主程序窗口时会返回被激活的窗口为None
			print(win.windowTitle(), "被激活了。。。")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MultiWindow()
	window.show()
	sys.exit(app.exec_())