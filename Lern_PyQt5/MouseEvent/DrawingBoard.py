import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QMouseEvent, QPaintEvent, QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QPointF, QRect


class DrawingBoard(QWidget):
	def __init__(self):
		super(DrawingBoard, self).__init__()
		self.setWindowTitle("绘画板")
		self.resize(500, 500)
		self.saveButton = QPushButton("保存图片", self)
		self.saveButton.move(320, 410)
		self.saveButton.clicked.connect(self.savePixmap)
		self.openButton = QPushButton("打开图片", self)
		self.openButton.move(220, 410)
		self.openButton.clicked.connect(self.openPixmap)

		self.startingPoint = QPointF(0, 0)
		self.endPoint = QPointF(0, 0)

		# 创建一个QPixmap用保存绘画好的图形，如果直接画到窗口执行update()后之前画的就没有了
		self.pix = QPixmap(400, 400)
		self.pix.fill(Qt.cyan)

		self.pen = QPen()
		self.pen.setColor(Qt.red)
		self.pen.setWidth(0)  # 防止在窗口一打开时会在QPointF(0, 0)位置画一个点

	def paintEvent(self, a0: QPaintEvent):
		self.painter = QPainter()

		self.painter.begin(self.pix)
		self.painter.setPen(self.pen)
		self.painter.drawLine(self.startingPoint, self.endPoint)
		self.painter.end()

		self.painter.begin(self)
		print(1)
		self.painter.drawPixmap(0, 0, self.pix)
		self.painter.end()

		self.startingPoint = self.endPoint

	def mouseMoveEvent(self, a0: QMouseEvent):
		self.endPoint = a0.windowPos()
		self.update()  # 调用paintEvent()，更新界面

	def mousePressEvent(self, a0: QMouseEvent):
		self.startingPoint = a0.windowPos()
		self.pen.setWidth(5)

	def savePixmap(self):
		SaveFileDialog = QFileDialog(None, "SaveFileDialog对话框的标题",
		                             "/Users/qianshaoqing/Documents/Python/Lern_PyQt5/MouseEvent/images")
		SaveFileDialog.setAcceptMode(QFileDialog.AcceptSave)  # 设置为保存文件模式
		SaveFileDialog.setDefaultSuffix(".png")  # 设置保存文件名后缀

		if SaveFileDialog.exec_():  # 点击QFileDialog中cancel时返回0，点击QFileDialog中open时返回1
			print("1, 获取被保存文件所在目录路径：", SaveFileDialog.directory().path())  # 获取选中文件的目录路径
			fileName = SaveFileDialog.selectedFiles()
			print("2, 获取被保存文件路径：", fileName)

		ret = self.pix.save(fileName[0])  # 返回True表示保存成功
		if ret == 1:
			print("图片保存成功", ret)
		else:
			print("图片保存失败")

	def openPixmap(self):
		OpenFileDialog = QFileDialog(None, "OpenFileDialog对话框的标题",
		                             "/Users/qianshaoqing/Documents/Python/Lern_PyQt5/MouseEvent/images/pix.png",
		                             "image files(*.png *.jpg *.ico)")
		OpenFileDialog.setAcceptMode(QFileDialog.AcceptOpen)  # 设置为打开文件模式
		OpenFileDialog.setOption(True)  # 设置为只能选中文件
		OpenFileDialog.setFileMode(QFileDialog.ExistingFiles)  # 可选中多个文件

		if OpenFileDialog.exec_():  # 点击QFileDialog中cancel时返回0，点击QFileDialog中open时返回1
			print("1, 获取文件所在目录路径：", OpenFileDialog.directory().path())  # 获取选中文件的目录路径
			fileNames = OpenFileDialog.selectedFiles()
			print("2, 获取文件路径：", fileNames)
			# 打开选择的图片，原理：之所在指定QPixmap路径后图片自动加载到了窗口，是因为在选择好文件路径关闭对话框时会自动调用paintEvent()
			self.pix.load(fileNames[0])
			self.pen.setWidth(0)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = DrawingBoard()
	window.show()
	sys.exit(app.exec_())