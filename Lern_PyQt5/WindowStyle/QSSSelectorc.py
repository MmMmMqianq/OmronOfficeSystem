"""
QSS(Qt Style Sheet):用于设置控件的样式
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QComboBox
from PyQt5.QtCore import Qt


class QSSSelector(QWidget):
	def __init__(self):
		super(QSSSelector, self).__init__()

		self.setWindowTitle("窗口最大化和最小化")
		self.resize(500, 500)

		self.button1 = QPushButton("按钮1")
		self.button2 = QPushButton("按钮2")
		self.button2.setProperty("name", "btn2")  # 设置的属性是以键值对方式
		self.button3 = QPushButton("按钮3")
		self.button3.setProperty("name", "btn3")

		self.comboBox = QComboBox()
		self.comboBox.setObjectName("cb")  # 设置对象名字
		self.comboBox.addItems(["windows", "macOS", "linux"])

		self.vLayout = QVBoxLayout(self)
		self.vLayout.addWidget(self.button1)
		self.vLayout.addWidget(self.button2)
		self.vLayout.addWidget(self.button3)
		self.vLayout.addWidget(self.comboBox)

		# 选择器，将所有的PushButton背景改为红色
		qssStyle = """
			QPushButton{
				background-color: red;
			}
				
			QPushButton[name="btn2"]{
				background-color: cyan;
				color: blue;
				height: 60;
				font-size: 30px
			}
			
			QComboBox#cb::drop-down {
				image: url(./images/2.png);
			}
		"""
		self.setStyleSheet(qssStyle)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QSSSelector()
	window.show()
	sys.exit(app.exec_())