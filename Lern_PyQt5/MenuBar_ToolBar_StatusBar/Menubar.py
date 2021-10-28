import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QMenuBar


class MenuBarDemo(QMainWindow):
	def __init__(self):
		super(MenuBarDemo, self).__init__()

		self.setWindowTitle("这是一个MenuBar实例")
		self.resize(500, 300)

		menuBar = QMenuBar(self)
		fileMenu = QMenu("文件")
		menuBar.addMenu(fileMenu)
		self.setMenuBar(menuBar)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = MenuBarDemo()
	mainWindow.show()
	sys.exit(app.exec_())
