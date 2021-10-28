import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QGridLayout, QLabel
from PyQt5.QtGui import QDragEnterEvent, QDropEvent


class ComboxDragDrop(QComboBox):
	def __init__(self):
		super(ComboxDragDrop, self).__init__()
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event: QDragEnterEvent):
		# 获取拖拽的内容
		dragDate = event.mimeData()  # 返回放置在小部件上的数据及其关联的 MIME 类型信息。
									 # QMimeData 用于描述可以存储在剪贴板中的信息，并通过拖放机制进行传输。
									 # QMimeData 对象将它们保存的数据与相应的 MIME 类型相关联，以确保信息可以在应用程序之间安全传输，
								  	 # 并在同一应用程序内进行复制。
		print("1. event.mimeData() = ：", dragDate)
		# 判断拖拽的内容，设置被拖拽的内容是否能够被接受
		if dragDate.hasText():
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, e: QDropEvent):
		# 放下后执行的动作
		self.addItem(e.mimeData().text())
		print("2. e.mimeData().text() = ", e.mimeData().text())


class DragDropDemo(QWidget):
	def __init__(self):
		super(DragDropDemo, self).__init__()

		label = QLabel("请先选中输入框里的文本并拖拽到comboBox里")
		lineEdit = QLineEdit()
		lineEdit.setDragEnabled(True)  # 启动lineEdit拖拽功能
		comboBox = ComboxDragDrop()

		gLayout = QGridLayout(self)
		gLayout.addWidget(label, 0, 0, 1, 2)
		gLayout.addWidget(lineEdit, 1, 0, 1, 1)
		gLayout.addWidget(comboBox, 1, 1, 1, 1)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = DragDropDemo()
	window.show()
	sys.exit(app.exec_())
