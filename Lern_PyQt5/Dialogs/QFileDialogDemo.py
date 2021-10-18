from PyQt5.QtWidgets import QFileDialog, QPushButton, QApplication, QMainWindow
import sys


class QFileDialogDemo(QMainWindow):
	def __init__(self):
		super(QFileDialogDemo, self).__init__()
		self.setWindowTitle("这是一个QFileDialog实例")
		self.resize(300, 110)

		self.buttonSave = QPushButton(self)
		self.buttonSave.setText("弹出SaveFileDialog")
		self.buttonSave.resize(150, 25)
		self.buttonSave.move(70, 10)
		self.buttonSave.clicked.connect(self.showSaveFileDialog)

		self.buttonOpenFiles = QPushButton(self)
		self.buttonOpenFiles.setText("弹出OpenFileDialog")
		self.buttonOpenFiles.resize(150, 25)
		self.buttonOpenFiles.move(70, 40)
		self.buttonOpenFiles.clicked.connect(self.showOpenFileDialog)

		self.buttonOpenDir = QPushButton(self)
		self.buttonOpenDir.setText("弹出OpenDirDialog")
		self.buttonOpenDir.resize(150, 25)
		self.buttonOpenDir.move(70, 70)
		self.buttonOpenDir.clicked.connect(self.showOpenDirectoriesDialog)

	def showSaveFileDialog(self):
		SaveFileDialog = QFileDialog(None, "SaveFileDialog对话框的标题", "/Users/qianshaoqing/Documents/Python/Lern_PyQt5/Dialogs")
		SaveFileDialog.setAcceptMode(QFileDialog.AcceptSave)  # 设置为保存文件模式
		SaveFileDialog.setDefaultSuffix(".txt")  # 设置保存文件名后缀

		if SaveFileDialog.exec_():  # 点击QFileDialog中cancel时返回0，点击QFileDialog中open时返回1
			print("1, 获取被保存文件所在目录路径：", SaveFileDialog.directory().path())  # 获取选中文件的目录路径
			fileName = SaveFileDialog.selectedFiles()
			print("2, 获取被保存文件路径：", fileName)
	
	def showOpenFileDialog(self):
		OpenFileDialog = QFileDialog(None, "OpenFileDialog对话框的标题", "/Users/qianshaoqing/Documents/Python/Lern_PyQt5/Dialogs",
		                             "image files(*.png *.jpg *.ico)")
		OpenFileDialog.setAcceptMode(QFileDialog.AcceptOpen)  # 设置为打开文件模式
		OpenFileDialog.setOption(True)  # 设置为只能选择文件
		OpenFileDialog.setFileMode(QFileDialog.ExistingFiles)  # 可选中多个文件
		OpenFileDialog.setLabelText(QFileDialog.LookIn, "adasda")

		if OpenFileDialog.exec_():  # 点击QFileDialog中cancel时返回0，点击QFileDialog中open时返回1
			print("1, 获取文件所在目录路径：", OpenFileDialog.directory().path())  # 获取选中文件的目录路径
			fileNames = OpenFileDialog.selectedFiles()
			print("2, 获取文件路径：", fileNames)

	def showOpenDirectoriesDialog(self):
		OpenDirDialog = QFileDialog(None, "penDirectoriesDialog对话框标题", "/Users/qianshaoqing/Documents/Python/Lern_PyQt5/Dialogs")
		OpenDirDialog.setAcceptMode(QFileDialog.AcceptOpen)  # 设置为打开文件模式
		OpenDirDialog.setOption(True, QFileDialog.ShowDirsOnly)  # 设置为只能选择目录

		if OpenDirDialog.exec_():  # 点击QFileDialog中cancel时返回0，点击QFileDialog中open时返回1
			print("1, 获取目录路径：", OpenDirDialog.directory().path())  # 获取选中文件的目录路径
			fileNames = OpenDirDialog.selectedFiles()
			print("2, 获取目录路径：", fileNames)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QFileDialogDemo()
	mainWindow.show()
	sys.exit(app.exec_())
