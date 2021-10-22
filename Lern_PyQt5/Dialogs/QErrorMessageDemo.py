from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QErrorMessage
import sys


class QErrorMessageDemo(QMainWindow):
	def __init__(self):
		super(QErrorMessageDemo, self).__init__()
		self.setWindowTitle("这是一个QErrorMessage实例")
		self.resize(300, 150)

		self.showErrorButton = QPushButton(self)
		self.showErrorButton.setText("错误1")
		self.showErrorButton.resize(180, 25)
		self.showErrorButton.move(70, 10)

		self.errorButton = QPushButton(self)
		self.errorButton.setText("错误2")
		self.errorButton.resize(180, 25)
		self.errorButton.move(70, 40)

		self.errorMessageDialog = QErrorMessage()
		self.errorMessageDialog.setWindowTitle("错误提示框标题")
		self.errorMessageDialog.showMessage("1. 错误提示信息1")

		self.showErrorButton.clicked.connect(lambda: self.errorMessageDialog.showMessage("错误1"))
		self.errorButton.clicked.connect(lambda: self.errorMessageDialog.showMessage("错误2"))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QErrorMessageDemo()
	mainWindow.show()
	sys.exit(app.exec_())
