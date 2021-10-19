from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QErrorMessage
import sys


class QErrorMessageDemo(QMainWindow):
	def __init__(self):
		super(QErrorMessageDemo, self).__init__()
		self.setWindowTitle("这是一个QErrorMessage实例")
		self.resize(300, 150)

		self.button = QPushButton(self)
		self.button.setText("弹出 error 对话框")
		self.button.resize(180, 25)
		self.button.move(70, 10)

		self.errorMessageDialog = QErrorMessage()
		self.button.clicked.connect(self.showErrorMessageDialog)

	def showErrorMessageDialog(self):
		errorMessageDialog = QErrorMessage()
		errorMessageDialog.setWindowTitle("错误提示框标题")
		errorMessageDialog.showMessage("1. 错误提示信息1")
		print(errorMessageDialog.exec_())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QErrorMessageDemo()
	mainWindow.show()
	sys.exit(app.exec_())
