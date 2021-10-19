import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette


class QColorDialogDemo(QMainWindow):
	def __init__(self):
		super(QColorDialogDemo, self).__init__()

		self.setWindowTitle("这是一个QColorDialog实例")
		self.resize(300, 150)

		self.lineEdit = QLineEdit(self)
		self.lineEdit.resize(180, 25)
		self.lineEdit.move(30, 50)
		self.lineEdit.setPlaceholderText("请输入：")

		self.textButton = QPushButton(self)
		self.textButton.setText("设置 text 颜色")
		self.textButton.resize(110, 25)
		self.textButton.move(20, 80)

		self.textButton.clicked.connect(self.showColorDialog)

	def showColorDialog(self):
		colorDialog = QColorDialog()
		if colorDialog.exec_():
			color = colorDialog.selectedColor()
			palette = QPalette()
			palette.setColor(QPalette.Text, color)
			self.lineEdit.setPalette(palette)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QColorDialogDemo()
	mainWindow.show()
	sys.exit(app.exec_())
