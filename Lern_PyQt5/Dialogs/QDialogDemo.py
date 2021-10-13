from PyQt5.QtWidgets import QDialog, QPushButton, QApplication, QMainWindow, QHBoxLayout
from PyQt5.QtCore import Qt
import sys


class QDialogDemo(QMainWindow):
	def __init__(self):
		super(QDialogDemo, self).__init__()
		self.setWindowTitle("这是一个QDialog实例")
		self.resize(300, 200)

		self.button = QPushButton(self)
		self.button.setText("弹出对话框")
		self.button.move(50, 50)

		self.button.clicked.connect(self.showDialog)

	def showDialog(self):
		dialog = QDialog()
		dialog.setWindowTitle("这是一个弹出的对话框")
		dialog.resize(200, 100)
		# dialog.setWindowModality(Qt.ApplicationModal)  # 弹出对话框后主窗口是不能进行任何操作的
		dialog.setModal(True)

		acceptButton = QPushButton()
		acceptButton.setText("Accept")
		acceptButton.clicked.connect(dialog.accept)
		dialog.accepted.connect(lambda: print("1. ", dialog.result()))

		rejectButton = QPushButton()
		rejectButton.setText("Reject")
		rejectButton.clicked.connect(dialog.reject)
		dialog.rejected.connect(lambda: print("2. ", dialog.result()))

		doneButton = QPushButton()
		doneButton.setText("Done")
		doneButton.clicked.connect(lambda: dialog.done(10))

		dialog.finished.connect(lambda: print("3. ", dialog.result()))

		hLayout = QHBoxLayout(dialog)
		hLayout.addWidget(acceptButton)
		hLayout.addWidget(rejectButton)
		hLayout.addWidget(doneButton)

		dialog.show()
		self.ret = dialog.exec_()
		print("4. ", self.ret)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QDialogDemo()
	mainWindow.show()
	sys.exit(app.exec_())
