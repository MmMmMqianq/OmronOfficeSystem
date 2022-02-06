import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow, QScrollArea, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt


class QScrollAreaDemo(QMainWindow):
	def __init__(self):
		super(QScrollAreaDemo, self).__init__()

		self.setWindowTitle("这是一个QScrollArea实例")
		self.resize(500, 500)

		self.pushBtn1 = QPushButton("1")
		self.pushBtn2 = QPushButton("2")
		self.pushBtn3 = QPushButton("3")
		self.pushBtn4 = QPushButton("4")
		self.pushBtn5 = QPushButton("5")
		self.pushBtn6 = QPushButton("6")
		self.pushBtn7 = QPushButton("7")
		self.pushBtn8 = QPushButton("8")
		self.pushBtn9 = QPushButton("9")

		self.widget = QWidget()
		self.widget.resize(200, 200)

		self.vLayout = QVBoxLayout(self.widget)
		self.vLayout.addWidget(self.pushBtn1)
		self.vLayout.addWidget(self.pushBtn2)
		self.vLayout.addWidget(self.pushBtn3)
		self.vLayout.addWidget(self.pushBtn4)
		self.vLayout.addWidget(self.pushBtn5)
		self.vLayout.addWidget(self.pushBtn6)
		self.vLayout.addWidget(self.pushBtn7)
		self.vLayout.addWidget(self.pushBtn8)

		self.scrollArea = QScrollArea(self)
		self.scrollArea.resize(150, 200)
		self.scrollArea.setAlignment(Qt.AlignCenter)  # QWidget宽度小于QScrollArea时有效果
		self.scrollArea.setWidgetResizable(False)  # 设置为True时，没有水平滚动条，宽度自适应QWidget大小
		self.scrollArea.setWidget(self.widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QScrollAreaDemo()
    window.show()
    sys.exit(app.exec_())