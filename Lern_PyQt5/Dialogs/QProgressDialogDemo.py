import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressDialog, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class QProgressDialogDemo(QMainWindow):
	def __init__(self):
		super(QProgressDialogDemo, self).__init__()

		self.setWindowTitle("这是一个QProgressDialog实例")
		self.resize(300, 150)

		self.button = QPushButton(self)
		self.button.setText("ProgressDialog按钮")
		self.button.resize(150, 25)
		self.button.move(80, 40)

		self.cancelButton = QPushButton(self)
		self.cancelButton.setText("取消按钮")
		self.cancelButton.resize(150, 25)
		self.cancelButton.move(80, 70)

		self.button.clicked.connect(self.showProgressDialog)

	def showProgressDialog(self):
		progressDialog = QProgressDialog()
		progressDialog.setWindowModality(Qt.WindowModal)
		progressDialog.setRange(0, 10000)
		progressDialog.setMinimumDuration(1)
		progressDialog.setWindowTitle("ProgressDialog")
		progressDialog.setLabelText("加载中...")
		progressDialog.setCancelButtonText("取消")

		for i in range(0, 10000):
			# progressDialog.setLabelText("加载中...当前文件为:%04d" % i)  # Windows系统上可以显示名字，Mac上会出现进度条不显示的情况
			for ii in range(0, 50000):
				if ii == 49999:
					progressDialog.setValue(i)
			self.cancelButton.clicked.connect(progressDialog.cancel)  # 按下自定义的取消按钮关闭进度条对话框
			if progressDialog.wasCanceled():  # 按下Cancel按钮时关闭进度条对话框
				print("1. ", progressDialog.wasCanceled())
				break
		progressDialog.setValue(10000)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QProgressDialogDemo()
	mainWindow.show()
	sys.exit(app.exec_())