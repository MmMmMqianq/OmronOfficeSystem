import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QDir


class FileSystemDemo(QMainWindow):
	def __init__(self):
		super(FileSystemDemo, self).__init__()

		self.setWindowTitle("这是一个FileSystemTreeView实例")
		self.resize(500, 500)

		self.fileSystemModel = QFileSystemModel()
		self.fileSystemModel.setRootPath(QDir.currentPath())

		self.treeView = QTreeView()
		self.treeView.setModel(self.fileSystemModel)

		self.centralwidget = QWidget()
		self.vLayout = QVBoxLayout(self.centralwidget)
		self.vLayout.addWidget(self.treeView)
		self.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = FileSystemDemo()
	window.show()
	sys.exit(app.exec_())