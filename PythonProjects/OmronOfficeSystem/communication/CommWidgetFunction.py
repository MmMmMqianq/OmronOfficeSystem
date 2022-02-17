import socket
from sys import argv
from sys import exit
from sys import path
from os import getcwd
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMessageBox, QSpinBox, QPushButton, QGridLayout, QLabel, \
	QLineEdit, \
	QTreeWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal, QObject, QItemSelectionModel
from PyQt5.QtGui import QIcon, QPixmap, QCloseEvent
import CommunicationUi
import SocketTcp
import logging.config
import logging


class CommWidgetUi(QWidget):

	def __init__(self):
		super(CommWidgetUi, self).__init__()
		self.logger = logging.getLogger("applog")
		self.commUi = CommunicationUi.Ui_communication()
		self.commUi.setupUi(self)
		self.initVariable()
		self.initWidget()
		self.initDialog()
		self.setupUi()

	def initVariable(self):
		self.server_l = list()  # 用于保存创建的服务器，元素为列表[服务器对象, 本机IP, 监听端口]
		self.server_top_l = list()  # 用于保存树控件的服务器top item
		self.server_child_l = list()  # 用于保存所有top item的child的信息， child为服务器所连得客户端信息组成的列表，[[], [], [], []]
		self.server_child_item_l = list()  # 用于保存top item的child item列表
		self.client_l = list()  # 用于保存创建的客户端，元素为元祖(客户端对象，客户端IP，客户端端口号， 服务器IP, 服务器端口号)
		self.client_item_l = list()  # 用于保存树控件的客户端item
		self.top_count = int()  # top item的数量

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
		self.messageBox2.setText("没有可删除的服务器或客户端！")
		self.messageBox2.setStandardButtons(QMessageBox.Close)
		self.messageBox2.setIcon(QMessageBox.Warning)

		# 未选中服务器时点击开始监听按钮提示该警告窗口
		self.messageBox3 = QMessageBox()
		self.messageBox3.setModal(True)
		self.messageBox3.setText("请选择要监听的服务器！")
		self.messageBox3.setStandardButtons(QMessageBox.Close)
		self.messageBox3.setIcon(QMessageBox.Warning)

	def setupUi(self):
		self.defSignal = Signals()
		self.root = self.commUi.CSTree.invisibleRootItem()
		self.local_ip = SocketTcp.get_local_ip()
		# 信号和槽的绑定
		self.commUi.plusBtn.clicked.connect(self.show_server_or_client_dialog)
		self.commUi.minusBtn.clicked.connect(self.delete_server_client)
		self.commUi.serverBtn.clicked.connect(self.refresh_interface)
		self.commUi.clientBtn.clicked.connect(self.refresh_interface)
		self.commUi.connectBtn.pressed.connect(self.startListen)
		self.commUi.connectBtn.pressed.connect(self.stop_listen)
		self.commUi.CSTree.itemClicked.connect(self.refresh_connect_button)

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
			                      self.local_ip, self.portSB.value()])
			# self.logger.debug(self.server_l)
		except OSError as e:
			if e.errno == 48:
				self.ret = self.messageBox1.exec_()  # yes = 16384  cancel = 4194304
				self.logger.exception(e)
			else:
				self.logger.exception(e)
		else:
			self.server_top_l.append(QTreeWidgetItem())
			self.server_top_l[-1].setText(0, self.server_l[-1][1])
			self.server_top_l[-1].setText(1, str(self.server_l[-1][2]))
			self.commUi.CSTree.addTopLevelItem(self.server_top_l[-1])
			self.server_child_l.append([])  # 由于还没有客户端连接所以append空列表
			self.commUi.CSTree.clearSelection()
			self.server_top_l[-1].setSelected(True)

			self.commUi.connectBtn.setChecked(False)
			self.server_l[-1][0].server_signal.accepted_done.connect(self.add_client_to_server)
			self.server_l[-1][0].server_No = self.top_count - 1
			self.server_l[-1][0].my_accept()
			self.server_l[-1][0].server_signal.listened_done.connect(self.auto_set_connect_button)
			self.server_l[-1][0].server_signal.listened_done.emit("auto_listened_done")
		# self.logger.debug(self.server_top_l)
		# self.logger.debug("add server ok")

	def add_client(self):
		# 添加客户端，在list中显示
		if self.serverHostEdit.text() == "...":
			self.serverHostEdit.setText(self.local_ip)
		self.client_l.append([SocketTcp.MyClient(host=self.serverHostEdit.text(), port=self.serverPortSB.value()),
		                      self.serverHostEdit.text(), self.serverPortSB.value()])
		# self.logger.debug(self.client_l)
		self.client_item_l.append(QTreeWidgetItem())
		self.client_item_l[-1].setText(0, self.client_l[-1][1])
		self.client_item_l[-1].setText(1, str(self.client_l[-1][2]))
		self.commUi.CSTree.addTopLevelItem(self.client_item_l[-1])
		self.commUi.CSTree.clearSelection()
		self.client_item_l[-1].setSelected(True)

	def delete_server_client(self):
		self.top_count = self.root.childCount()
		if self.commUi.serverBtn.isChecked():  # 删除服务器
			# if len(self.server_top_l) != 0:
			if self.top_count != 0:
				if self.commUi.CSTree.currentItem() is not None:
					# current_index = self.server_top_l.index(self.commUi.CSTree.currentItem())
					self.current_index = self.commUi.CSTree.currentIndex().row()
					self.server_top_l.pop(self.current_index)
					self.server_l.pop(self.current_index)
					self.commUi.CSTree.takeTopLevelItem(self.current_index)
				# self.logger.debug(self.server_l)
				# self.logger.debug(self.server_top_l)
				else:
					self.server_top_l.pop()
					self.server_l.pop()
					self.commUi.CSTree.takeTopLevelItem(self.top_count - 1)
			else:
				self.messageBox2.show()
		else:  # 删除客户端
			# if len(self.client_item_l) != 0:
			if self.top_count != 0:
				if self.commUi.CSTree.currentItem() is not None:
					# current_index = self.client_item_l.index(self.commUi.CSTree.currentItem())
					self.current_index = self.commUi.CSTree.currentIndex().row()
					self.client_item_l.pop(self.current_index)
					self.client_l.pop(self.current_index)
					self.commUi.CSTree.takeTopLevelItem(self.current_index)
				# self.logger.debug(self.client_l)
				# self.logger.debug(self.client_item_l)
				else:
					# self.messageBox2.show()
					self.client_item_l.pop()
					self.client_l.pop()
					self.commUi.CSTree.takeTopLevelItem(self.top_count - 1)
			else:
				self.messageBox2.show()

	def add_client_to_server(self, l):
		# l为二维列表:[[服务器监听状态, 服务器编号, 线程名, 服务器IP, 服务器端口号, 客户端IP, 客户端端口号, 客户端连接, 客户端编号, 客户端连接状态], [], []...]
		self.logger.debug(l)
		print("accept信号已经触发。。。")
		child_item = QTreeWidgetItem()
		child_item.setTextAlignment(0, 1)
		child_item.setText(0, l[-1][5] + "[%d]" % l[-1][6])
		# child_item.setText(2, str(self.server_child_l[No][-1][3]))
		self.server_top_l[l[-1][1]].addChild(child_item)

	def startListen(self):
		if not self.commUi.connectBtn.isChecked():
			self.commUi.connectBtn.setText("停止监听")
			self.top_count = self.root.childCount()
			if self.top_count != 0:
				if self.commUi.CSTree.currentItem() is not None:
					self.current_index = self.commUi.CSTree.currentIndex().row()
					# self.logger.debug(self.current_index)
					self.server_l[self.current_index][0].server_signal.accepted_done.connect(self.add_client_to_server)
					self.server_l[self.current_index][0].server_No = self.current_index
					self.server_l[self.current_index][0].my_accept()
				else:
					# self.logger.debug(self.server_l[-1])
					self.server_l[-1][0].server_signal.accepted_done.connect(self.add_client_to_server)
					self.server_l[-1][0].server_No = self.top_count - 1
					self.server_l[-1][0].my_accept()
			else:
				self.messageBox3.exec_()

	def stop_listen(self):
		if self.commUi.connectBtn.isChecked():
			if self.commUi.CSTree.currentItem() is not None:  # top item是否被选中执行不同的操作
				if self.commUi.CSTree.currentIndex().parent() is None:  # 判断当前选中的是不是top item
					self.commUi.connectBtn.setText("开始监听")
					self.current_index = self.commUi.CSTree.currentIndex().row()
					children = self.commUi.CSTree.currentItem().takeChildren()
					for i in children:
						del i
					self.server_l[self.current_index][0].stop_listen()
			else:
				self.commUi.connectBtn.setText("开始监听")
				children = self.server_top_l[-1].takeChildren()
				for i in children:
					del i
				self.server_l[-1][0].stop_listen()

	def refresh_interface(self):
		self.sen = self.sender()
		if self.sen.objectName() == "serverBtn":
			self.commUi.connectBtn.setText("开始监听")
			self.commUi.CSTree.setHeaderLabels(["服务器IP", "监听端口", "监听中"])
			for _ in range(0, len(self.client_item_l)):
				self.commUi.CSTree.takeTopLevelItem(0)
			if len(self.server_top_l) != 0:
				self.commUi.CSTree.addTopLevelItems(self.server_top_l)
		if self.sen.objectName() == "clientBtn":
			self.commUi.connectBtn.setText("连接")
			self.commUi.CSTree.setHeaderLabels(["对方IP", "对方端口", "连接状态"])
			for _ in range(0, len(self.server_top_l)):
				self.commUi.CSTree.takeTopLevelItem(0)
			if len(self.client_item_l) != 0:
				self.commUi.CSTree.addTopLevelItems(self.client_item_l)

	def refresh_connect_button(self, item: QTreeWidgetItem, column):
		if item.parent() is None:
			clicked_index = self.commUi.CSTree.currentIndex().row()
			if self.server_l[clicked_index][0].listening:
				self.commUi.connectBtn.setChecked(True)
				self.commUi.connectBtn.setText("停止监听")
		else:
			self.commUi.connectBtn.setChecked(True)
			self.commUi.connectBtn.setText("断开")

	def auto_set_connect_button(self):
		self.commUi.connectBtn.setChecked(True)
		self.commUi.connectBtn.setText("停止监听")

# def closeEvent(self, a0: QCloseEvent):


class Signals(QObject):
	a: pyqtBoundSignal
	start_lis = pyqtSignal(str)


if __name__ == "__main__":
	logging.config.fileConfig("./log/logging.conf")
	app = QApplication(argv)
	win = CommWidgetUi()
	win.show()
	exit(app.exec_())
