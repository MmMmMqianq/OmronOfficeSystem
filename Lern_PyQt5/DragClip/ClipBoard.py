import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap


class ClipBoardDemo(QWidget):
	def __init__(self):
		super(ClipBoardDemo, self).__init__()

		self.setWindowTitle("ClipBoard 实例")
		# self.resize(500, 500)

		self.copyTextButton = QPushButton("复制文本")
		self.pasteTextButton = QPushButton("粘贴文本")
		self.copyImageButton = QPushButton("复制图像")
		self.pasteImageButton = QPushButton("粘贴图像")

		self.label = QLabel("label")

		gLayout = QGridLayout(self)
		gLayout.addWidget(self.copyTextButton, 0, 0, 1, 1)
		gLayout.addWidget(self.pasteTextButton, 1, 0, 1, 1)
		gLayout.addWidget(self.copyImageButton, 0, 1, 1, 1)
		gLayout.addWidget(self.pasteImageButton, 1, 1, 1, 1)
		gLayout.addWidget(self.label, 2, 0, 1, 1)

		self.copyTextButton.clicked.connect(self.copyText)
		self.pasteTextButton.clicked.connect(self.pasteText)

		self.copyImageButton.clicked.connect(self.copyImage)
		self.pasteImageButton.clicked.connect(self.pasteImage)

	def copyText(self):
		clipBoard = QApplication.clipboard()
		clipBoard.setText("我是被复制的文字，哈哈哈")

	def pasteText(self):
		clipBoard = QApplication.clipboard()
		self.label.setText(clipBoard.text())

	def copyImage(self):
		clipBoard = QApplication.clipboard()
		clipBoard.setPixmap(QPixmap("./images/1.ico"))

	def pasteImage(self):
		clipBoard = QApplication.clipboard()
		self.label.setPixmap(clipBoard.pixmap())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = ClipBoardDemo()
	window.show()
	sys.exit(app.exec_())
