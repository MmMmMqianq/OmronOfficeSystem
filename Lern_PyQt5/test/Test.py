"""
将Qt Designer生成的.ui文件转换为.py文件并调用，这样可以将Ui代码和功能代码分开
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem
import TestUi


class Test(QMainWindow):
	def __init__(self):
		super(Test, self).__init__()

		self.setWindowTitle("这是一个QTreeWidget实例")
		self.resize(300, 500)
		self.ui = TestUi.Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Test()
	window.show()
	sys.exit(app.exec_())