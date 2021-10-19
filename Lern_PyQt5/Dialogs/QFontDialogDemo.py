import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFontDialog, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class QFontDialogDemo(QMainWindow):
	def __init__(self):
		super(QFontDialogDemo, self).__init__()

		self.setWindowTitle("这是一个QFontDialog实例")
		self.resize(300, 150)

		self.lineEdit = QLineEdit(self)
		self.lineEdit.resize(180, 25)
		self.lineEdit.move(30, 50)

		self.button = QPushButton(self)
		self.button.setText("设置字体")
		self.button.resize(80, 25)
		self.button.move(215, 50)

		self.button.clicked.connect(self.showFontDialog)

	def showFontDialog(self):
		fontDialog = QFontDialog()
		print(fontDialog.currentFont())
		fontDialog.fontSelected.connect(lambda: self.lineEdit.setFont(fontDialog.selectedFont()))
		fontDialog.exec_()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QFontDialogDemo()
	mainWindow.show()
	sys.exit(app.exec_())
