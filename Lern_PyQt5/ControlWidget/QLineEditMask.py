"""
def inputMask ()                      # 获取输入的掩码
def setInputMask ("mask;_")          # 设置输入的掩码，分号后面的"_"是指默认显示的字符。

A: ASCII字母字符是必须的，取值空间是A-Z,a-z
a: ASCII 字母字符是允许的但不是必须的.
N: ASCII字母字符是必须的. A-Z, a-z, 0-9.
n: ASCII 字母字符是允许的但不是必须的.
X: 任何字符都可以，是必须需要的.
x: 任何字符都允许的，但不是必须需要的.
9: ASCII 数字是必须要的. 0-9.
0: ASCII 数字是允许的，但不是必须要的.
D: ASCII  数字是必须要的. 1-9.
d: ASCII 数字是允许的，但不是必须要的 (1-9).
#: ASCII 数字或加减符号是允许的，但不是必须要的.
H: 十六进制数据字符是必须要的. A-F, a-f, 0-9.
h: 十六进制数据字符是允许的，但不是必须要的.
B: 二进制数据字符是必须要的. 0-1.
b: 二进制数据字符是允许的，但不是必须要的.
>: 所有的字符字母都都大写的.
<: 所有的字符字幕都是小写的.
!: 关闭大小写.
\: 使用 \ 去转义上面的字符，如果再需要显示上述字符的时候.
"""
import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout, QApplication


class QLineEditMask(QWidget):
	def __init__(self):
		super(QLineEditMask, self).__init__()
		self.setWindowTitle("这是一个QLineEditMask案例")

		self.line_edit_ip = QLineEdit(self)
		self.line_edit_mac = QLineEdit(self)
		self.line_edit_datetime = QLineEdit(self)
		self.f_layout = QFormLayout(self)
		self.f_layout.addRow("ip", self.line_edit_ip)
		self.f_layout.addRow("mac", self.line_edit_mac)
		self.f_layout.addRow("date", self.line_edit_datetime)

		self.line_edit_ip.setInputMask("000.000.000.000;_")
		self.line_edit_mac.setInputMask(">HH.HH.HH.HH;_")  # >表示输入的字符默认自动转换为大写字母
		self.line_edit_datetime.setInputMask("9999-99-99 99:99:99;_")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = QLineEditMask()
	widget.show()
	sys.exit(app.exec_())
