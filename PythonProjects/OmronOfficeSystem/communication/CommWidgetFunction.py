import socket
from sys import argv
from sys import exit
from sys import path
from os import getcwd
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMessageBox, QSpinBox, QPushButton, QGridLayout, QLabel, QLineEdit, \
	QTreeWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal, QObject, QItemSelectionModel
from PyQt5.QtGui import QIcon, QPixmap, QCloseEvent
import CommunicationUi
import SocketTcp
import logging.config
import logging


class CommWidgetUi(QWidget):
	server_l = list()  # 用于保存创建的服务器，元素为列表[服务器对象, 本机IP, 监听端口]
	server_item_l = list()  # 用于保存树控件的服务器item
	client_l = list()  # 用于保存创建的客户端，元素为元祖(客户端对象，客户端IP，客户端端口号， 服务器IP, 服务器端口号)
	client_item_l = list()  # 用于保存树控件的客户端item
	qq = """
			QPushButton[name="connectBtn"]{
			background-color: rgb(100, 50, 50,50);
			color: blue;}
			"""

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

		# CSTree标题显示
		# if self.commUi.serverBtn.isChecked():
		# 	self.commUi.CSTree.setHeaderLabels(["服务器IP", "监听端口", "监听中"])
		# else:
		# 	self.commUi.CSTree.setHeaderLabels(["对方IP", "对方端口", "连接状态"])

	def initDialog(self):
		# 添加服务器参数对话框
		self.dialog1 = QDialog()
		self.dialog1.setWindowModality(Qt.ApplicationModal)
		self.dialog1.setWindowTitle("设置服务器监听端口")
		self.portSB = QSpinBox()
		self.portSB.setRange(1, 65535)
		self.portSB.setValue(60000)
		self.portSB.setToolTip("监听端口范围1-65535")
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
		self.serverHostEdit.setInputMask("999.999.999.999;_")
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

		# 端口号重复报错对话框
		self.messageBox1 = QMessageBox()
		self.messageBox1.setText("监听端口已被使用")
		self.messageBox1.setInformativeText("想要重新输入监听端口吗?")
		self.messageBox1.setStandardButtons(QMessageBox.Close | QMessageBox.Yes)
		self.messageBox1.setIcon(QMessageBox.Critical)

		# 未选中服务器或者客户端item时点击删除键
		self.messageBox2 = QMessageBox()
		self.messageBox2.setModal(True)
		self.messageBox2.setText("未选中服务器或客户端！")
		self.messageBox2.setStandardButtons(QMessageBox.Close)
		self.messageBox2.setIcon(QMessageBox.Warning)

	def setupUi(self):
		self.defSignal = Signals()
		# 信号和槽的绑定
		self.commUi.plusBtn.clicked.connect(self.show_server_or_client_dialog)
		self.commUi.minusBtn.clicked.connect(self.delete_server_client)
		self.commUi.serverBtn.clicked.connect(self.refresh_interface)
		self.commUi.clientBtn.clicked.connect(self.refresh_interface)
		self.commUi.connectBtn.pressed.connect(self.startListen)

		self.serverCancelBtn.clicked.connect(self.dialog1.reject)
		self.serverOkBtn.clicked.connect(self.dialog1.accept)
		self.dialog1.accepted.connect(self.add_server)

		self.messageBox1.accepted.connect(self.dialog1.show)
		self.messageBox2.rejected.connect(lambda: self.commUi.connectBtn.setChecked(False))

		self.clientCancelBtn.clicked.connect(self.dialog2.reject)
		self.clientOkBtn.clicked.connect(self.dialog2.accept)
		self.dialog2.accepted.connect(self.add_client)

	def show_server_or_client_dialog(self):
		if self.commUi.serverBtn.isChecked():
			self.dialog1.exec_()
		else:
			self.dialog2.exec_()

	def add_server(self):
		# 添加服务器，在list中显示
		try:
			self.server_l.append([SocketTcp.MyServer(host="", port=self.portSB.value()),
			                      socket.gethostbyname(socket.gethostname()), self.portSB.value()])
			# self.logger.debug(self.server_l)
		except OSError as e:
			if e.errno == 48:
				self.ret = self.messageBox1.exec_()  # yes = 16384  cancel = 4194304
				self.logger.exception(e)
			else:
				self.logger.exception(e)
		else:
			self.server_item_l.append(QTreeWidgetItem())
			self.server_item_l[-1].setText(0, self.server_l[-1][1])
			self.server_item_l[-1].setText(1, str(self.server_l[-1][2]))
			self.commUi.CSTree.addTopLevelItem(self.server_item_l[-1])
			self.commUi.CSTree.clearSelection()
			self.server_item_l[-1].setSelected(True)
			self.logger.debug(self.commUi.CSTree.currentIndex().row())
			self.logger.debug(self.commUi.CSTree.currentItem())
			# self.logger.debug(self.server_item_l)
			# self.logger.debug("add server ok")

	def add_client(self):
		# 添加客户端，在list中显示
		if self.serverHostEdit.text() == "...":
			self.serverHostEdit.setText(socket.gethostbyname(socket.gethostname()))
		self.client_l.append([SocketTcp.MyClient(host=self.serverHostEdit.text(), port=self.serverPortSB.value()),
		                      self.serverHostEdit.text(), self.serverPortSB.value()])
		# self.logger.debug(self.client_l)
		self.client_item_l.append(QTreeWidgetItem())
		self.client_item_l[-1].setText(0, self.client_l[-1][1])
		self.client_item_l[-1].setText(1, str(self.client_l[-1][2]))
		self.commUi.CSTree.addTopLevelItem(self.client_item_l[-1])
		self.commUi.CSTree.clearSelection()
		self.client_item_l[-1].setSelected(True)
		# self.logger.debug(self.client_item_l)
		# self.logger.debug("add client ok")

	def delete_server_client(self):
		if self.commUi.serverBtn.isChecked():
			if len(self.server_item_l) != 0:
				if self.commUi.CSTree.currentItem() is not None:
					# current_index = self.server_item_l.index(self.commUi.CSTree.currentItem())
					self.current_index = self.commUi.CSTree.currentIndex().row()
					self.server_item_l.remove(self.commUi.CSTree.currentItem())
					self.server_l.remove(self.server_l[self.current_index])
					self.commUi.CSTree.takeTopLevelItem(self.current_index)
					# self.logger.debug(self.server_l)
					# self.logger.debug(self.server_item_l)
				else:
					self.messageBox2.show()
		else:
			if len(self.client_item_l) != 0:
				if self.commUi.CSTree.currentItem() is not None:
					# current_index = self.client_item_l.index(self.commUi.CSTree.currentItem())
					self.current_index = self.commUi.CSTree.currentIndex().row()
					self.client_item_l.remove(self.commUi.CSTree.currentItem())
					self.client_l.remove(self.client_l[self.current_index])
					self.commUi.CSTree.takeTopLevelItem(self.current_index)
					# self.logger.debug(self.client_l)
					# self.logger.debug(self.client_item_l)
				else:
					self.messageBox2.show()

	def startListen(self):
		if not self.commUi.connectBtn.isChecked():
			if self.commUi.CSTree.currentItem() is not None:
				self.current_index = self.commUi.CSTree.currentIndex().row()
				self.logger.debug(self.current_index)
				self.server_l[self.current_index][0].my_accept()
			else:
				self.messageBox2.exec_()


	def refresh_interface(self):
		self.sen = self.sender()
		if self.sen.objectName() == "serverBtn":
			self.commUi.connectBtn.setText("开始监听")
			self.commUi.CSTree.setHeaderLabels(["服务器IP", "监听端口", "监听中"])
			for _ in range(0, len(self.client_item_l)):
				self.commUi.CSTree.takeTopLevelItem(0)
			if len(self.server_item_l) != 0:
				self.commUi.CSTree.addTopLevelItems(self.server_item_l)
		if self.sen.objectName() == "clientBtn":
			self.commUi.connectBtn.setText("连接")
			self.commUi.CSTree.setHeaderLabels(["对方IP", "对方端口", "连接状态"])
			for _ in range(0, len(self.server_item_l)):
				self.commUi.CSTree.takeTopLevelItem(0)
			if len(self.client_item_l) != 0:
				self.commUi.CSTree.addTopLevelItems(self.client_item_l)

	# def closeEvent(self, a0: QCloseEvent):


class Signals(QObject):
	a: pyqtBoundSignal
	a = pyqtSignal(str)


if __name__ == "__main__":
	logging.config.fileConfig("./log/logging.conf")
	app = QApplication(argv)
	win = CommWidgetUi()
	win.show()
	exit(app.exec_())
