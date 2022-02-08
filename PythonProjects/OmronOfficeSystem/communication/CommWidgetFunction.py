from sys import argv
from sys import exit
from sys import path
from os import getcwd
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon, QPixmap
import CommunicationUi


class CommWidgetUi(QWidget):
	def __init__(self):
		super(CommWidgetUi, self).__init__()
		self.commUi = CommunicationUi.Ui_communication()
		self.commUi.setupUi(self)
		self.setupUi()
		print(getcwd())

	def setupUi(self):
		# 设置图标路径，由于工作路径的问题所以要重写图标路径
		icon = QIcon()
		icon.addPixmap(QPixmap("./communication/images/plus.png"), QIcon.Normal, QIcon.Off)
		self.commUi.plusBtn.setIcon(icon)
		icon2 = QIcon()
		icon2.addPixmap(QPixmap("./communication/images/minus.png"), QIcon.Normal, QIcon.Off)
		self.commUi.minusBtn.setIcon(icon2)
		icon3 = QIcon()
		icon3.addPixmap(QPixmap("./communication/images/cog.png"), QIcon.Normal, QIcon.Off)
		self.commUi.settingBtn.setIcon(icon3)


if __name__ == "__main__":
	app = QApplication(argv)
	win = CommWidgetUi()
	win.show()
	exit(app.exec_())
