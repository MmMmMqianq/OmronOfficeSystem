from PyQt5.QtWidgets import QFileDialog, QPushButton, QApplication, QMainWindow
import sys


class QFileDialogDemo(QMainWindow):
	def __init__(self):
		super(QFileDialogDemo, self).__init__()
		self.setWindowTitle("这是一个QFileDialog实例")
		self.resize(300, 100)

		self.button = QPushButton(self)
		self.button.setText("弹出QFileDialog")
		self.button.resize(150, 25)
		self.button.move(70, 30)
		self.button.clicked.connect(self.showQFileDialog)

	def showQFileDialog(self):
		fileDialog = QFileDialog()
		fileDialog.getOpenFileName(self, "open image", "/Users/qianshaoqing/Documents/Python/Lern_PyQt5/Dialogs",
		                           "Image Files (*.png *.jpg *.bmp)")
		fileDialog.exec_()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QFileDialogDemo()
	mainWindow.show()
	sys.exit(app.exec_())

