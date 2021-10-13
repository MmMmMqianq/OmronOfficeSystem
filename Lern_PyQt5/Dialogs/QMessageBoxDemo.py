from PyQt5.QtWidgets import QMessageBox, QPushButton, QMainWindow, QApplication, QCheckBox
import sys


class QMessageBoxDemo(QMainWindow):
	def __init__(self):
		super(QMessageBoxDemo, self).__init__()
		self.setWindowTitle("这是一个QMessageBox实例")
		self.resize(500, 200)

		self.button = QPushButton(self)
		self.button.resize(200, 50)
		self.button.move(100, 100)
		self.button.setText("显示QMessageBox对话框")

		self.button.clicked.connect(self.showQMessageBox)

	def showQMessageBox(self):
		messageBox = QMessageBox()
		messageBox.setText("The document has been modified.")
		messageBox.setInformativeText("Do you want to save your changes?")
		messageBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
		messageBox.setDetailedText("1.\n2.\n3.")

		addButton = QPushButton("添加的按钮，角色为YesRole")
		messageBox.addButton(addButton, QMessageBox.YesRole)
		print("3. ", messageBox.buttonRole(addButton))

		addCheckBoxYes = QCheckBox("是")
		messageBox.setCheckBox(addCheckBoxYes)
		messageBox.buttonClicked.connect(lambda: print(addCheckBoxYes.checkState()))

		self.ret = messageBox.exec_()
		print("1. ", self.ret, type(self.ret))
		print("2. ", messageBox.result())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QMessageBoxDemo()
	mainWindow.show()
	sys.exit(app.exec_())
