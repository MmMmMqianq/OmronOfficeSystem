from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QPushButton, QLineEdit
import sys


class QInputDialogDemo(QMainWindow):
	def __init__(self):
		super(QInputDialogDemo, self).__init__()
		self.setWindowTitle("这是一个QInputDialog实例")
		self.resize(300, 150)

		self.intButton = QPushButton(self)
		self.intButton.setText("弹出 int 输入框")
		self.intButton.resize(180, 25)
		self.intButton.move(70, 10)
		self.intButton.clicked.connect(self.showIntInputDialog)

		self.doubleButton = QPushButton(self)
		self.doubleButton.setText("弹出 double 输入框")
		self.doubleButton.resize(180, 25)
		self.doubleButton.move(70, 40)
		self.doubleButton.clicked.connect(self.showDoubleDialog)

		self.textButton = QPushButton(self)
		self.textButton.setText("弹出 text 输入框")
		self.textButton.resize(180, 25)
		self.textButton.move(70, 70)
		self.textButton.clicked.connect(self.showTextDialog)

		self.multiLineTextButton = QPushButton(self)
		self.multiLineTextButton.setText("弹出 MultiLineText 输入框")
		self.multiLineTextButton.resize(180, 25)
		self.multiLineTextButton.move(70, 100)
		self.multiLineTextButton.clicked.connect(self.showMultiLineTextDialog)

	def showIntInputDialog(self):
		intInputDialog = QInputDialog()

		intInputDialog.setInputMode(QInputDialog.IntInput)
		intInputDialog.setWindowTitle("int型数据输入对话框")
		intInputDialog.setCancelButtonText("返回")
		intInputDialog.setOkButtonText("确定")
		intInputDialog.setLabelText("请输入0-100之间的值：")

		intInputDialog.setIntRange(0, 100)
		intInputDialog.setIntStep(5)
		intInputDialog.setIntValue(10)

		if intInputDialog.exec_():
			print("1. int输入框内容为：", intInputDialog.intValue())

	def showDoubleDialog(self):
		doubleInputDialog = QInputDialog()

		doubleInputDialog.setInputMode(QInputDialog.DoubleInput)
		doubleInputDialog.setWindowTitle("double型数据输入对话框")
		doubleInputDialog.setCancelButtonText("返回")
		doubleInputDialog.setOkButtonText("确定")
		doubleInputDialog.setLabelText("请输入0.00-200.000之间的值：")

		doubleInputDialog.setDoubleDecimals(3)  # 设置几位小数
		doubleInputDialog.setDoubleRange(0, 200.000)
		doubleInputDialog.setDoubleStep(5.016)
		doubleInputDialog.setDoubleValue(20.000)

		if doubleInputDialog.exec_():
			print("2. double输入框内容为：", doubleInputDialog.doubleValue())

	def showTextDialog(self):
		textInputDialog = QInputDialog()
		textInputDialog.setInputMode(QInputDialog.TextInput)
		textInputDialog.setTextEchoMode(QLineEdit.Normal)
		textInputDialog.setTextValue("哈哈哈hahaha")

		if textInputDialog.exec_():
			print("3. text输入框内容为：", textInputDialog.textValue())

	def showMultiLineTextDialog(self):
		multiLineTextDialog = QInputDialog()
		# result是multiLineTextDialog.getMultiLineText()返回的一个元组，result[0]是文本内容，按下Cancel按钮时result[1]=False,按下OK按钮时result[1]=True
		result = multiLineTextDialog.getMultiLineText(None, "MultiLineText输入对话框", "请输入多行文本：", "哈哈哈hahaha")
		if result[1]:
			print("4. multiLineText输入框内容为：", result[0])


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QInputDialogDemo()
	mainWindow.show()
	sys.exit(app.exec_())
