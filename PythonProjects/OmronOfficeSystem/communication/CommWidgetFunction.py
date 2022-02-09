import socket
from sys import argv
from sys import exit
from sys import path
from os import getcwd
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMessageBox, QSpinBox, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
import CommunicationUi
import SocketTcp
import logging.config
import logging


class CommWidgetUi(QWidget):
	server_l = list()  # 用于保存创建的服务器，元素为元祖(服务器对象, 本机IP, 监听端口)

	def __init__(self):
		super(CommWidgetUi, self).__init__()
		self.logger = logging.getLogger("applog")
		self.commUi = CommunicationUi.Ui_communication()
		self.commUi.setupUi(self)
		self.initWidget()
		self.initDialog()
		self.setupUi()

	def initWidget(self):
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

	def initDialog(self):
		# 添加服务器参数对话框
		self.dialog1 = QDialog()
		self.dialog1.setWindowTitle("设置服务器监听端口")
		self.portSB = QSpinBox()
		self.portSB.setRange(1, 65535)
		portLab = QLabel("监听端口:")
		self.serverCancelBtn = QPushButton("取消")
		self.serverOkBtn = QPushButton("确定")
		gLayout = QGridLayout(self.dialog1)
		gLayout.addWidget(portLab, 0, 0, 1, 1)
		gLayout.addWidget(self.portSB, 0, 1, 1, 1)
		gLayout.addWidget(self.serverCancelBtn, 1, 0, 1, 1)
		gLayout.addWidget(self.serverOkBtn, 1, 1, 1, 1)

		# 添加客户端参数对话框
		self.dialog2 = QDialog()
		self.dialog2.setWindowTitle("设置对方IP地址和端口号")
		self.serverHostEdit = QLineEdit()
		self.serverHostEdit.setInputMask("000.000.000.000;_")
		self.serverHostLab = QLabel("对方IP:")
		self.serverPortSB = QSpinBox()
		self.serverPortSB.setRange(1, 65535)
		self.serverPortSB.setValue(60000)
		self.serverPortSB.setToolTip("范围：1-65535")
		self.serverPortLab = QLabel("对方端口:")
		self.clientCancelBtn = QPushButton("取消")
		self.clientOkBtn = QPushButton("确定")
		gLayout = QGridLayout(self.dialog2)
		gLayout.addWidget(self.serverHostLab, 0, 0, 1, 1)
		gLayout.addWidget(self.serverHostEdit, 0, 1, 1, 1)
		gLayout.addWidget(self.serverPortLab, 1, 0, 1, 1)
		gLayout.addWidget(self.serverPortSB, 1, 1, 1, 1)
		gLayout.addWidget(self.clientCancelBtn, 2, 0, 1, 1)
		gLayout.addWidget(self.clientOkBtn, 2, 1, 1, 1)

	def setupUi(self):
		# 信号和槽的绑定
		self.commUi.plusBtn.clicked.connect(self.show_server_or_client_dialog)

		self.serverCancelBtn.clicked.connect(self.dialog1.reject)
		self.serverOkBtn.clicked.connect(self.dialog1.accept)
		self.dialog1.accepted.connect(self.add_server_accepted)

		self.clientCancelBtn.clicked.connect(self.dialog2.reject)
		self.clientOkBtn.clicked.connect(self.dialog2.accept)
		self.dialog2.accepted.connect(self.add_client_accepted)

	def show_server_or_client_dialog(self):
		if self.commUi.serverBtn.isChecked():
			self.dialog1.exec_()
		if self.commUi.clientBtn.isChecked():
			self.dialog2.exec_()

	def add_server_accepted(self):
		# 添加服务器，在list中显示
		self.server_l.append((SocketTcp.MyServer(host="", port=self.portSB.value()), socket.gethostbyname(socket.gethostname()),
		                      self.portSB.value()))
		self.logger.debug(self.server_l)
		self.logger.debug("add server ok")

	def add_client_accepted(self):
		# 添加客户端，在list中显示
		self.logger.debug("add client ok")
		pass


if __name__ == "__main__":
	logging.config.fileConfig("./log/logging.conf")
	app = QApplication(argv)
	win = CommWidgetUi()
	win.show()
	exit(app.exec_())
