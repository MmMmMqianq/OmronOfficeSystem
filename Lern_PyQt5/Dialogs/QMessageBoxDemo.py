from PyQt5.QtWidgets import QMessageBox, QPushButton, QMainWindow, QApplication, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
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
		print("5. messageBox的提示信息内容为：", messageBox.text())
		messageBox.setInformativeText("Do you want to save your changes?")
		messageBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
		messageBox.setDetailedText("1.\n2.\n3.")

		messageBox.setIcon(QMessageBox.Question)  # 设置QMessageBox自带的图标
		print("6, messageBox设置的图标为：", messageBox.icon())

		# messageBox.setIconPixmap(QPixmap(r"./images/1.ico"))  # 为QMessageBox自定义的像素图
		# print("7, messageBox设置的图标为：", messageBox.iconPixmap())

		addButtonYesRole = QPushButton("添加的按钮，角色为YesRole")
		messageBox.addButton(addButtonYesRole, QMessageBox.YesRole)
		print("3. addButtonYesRole按钮的角色为：", messageBox.buttonRole(addButtonYesRole))

		addButtonEscape = QPushButton("ECC键按下时按钮被触发")
		messageBox.addButton(addButtonEscape, QMessageBox.NoRole)
		messageBox.setEscapeButton(addButtonEscape)  # 按下ESC键时addButtonEscape按钮也会被激活

		addCheckBoxYes = QCheckBox("是")
		messageBox.setCheckBox(addCheckBoxYes)
		print(messageBox.checkBox())
		messageBox.buttonClicked.connect(lambda: print("4. Yes复选框状态为：",  addCheckBoxYes.checkState()))

		self.ret = messageBox.exec_()  # 返回按下了那个按钮
		print("1. messageBox返回值和类型为：", self.ret, type(self.ret))
		print("2. messageBox.result()返回的结果为：", messageBox.result())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QMessageBoxDemo()
	mainWindow.show()
	sys.exit(app.exec_())
