import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QWidget, QVBoxLayout


class QTextEditDemo(QWidget):
	def __init__(self):
		super(QTextEditDemo, self).__init__()

		self.setWindowTitle("这是一个QTextEdit案例")

		self.text_edit = QTextEdit(self)
		self.button_set_plaint = QPushButton("设置无格式文本", self)
		self.button_set_html = QPushButton("设置HTML文本", self)
		self.button_plaint = QPushButton("获取无格式文本", self)
		self.button_html = QPushButton("获取HTML文本", self)

		self.v_layout = QVBoxLayout(self)
		self.v_layout.addWidget(self.text_edit)
		self.v_layout.addWidget(self.button_set_plaint)
		self.v_layout.addWidget(self.button_set_html)
		self.v_layout.addWidget(self.button_plaint)
		self.v_layout.addWidget(self.button_html)

		self.button_set_plaint.clicked.connect(self.clicked_button_set_plaint)
		self.button_set_html.clicked.connect(self.clicked_button_set_html)
		self.button_plaint.clicked.connect(self.clicked_button_plaint)
		self.button_html.clicked.connect(self.clicked_button_html)

	def clicked_button_set_plaint(self):
		self.text_edit.setPlainText("你好啊！")

	def clicked_button_set_html(self):
		self.text_edit.setHtml('<font color="blue" size="5">你好啊！</font>')

	def clicked_button_plaint(self):
		print(self.text_edit.toPlainText())

	def clicked_button_html(self):
		print(self.text_edit.toHtml())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QTextEditDemo()
	widget.show()
	sys.exit(app.exec_())
