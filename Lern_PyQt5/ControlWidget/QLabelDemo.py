"""
QLable控件
set.Alignment(): 设置文本对齐方式
setIndent(): 设置文本缩进
text(): 获取文本内容
setBuddy(): 设置伙伴关系
setText(): 设置文本内容
selectedText(): 返回所选择的字符
setWordWrap(): 设置是否允许换行

QLable常用的信号（事件）：
1. 当鼠标滑过QLable控件时触发：linkHovered()
2. 当鼠标单击QLable控件时触发：linkActivated()
"""
import sys
from typing import Union

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPalette, QPixmap  # 调色板
from PyQt5.QtCore import Qt


class QLableDemo(QMainWindow):

	def __init__(self):
		super(QLableDemo, self).__init__()
		self.setWindowTitle("我是一个QLable控件演示")
		self.setGeometry(400, 400, 500, 500)
		self.status_bar = self.statusBar()

		self.centralWidget = QWidget(self)
		self.widget = QWidget(self.centralWidget)

		self.lable1 = QLabel(self.widget)
		# self.lable1.move(0, 0)
		self.lable1.setText("<font color=black>按钮1</font>")
		self.lable1.setAutoFillBackground(True)
		self.palette = QPalette()
		self.palette.setColor(QPalette.Window, Qt.blue)  # 设置的是背景色
		self.lable1.setPalette(self.palette)
		self.lable1.setAlignment(Qt.AlignCenter)

		self.lable2 = QLabel(self.widget)
		# self.lable2.move(0, 15)
		self.lable2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

		self.lable3 = QLabel(self.widget)
		# self.lable3.move(0, 30)
		self.lable3.setToolTip("这是一个图片标签")
		self.lable3.setAlignment(Qt.AlignHCenter)
		self.lable3.setPixmap(QPixmap("./images/1.ico"))  # lable设置为图像

		self.lable4 = QLabel(self.widget)
		# self.lable4.setOpenExternalLinks(True)  # 打开网页和linkActivated()是互斥的
		self.lable4.setText("<a href='http://www.baidu.com'>打开百度连接</a>")
		self.lable4.setAlignment(Qt.AlignRight)
		self.lable4.setToolTip("这是一个超文本连接哦")

		self.layout = QVBoxLayout(self.widget)
		self.layout.addWidget(self.lable1)
		self.layout.addWidget(self.lable2)  # 如果将lable2放到垂直布局内，linkHovered()事件只会执行一次，不知道为什么！！！
		self.layout.addWidget(self.lable3)
		self.layout.addWidget(self.lable4)
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.centralWidget)

		self.lable2.linkHovered.connect(self.linkHovered)
		self.lable4.linkActivated.connect(self.linkActivated)

	def linkHovered(self):
		print("鼠标滑过了lable2")
		self.sender_1 = self.sender()
		self.status_bar.showMessage(self.sender_1.text(), 1000)

	def linkActivated(self):
		print("鼠标点击了lable4")
		self.sender_1 = self.sender()
		self.status_bar.showMessage(self.sender_1.text(), 1000)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QLableDemo()
	mainWindow.show()
	sys.exit(app.exec_())
