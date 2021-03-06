import socket
import string
import threading
import time
from sys import argv
from sys import exit
from sys import path
from os import getcwd
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMessageBox, QSpinBox, QPushButton, QGridLayout, QLabel, \
	QLineEdit, QTreeWidgetItem, QHeaderView, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal, pyqtBoundSignal, QObject, QEvent
from PyQt5.QtGui import QIcon, QPixmap
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
		self.server_pool = list()  # 用于保存创建的服务器，元素为列表[服务器对象, 本机IP, 监听端口, 服务器号]
		self.server_count = 0  # 用于累计服务器数量
		self.server_top_pool = list()  # 用于保存树控件的服务器top item
		# self.server_child_l = list()  # 用于保存所有top item的child的信息， child为服务器所连得客户端信息组成的列表，[[], [], [], []]
		# self.server_child_item_pool = list()  # 用于保存top item的child item列表
		self.client_pool = list()  # 用于保存创建的客户端，元素为元祖(客户端对象，客户端IP，客户端端口号， 服务器IP, 服务器端口号)
		self.client_item_pool = list()  # 用于保存树控件的客户端item
		self.top_count = int()  # top item的数量
		self.current_index = int()
		self.isClientDisconnected = False
		self.info_pool = list()  # 用于保存所有的消息列表
		self.info_No = 1
		self.checked_pool = list()  # 用保存overViewTree中哪两个top item的复选框被勾选了。在计算时间差时需要用到。
		self.in_sever_interface = True
		self.in_client_interface = False

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

		# 将Tree的列宽改为自适应文本
		self.commUi.CSTree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.commUi.overViewTree.header().setSectionResizeMode(QHeaderView.ResizeToContents)

		# 启动时IP标签设置为不显示
		self.commUi.serverIPLab.setHidden(True)
		self.commUi.serverPortLab.setHidden(True)
		self.commUi.serverIPLab2.setHidden(True)
		self.commUi.serverPortLab2.setHidden(True)
		self.commUi.clientIPLab.setHidden(True)
		self.commUi.clientIPLab2.setHidden(True)
		self.commUi.clientPortLab.setHidden(True)
		self.commUi.clientPortLab2.setHidden(True)

		# 默认隐藏ASC显示窗口
		self.commUi.receiveDataAscEdit.setHidden(True)
		self.commUi.sendDataAscEdit.setHidden(True)

		# 设置QTextEdit过滤器
		keyPressEster = KeyPressEster(self)
		self.commUi.sendDataHexEdit.installEventFilter(keyPressEster)

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

		# 未选择被监听的客户端时点击发送按钮
		self.messageBox4 = QMessageBox()
		self.messageBox4.setModal(True)
		self.messageBox4.setText("请选择数据发送至哪一个客户端！")
		self.messageBox4.setStandardButtons(QMessageBox.Close)
		self.messageBox4.setIcon(QMessageBox.Warning)

		# 网络异常报错
		self.messageBox5 = QMessageBox()
		self.messageBox5.setModal(True)
		self.messageBox5.setText("请检查网络连接！")
		self.messageBox5.setStandardButtons(QMessageBox.Close)
		self.messageBox5.setIcon(QMessageBox.Warning)

		# 删除服务器时选中的是所连接的客户端，应当选中服务器
		self.messageBox6 = QMessageBox()
		self.messageBox6.setModal(True)
		self.messageBox6.setText("请选择要删除的服务器！\n如果想删除所监听的客户端，\n请点击\"断开\"按钮！")
		self.messageBox6.setStandardButtons(QMessageBox.Close)
		self.messageBox6.setIcon(QMessageBox.Warning)

		# 清楚收发数据框
		self.messageBox7 = QMessageBox()
		self.messageBox7.setModal(True)
		self.messageBox7.setText("确定要清除%d条通信数据吗？" % len(self.info_pool))
		self.messageBox7.setStandardButtons(QMessageBox.Close | QMessageBox.Yes)
		self.messageBox7.setIcon(QMessageBox.Warning)

		# sendDataHexEdit字符为奇数个，不满足字节要求
		self.messageBox8 = QMessageBox()
		self.messageBox8.setModal(True)
		self.messageBox8.setText("请输入正确的字节数据！当前字符数%d个！" % len(self.commUi.sendDataHexEdit.toPlainText()))
		self.messageBox8.setStandardButtons(QMessageBox.Close)
		self.messageBox8.setIcon(QMessageBox.Warning)

	def setupUi(self):
		self.defSignal = Signals()
		self.root = self.commUi.CSTree.invisibleRootItem()
		self.local_ip = SocketTcp.get_local_ip(self.messageBox5)
		# 信号和槽的绑定
		self.commUi.plusBtn.clicked.connect(self.show_server_or_client_dialog)
		self.commUi.minusBtn.clicked.connect(self.delete_server_or_client)
		self.commUi.serverBtn.clicked.connect(self.refresh_CSTree_interface)
		self.commUi.clientBtn.clicked.connect(self.refresh_CSTree_interface)
		self.commUi.connectBtn.clicked.connect(self.startListen)
		self.commUi.connectBtn.clicked.connect(self.stop_listen_or_disconnect_client_by_button)
		self.commUi.connectBtn.clicked.connect(self.connect_to_the_server)
		self.commUi.connectBtn.clicked.connect(self.disconnect_the_server)
		self.commUi.CSTree.itemClicked.connect(self.refresh_connect_button_and_address_label)
		self.commUi.overViewTree.itemClicked.connect(self.calculate_the_time_difference)
		self.commUi.overViewTree.itemClicked.connect(self.showMessage)
		self.commUi.hexBtn.clicked.connect(self.show_hex_and_asc_edit)
		self.commUi.ascBtn.clicked.connect(self.show_hex_and_asc_edit)
		self.commUi.sendBtn.clicked.connect(self.send_data)
		self.commUi.sendDataHexEdit.textChanged.connect(self.input_data)
		self.commUi.sendDataAscEdit.textChanged.connect(self.input_data)
		self.commUi.clearBtn.clicked.connect(self.clear_data)

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
			self.server_pool.append([SocketTcp.MyServer(host="", port=self.portSB.value()),
			                         self.local_ip, self.portSB.value()])
		# self.logger.debug(self.server_pool)
		except OSError as e:
			if e.errno == 48:
				self.ret = self.messageBox1.exec_()  # yes = 16384  cancel = 4194304
				self.logger.exception(e)
			else:
				self.logger.exception(e)
		else:
			# 服务器相关信号绑定
			self.bind_server_signals(self.server_pool[-1][0])

			self.server_top_pool.append(QTreeWidgetItem())
			self.server_top_pool[-1].setText(0, self.server_pool[-1][1])
			self.server_top_pool[-1].setText(1, str(self.server_pool[-1][2]))
			self.commUi.CSTree.addTopLevelItem(self.server_top_pool[-1])
			self.server_top_pool[-1].setExpanded(True)
			self.commUi.CSTree.clearSelection()
			self.server_top_pool[-1].setSelected(True)

			self.commUi.connectBtn.setChecked(True)
			self.top_count = self.root.childCount()
			self.server_pool[-1][0].server_No = self.server_count
			self.server_pool[-1].append(self.server_count)
			self.server_count += 1
			self.server_pool[-1][0].my_accept()
			self.server_top_pool[-1].setIcon(2, QIcon("./communication/images/happy.png"))

	def startListen(self):
		if self.commUi.serverBtn.isChecked():
			if self.commUi.connectBtn.isChecked():
				self.top_count = self.root.childCount()
				if self.top_count != 0:
					if self.commUi.CSTree.currentItem() is not None:
						self.commUi.connectBtn.setText("停止监听")
						self.current_index = self.commUi.CSTree.currentIndex().row()
						# self.logger.debug(self.current_index)
						# self.server_pool[self.current_index][0].server_signal.accepted_done.connect(self.add_client_to_server)
						# self.server_pool[self.current_index][0].server_No = self.current_index
						self.server_pool[self.current_index][0].my_accept()
						self.server_top_pool[self.current_index].setIcon(2, QIcon("./communication/images/happy.png"))
					else:
						self.commUi.connectBtn.setText("停止监听")
						# self.logger.debug(self.server_pool[-1])
						# self.server_pool[-1][0].server_signal.accepted_done.connect(self.add_client_to_server)
						# self.logger.debug(self.top_count)
						self.server_pool[-1][0].server_No = self.top_count - 1
						self.server_pool[-1][0].my_accept()
						self.server_top_pool[-1].setIcon(2, QIcon("./communication/images/happy.png"))
				else:
					self.messageBox3.exec_()

	def stop_listen_or_disconnect_client_by_button(self):
		if self.commUi.serverBtn.isChecked():
			if not self.commUi.connectBtn.isChecked():
				if self.commUi.CSTree.currentItem() is not None:  # top item是否被选中执行不同的操作
					if self.commUi.CSTree.currentItem().parent() is None:  # 判断当前选中的是不是top item
						self.commUi.connectBtn.setText("开始监听")
						self.current_index = self.commUi.CSTree.currentIndex().row()
						children = self.commUi.CSTree.currentItem().takeChildren()
						for i in children:
							del i
						# self.logger.debug(self.server_pool[self.top_count - 1][0])
						self.server_pool[self.current_index][0].stop_listen()
						self.server_top_pool[self.current_index].setIcon(2, QIcon("./communication/images/neutral.png"))
						del self.server_pool[self.current_index][0]
						self.logger.debug(self.server_pool)
						self.server_pool[self.current_index].insert(0, SocketTcp.MyServer(host="",
						                                                                  port=self.server_pool[
							                                                                  self.current_index][1]))
						self.server_pool[self.current_index][0].server_No = self.server_pool[self.current_index][-1]
						# self.logger.debug(self.server_pool)
						# self.logger.debug(self.server_pool[self.current_index][0].server_No)
						# 服务器相关信号绑定
						self.bind_server_signals(self.server_pool[self.current_index][0])
					# self.logger.debug(self.server_pool[self.current_index][0])
					else:
						# 断开客户端
						top_row = self.commUi.CSTree.indexFromItem(self.commUi.CSTree.currentItem().parent()).row()
						child_row = self.commUi.CSTree.indexFromItem(self.commUi.CSTree.currentItem()).row()
						self.server_pool[top_row][0].conn_pool[child_row][7].close()
				else:
					self.commUi.connectBtn.setText("开始监听")
					children = self.server_top_pool[-1].takeChildren()
					for i in children:
						del i
					self.server_pool[-1][0].stop_listen()
					self.server_top_pool[-1].setIcon(2, QIcon("./communication/images/neutral.png"))
					# self.logger.debug(self.server_pool[self.current_index][2])
					del self.server_pool[self.top_count - 1][0]

					self.server_pool[self.top_count - 1].insert(0, SocketTcp.MyServer(host="",
					                                                                  port=self.server_pool[-1][1]))
					self.server_pool[-1][0].server_No = self.server_pool[-1][-1]
					# 服务器相关信号绑定
					self.bind_server_signals(self.server_pool[self.top_count - 1][0])

	def delete_server_or_client(self):
		isDeleted = False
		self.top_count = self.root.childCount()
		if self.commUi.serverBtn.isChecked():  # 删除服务器
			# if len(self.server_top_pool) != 0:
			if self.top_count != 0:
				if self.commUi.CSTree.currentItem() is not None:
					if self.commUi.CSTree.currentItem().parent() is None:
						# current_index = self.server_top_pool.index(self.commUi.CSTree.currentItem())
						self.current_index = self.commUi.CSTree.currentIndex().row()
						self.server_top_pool.pop(self.current_index)
						self.server_pool[self.current_index][0].stop_listen()
						self.server_pool.pop(self.current_index)
						self.commUi.CSTree.takeTopLevelItem(self.current_index)
						self.logger.debug(self.server_pool)
						self.logger.debug(self.server_top_pool)
						isDeleted = True
					else:
						self.messageBox6.show()
				else:
					self.server_top_pool.pop()
					self.server_pool[-1][0].s.close()
					self.server_pool.pop()
					self.commUi.CSTree.takeTopLevelItem(self.top_count - 1)

				if isDeleted:
					self.top_count = self.root.childCount()
					if self.top_count != 0:
						self.commUi.CSTree.clearSelection()
						self.server_top_pool[self.top_count - 1].setSelected(True)
						self.commUi.connectBtn.setChecked(self.server_pool[self.top_count - 1][0].listening)
						if self.server_pool[self.top_count - 1][0].listening:
							self.commUi.connectBtn.setText("停止监听")
						else:
							self.commUi.connectBtn.setText("开始监听")
						self.commUi.serverIPLab2.setText(self.server_pool[self.top_count - 1][1])
						self.commUi.serverPortLab2.setText(str(self.server_pool[self.top_count - 1][2]))
						self.commUi.clientIPLab.setHidden(True)
						self.commUi.clientIPLab2.setHidden(True)
						self.commUi.clientPortLab.setHidden(True)
						self.commUi.clientPortLab2.setHidden(True)
					else:
						self.commUi.connectBtn.setChecked(False)
						self.commUi.connectBtn.setText("开始监听")
						self.commUi.serverIPLab.setHidden(True)
						self.commUi.serverPortLab.setHidden(True)
						self.commUi.serverIPLab2.setHidden(True)
						self.commUi.serverPortLab2.setHidden(True)
						self.commUi.clientIPLab.setHidden(True)
						self.commUi.clientIPLab2.setHidden(True)
						self.commUi.clientPortLab.setHidden(True)
						self.commUi.clientPortLab2.setHidden(True)
			else:
				self.messageBox2.show()
		else:  # 删除客户端
			# if len(self.client_item_pool) != 0:
			if self.top_count != 0:
				if self.commUi.CSTree.currentItem() is not None:
					# current_index = self.client_item_pool.index(self.commUi.CSTree.currentItem())
					self.current_index = self.commUi.CSTree.currentIndex().row()
					self.client_item_pool.pop(self.current_index)
					self.client_pool.pop(self.current_index)
					self.commUi.CSTree.takeTopLevelItem(self.current_index)
				# self.logger.debug(self.client_pool)
				# self.logger.debug(self.client_item_pool)
				else:
					# self.messageBox2.show()
					self.client_item_pool.pop()
					self.client_pool.pop()
					self.commUi.CSTree.takeTopLevelItem(self.top_count - 1)
				self.top_count = self.root.childCount()
				if self.top_count == 0:
					self.commUi.connectBtn.setChecked(False)
					self.commUi.connectBtn.setText("连接")
			else:
				self.messageBox2.show()

	def add_client_to_server(self, l):

		# l为二维列表:[[服务器监听状态, 服务器编号, 线程名, 服务器IP, 服务器端口号, 客户端IP, 客户端端口号, 客户端连接, 客户端编号, 客户端连接状态], [], []...]
		# self.logger.debug(l)
		print("accept已完成。。。")
		child_item = QTreeWidgetItem()
		child_item.setTextAlignment(0, 1)
		child_item.setText(0, l[-1][5] + "[%d]" % l[-1][6])
		for i in range(len(self.server_pool)):
			if self.server_pool[i][-1] == l[-1][1]:
				self.server_top_pool[i].addChild(child_item)
				break

	def disconnect_client_by_defSignal(self, l):
		server_index = -1
		self.logger.debug(l)
		self.top_count = self.commUi.CSTree.topLevelItemCount()
		for ii in range(len(self.server_pool)):
			if self.server_pool[ii][-1] == l[-1]:
				server_index = ii
		if server_index != -1:  # server_index为-1时表示服务器已被删除，删除客户端的操作将不被执行
			self.logger.debug(self.server_pool)
			self.logger.debug(self.server_pool[server_index][0].conn_pool)
			if l[3]:  # listening
				if len(self.server_pool[server_index][0].conn_pool):
					for i in range(len(self.server_pool[server_index][0].conn_pool)):
						if self.server_pool[server_index][0].conn_pool[i][8] == l[2]:
							self.server_top_pool[server_index].takeChild(i)
							self.server_pool[server_index][0].conn_pool.pop(i)
							self.isClientDisconnected = True
							break
				child_count = self.server_top_pool[server_index].childCount()
				if child_count != 0:
					self.commUi.CSTree.clearSelection()
					self.server_top_pool[server_index].child(child_count - 1).setSelected(True)

					self.commUi.connectBtn.setChecked(True)
					self.commUi.connectBtn.setText("断开")
					self.commUi.serverIPLab2.setText(self.server_pool[server_index][1])
					self.commUi.serverPortLab2.setText(str(self.server_pool[server_index][2]))
					self.commUi.clientIPLab2.setText(self.server_pool[server_index][0].conn_pool[-1][5])
					self.commUi.clientPortLab2.setText(str(self.server_pool[server_index][0].conn_pool[-1][6]))
					self.commUi.clientIPLab.setHidden(False)
					self.commUi.clientIPLab2.setHidden(False)
					self.commUi.clientPortLab.setHidden(False)
					self.commUi.clientPortLab2.setHidden(False)
				else:
					self.commUi.connectBtn.setChecked(True)
					self.commUi.connectBtn.setText("停止监听")
					self.commUi.CSTree.clearSelection()
					self.server_top_pool[server_index].setSelected(True)
					self.commUi.serverIPLab2.setText(self.server_pool[server_index][1])
					self.commUi.serverPortLab2.setText(str(self.server_pool[server_index][2]))
					self.commUi.clientIPLab.setHidden(True)
					self.commUi.clientIPLab2.setHidden(True)
					self.commUi.clientPortLab.setHidden(True)
					self.commUi.clientPortLab2.setHidden(True)

	# self.logger.debug(self.server_pool[l[1]][0].conn_pool)

	def add_client(self):
		# 添加客户端，在list中显示
		if self.serverHostEdit.text() == "...":
			self.serverHostEdit.setText(self.local_ip)
		self.client_pool.append(
			[SocketTcp.MyClient(server_ip=self.serverHostEdit.text(), server_port=self.serverPortSB.value()),
			 self.serverHostEdit.text(), self.serverPortSB.value()])
		self.bind_client_signals(self.client_pool[-1][0])
		# self.logger.debug(self.client_pool)
		self.client_item_pool.append(QTreeWidgetItem())
		self.client_item_pool[-1].setText(0, self.client_pool[-1][1])
		self.client_item_pool[-1].setText(1, str(self.client_pool[-1][2]))
		self.commUi.CSTree.addTopLevelItem(self.client_item_pool[-1])
		self.commUi.CSTree.clearSelection()
		self.client_item_pool[-1].setSelected(True)
		self.commUi.connectBtn.setEnabled(True)

		self.commUi.connectBtn.setText("连接")
		self.commUi.serverIPLab2.setText(self.client_pool[-1][1])
		self.commUi.serverPortLab2.setText(str(self.client_pool[-1][2]))
		self.commUi.serverIPLab.setHidden(False)
		self.commUi.serverIPLab2.setHidden(False)
		self.commUi.serverPortLab.setHidden(False)
		self.commUi.serverPortLab2.setHidden(False)
		self.commUi.clientIPLab.setHidden(True)
		self.commUi.clientIPLab2.setHidden(True)
		self.commUi.clientPortLab.setHidden(True)
		self.commUi.clientPortLab2.setHidden(True)

	def connect_to_the_server(self):
		if self.commUi.clientBtn.isChecked():
			if self.commUi.connectBtn.isChecked():
				current_item = self.commUi.CSTree.currentItem()
				if current_item is not None:
					current_row = self.commUi.CSTree.indexFromItem(current_item).row()
					self.client_pool[current_row][0].client_No = current_row
					self.client_pool[current_row][0].client_connect()
				else:
					self.client_pool[-1][0].client_No = self.commUi.CSTree.topLevelItemCount() - 1
					self.client_pool[-1][0].client_connect()

	def disconnect_the_server(self):
		if self.commUi.clientBtn.isChecked():
			if not self.commUi.connectBtn.isChecked():
				current_item = self.commUi.CSTree.currentItem()
				if current_item is not None:
					current_row = self.commUi.CSTree.indexFromItem(current_item).row()
					self.client_pool[current_row][0].c.close()
					self.client_pool[current_row][0].client_signal.conn_closed_done.emit(
						[self.client_pool[-1][0].client_No,
						 "--", "--",
						 self.client_pool[-1][0].server_ip,
						 self.client_pool[-1][0].server_port, 0],
						"conn_closed_done")
					self.client_pool[current_row][0] = SocketTcp.MyClient(self.client_pool[current_row][1],
					                                                      self.client_pool[current_row][2])
					self.client_pool[current_row][0].client_No = current_row
					self.bind_client_signals(self.client_pool[current_row][0])
				else:
					self.client_pool[-1][0].c.close()
					self.client_pool[-1][0].client_signal.conn_closed_done.emit([self.client_pool[-1][0].client_No,
					                                                             "--", "--",
					                                                             self.client_pool[-1][0].server_ip,
					                                                             self.client_pool[-1][0].server_port,
					                                                             0],
					                                                            "conn_closed_done")
					self.client_pool[-1][0] = SocketTcp.MyClient(self.client_pool[-1][1],
					                                             self.client_pool[-1][2])
					self.client_pool[-1][0].client_No = self.commUi.CSTree.topLevelItemCount() - 1
					self.bind_client_signals(self.client_pool[-1][0])

	def create_my_client(self, index, client_No):
		self.client_pool[index][0].client_signal.conn_closed_done.emit([self.client_pool[index][0].client_No,
		                                                             "--", "--",
		                                                             self.client_pool[index][0].server_ip,
		                                                             self.client_pool[index][0].server_port,
		                                                             0],
		                                                            "conn_closed_done")
		self.client_pool[index][0] = SocketTcp.MyClient(self.client_pool[index][1],
		                                             self.client_pool[index][2])
		self.client_pool[index][0].client_No = client_No
		self.bind_client_signals(self.client_pool[index][0])

	def refresh_CSTree_interface(self):
		self.sen = self.sender()
		if self.sen.objectName() == "serverBtn":
			if not self.in_sever_interface:  # 用于判断只有当两个切换时才能执行，如果只点击按钮不切换的话不执行下面代码
				self.commUi.connectBtn.setChecked(False)
				self.commUi.connectBtn.setText("开始监听")
				self.commUi.CSTree.setHeaderLabels(["服务器IP", "监听端口", "监听中"])
				for _ in range(0, len(self.client_item_pool)):
					self.commUi.CSTree.takeTopLevelItem(0)
				if len(self.server_top_pool) != 0:
					self.commUi.CSTree.addTopLevelItems(self.server_top_pool)

				self.commUi.serverIPLab.setHidden(True)
				self.commUi.serverPortLab.setHidden(True)
				self.commUi.serverIPLab2.setHidden(True)
				self.commUi.serverPortLab2.setHidden(True)
				self.commUi.clientIPLab.setHidden(True)
				self.commUi.clientIPLab2.setHidden(True)
				self.commUi.clientPortLab.setHidden(True)
				self.commUi.clientPortLab2.setHidden(True)
				self.commUi.connectBtn.setEnabled(False)

				self.in_client_interface = False
				self.in_sever_interface = True

		if self.sen.objectName() == "clientBtn":
			if not self.in_client_interface:  # 用于判断只有当两个切换时才能执行，如果只点击按钮不切换的话不执行下面代码
				self.commUi.connectBtn.setChecked(False)
				self.commUi.connectBtn.setText("连接")
				self.commUi.CSTree.setHeaderLabels(["对方IP", "对方端口", "连接状态"])
				for _ in range(0, len(self.server_top_pool)):
					self.commUi.CSTree.takeTopLevelItem(0)
				if len(self.client_item_pool) != 0:
					self.commUi.CSTree.addTopLevelItems(self.client_item_pool)

				self.commUi.serverIPLab.setHidden(True)
				self.commUi.serverPortLab.setHidden(True)
				self.commUi.serverIPLab2.setHidden(True)
				self.commUi.serverPortLab2.setHidden(True)
				self.commUi.clientIPLab.setHidden(True)
				self.commUi.clientIPLab2.setHidden(True)
				self.commUi.clientPortLab.setHidden(True)
				self.commUi.clientPortLab2.setHidden(True)
				self.commUi.connectBtn.setEnabled(False)

				self.in_sever_interface = False
				self.in_client_interface = True

	def refresh_connect_button_and_address_label(self, item: QTreeWidgetItem, column):
		self.commUi.connectBtn.setEnabled(True)  # 切换client和Server时会将连接按钮设置为disable，点击top item时设置为enable
		if self.commUi.serverBtn.isChecked():  # 当CSTress显示Server时
			new_index = self.commUi.CSTree.indexFromItem(item).row()
			if item.parent() is None:
				# 设置connect button的状态
				if self.server_pool[new_index][0].listening:
					self.commUi.connectBtn.setChecked(True)
					self.commUi.connectBtn.setText("停止监听")
				else:
					self.commUi.connectBtn.setChecked(False)
					self.commUi.connectBtn.setText("开始监听")
				# 设置address的显示内容
				self.commUi.serverIPLab2.setText(self.server_pool[new_index][1])
				self.commUi.serverPortLab2.setText(str(self.server_pool[new_index][2]))
				self.commUi.serverIPLab.setHidden(False)
				self.commUi.serverPortLab.setHidden(False)
				self.commUi.serverIPLab2.setHidden(False)
				self.commUi.serverPortLab2.setHidden(False)
				self.commUi.clientIPLab.setHidden(True)
				self.commUi.clientIPLab2.setHidden(True)
				self.commUi.clientPortLab.setHidden(True)
				self.commUi.clientPortLab2.setHidden(True)
			else:
				parent_index = self.commUi.CSTree.indexFromItem(item.parent()).row()
				self.commUi.connectBtn.setChecked(True)
				self.commUi.connectBtn.setText("断开")
				self.commUi.serverIPLab2.setText(self.server_pool[parent_index][1])
				self.commUi.serverPortLab2.setText(str(self.server_pool[parent_index][2]))
				self.commUi.clientIPLab2.setText(self.server_pool[parent_index][0].conn_pool[new_index][5])
				self.commUi.clientPortLab2.setText(str(self.server_pool[parent_index][0].conn_pool[new_index][6]))
				self.commUi.serverIPLab.setHidden(False)
				self.commUi.serverPortLab.setHidden(False)
				self.commUi.serverIPLab2.setHidden(False)
				self.commUi.serverPortLab2.setHidden(False)
				self.commUi.clientIPLab.setHidden(False)
				self.commUi.clientIPLab2.setHidden(False)
				self.commUi.clientPortLab.setHidden(False)
				self.commUi.clientPortLab2.setHidden(False)
		else:
			current_row = self.commUi.CSTree.indexFromItem(self.commUi.CSTree.currentItem()).row()
			info = self.client_pool[current_row][0].info
			if info[-1] == 1 or info[-1] == -1:  # 判断客户端当前连接状态，1表正常连接，-1表示连接出错，0表示客户端未进行连接操作
				if info[-1] == 1:
					self.commUi.connectBtn.setText("断开")
				else:
					self.commUi.connectBtn.setText("连接")
				self.commUi.serverIPLab2.setText(info[3])
				self.commUi.serverPortLab2.setText(str(info[4]))
				self.commUi.clientIPLab2.setText(info[1])
				self.commUi.clientPortLab2.setText(str(info[2]))
				self.commUi.serverIPLab.setHidden(False)
				self.commUi.serverPortLab.setHidden(False)
				self.commUi.serverIPLab2.setHidden(False)
				self.commUi.serverPortLab2.setHidden(False)
				self.commUi.clientIPLab.setHidden(False)
				self.commUi.clientIPLab2.setHidden(False)
				self.commUi.clientPortLab.setHidden(False)
				self.commUi.clientPortLab2.setHidden(False)
			else:
				self.commUi.connectBtn.setText("连接")
				self.commUi.serverIPLab2.setText(info[3])
				self.commUi.serverPortLab2.setText(str(info[4]))
				self.commUi.serverIPLab.setHidden(False)
				self.commUi.serverPortLab.setHidden(False)
				self.commUi.serverIPLab2.setHidden(False)
				self.commUi.serverPortLab2.setHidden(False)
				self.commUi.clientIPLab.setHidden(True)
				self.commUi.clientIPLab2.setHidden(True)
				self.commUi.clientPortLab.setHidden(True)
				self.commUi.clientPortLab2.setHidden(True)

	def auto_set_connect_button_and_address_label_1(self):
		"""通过listened_done信号执行改槽函数"""
		# self.commUi.connectBtn.setChecked(True)
		self.commUi.connectBtn.setText("停止监听")
		self.commUi.serverIPLab2.setText(self.server_pool[-1][1])
		self.commUi.serverPortLab2.setText(str(self.server_pool[-1][2]))
		self.commUi.serverIPLab.setHidden(False)
		self.commUi.serverIPLab2.setHidden(False)
		self.commUi.serverPortLab.setHidden(False)
		self.commUi.serverPortLab2.setHidden(False)
		self.commUi.clientIPLab.setHidden(True)
		self.commUi.clientIPLab2.setHidden(True)
		self.commUi.clientPortLab.setHidden(True)
		self.commUi.clientPortLab2.setHidden(True)

	def auto_set_connect_button_and_address_label_2(self, info, name):
		# info = [0self.client_No, 1self.client_ip, 2self.client_port, 3self.server_ip, 4self.server_port]
		if info[-1] == 0:
			self.commUi.connectBtn.setChecked(False)
			self.commUi.connectBtn.setText("连接")
			self.commUi.clientIPLab.setHidden(True)
			self.commUi.clientIPLab2.setHidden(True)
			self.commUi.clientPortLab.setHidden(True)
			self.commUi.clientPortLab2.setHidden(True)
		if info[-1] == 1 or info[-1] == -1:
			if info[-1] == 1:
				self.commUi.connectBtn.setChecked(True)
				self.commUi.connectBtn.setText("断开")
			if info[-1] == -1:
				self.commUi.connectBtn.setChecked(False)
				self.commUi.connectBtn.setText("连接")
			self.commUi.clientIPLab.setHidden(False)
			self.commUi.clientIPLab2.setHidden(False)
			self.commUi.clientPortLab.setHidden(False)
			self.commUi.clientPortLab2.setHidden(False)

		self.commUi.serverIPLab2.setText(info[3])
		self.commUi.serverPortLab2.setText(str(info[4]))
		self.commUi.clientIPLab2.setText(info[1])
		self.commUi.clientPortLab2.setText(str(info[2]))
		self.commUi.serverIPLab.setHidden(False)
		self.commUi.serverPortLab.setHidden(False)
		self.commUi.serverIPLab2.setHidden(False)
		self.commUi.serverPortLab2.setHidden(False)

	def bind_server_signals(self, s: SocketTcp.MyServer):
		s.server_signal.conn_closed_done.connect(self.disconnect_client_by_defSignal)
		s.server_signal.listened_done.connect(self.auto_set_connect_button_and_address_label_1)
		s.server_signal.accepted_done.connect(self.add_client_to_server)
		s.server_signal.receive_data_done.connect(self.send_receive_data)
		s.server_signal.send_data_done.connect(self.send_receive_data)

	def bind_client_signals(self, c: SocketTcp.MyClient):
		c.client_signal.connect_done.connect(self.auto_set_connect_button_and_address_label_2)
		c.client_signal.connect_error.connect(self.auto_set_connect_button_and_address_label_2)
		c.client_signal.conn_closed_done.connect(self.auto_set_connect_button_and_address_label_2)

	def send_receive_data(self, info: list, name: str):
		# info = [0info_No, 1ts, 2server_ip, 3server_port, 4server_index, 5client_ip, 6client_port,
		#                                               7client_index, 8len(recv_data), 9recv_data]
		for i in range(len(self.server_pool)):
			if self.server_pool[i][-1] == info[2]:
				info[2] = i  # 当前服务器在server_pool列表中的索引
				break
		info.insert(0, self.info_No)
		# self.logger.debug(info)
		self.info_pool.append(info)
		item = QTreeWidgetItem()
		item.setCheckState(0, False)
		item.setText(0, str(info[0]))
		item.setText(1, str(info[1]))
		item.setText(4, str(info[8]))
		if name == "receive_data_done":
			item.setText(2, info[5])
			item.setText(3, info[2])
			item.setText(5, "%d to %d" % (info[6], info[3]))
		elif name == "send_data_done":
			item.setText(2, info[2])
			item.setText(3, info[5])
			item.setText(5, "%d to %d" % (info[3], info[6]))
		self.commUi.overViewTree.addTopLevelItem(item)
		self.commUi.overViewTree.clearSelection()
		item.setSelected(True)
		self.info_No += 1

		data_h = self.info_pool[-1][-1].hex()
		self.commUi.receiveDataHexEdit.clear()
		self.commUi.receiveDataHexEdit.setText(data_h)
		data = ""
		for i in self.info_pool[-1][-1]:
			try:
				data_a = i.decode("utf-8")
			except Exception as e:
				data += "?"
			# self.logger.exception(e)
			else:
				data += data_a
		self.commUi.receiveDataAscEdit.clear()
		self.commUi.receiveDataAscEdit.setText(data)
		self.commUi.receiveDataAscEdit.setText(self.convert_hex_to_ASCII(self.info_pool[-1][-1], True))

	def showMessage(self, item, c):
		current_row = self.commUi.overViewTree.indexFromItem(item).row()
		data_h = self.info_pool[current_row][-1].hex()
		self.commUi.receiveDataHexEdit.clear()
		self.commUi.receiveDataHexEdit.setText(data_h)
		try:
			data_a = self.info_pool[current_row][-1].decode("utf-8")
		# self.logger.debug(data_a)
		except Exception as e:
			self.commUi.receiveDataAscEdit.clear()
			self.commUi.receiveDataAscEdit.setText("?")
			self.logger.exception(e)
		else:
			self.commUi.receiveDataAscEdit.clear()
			self.commUi.receiveDataAscEdit.setText(data_a)

	def show_hex_and_asc_edit(self):
		sd = self.sender()
		if not self.commUi.hexBtn.isChecked() and not self.commUi.ascBtn.isChecked():
			sd.setChecked(True)
		if self.commUi.hexBtn.isChecked():
			self.commUi.receiveDataHexEdit.setHidden(False)
			self.commUi.sendDataHexEdit.setHidden(False)
		else:
			self.commUi.receiveDataHexEdit.setHidden(True)
			self.commUi.sendDataHexEdit.setHidden(True)
		if self.commUi.ascBtn.isChecked():
			self.commUi.receiveDataAscEdit.setHidden(False)
			self.commUi.sendDataAscEdit.setHidden(False)
		else:
			self.commUi.receiveDataAscEdit.setHidden(True)
			self.commUi.sendDataAscEdit.setHidden(True)

	def send_data(self):
		self.commUi.sendBtn.setDisabled(True)
		if not len(self.commUi.sendDataHexEdit.toPlainText()) % 2:
			# data = self.commUi.sendDataHexEdit.toPlainText().encode("utf-8")
			data = bytes.fromhex(self.commUi.sendDataHexEdit.toPlainText())
			# self.logger.debug(data)
			self.top_count = self.commUi.CSTree.topLevelItemCount()
			if self.top_count != 0:
				if self.commUi.CSTree.currentItem() is not None:
					if self.commUi.CSTree.currentItem().parent() is not None:
						top_row = self.commUi.CSTree.indexFromItem(self.commUi.CSTree.currentItem().parent()).row()
						child_row = self.commUi.CSTree.indexFromItem(self.commUi.CSTree.currentItem()).row()
						self.server_pool[top_row][0].conn_pool[child_row][7].sendall(data)

						# info = [0info_No, 1ts, 2server_ip, 3server_port, 4server_index, 5client_ip, 6client_port,
						#                                               7client_index, 8len(recv_data), 9recv_data]

						def send_date_handle():
							send_count = 0
							while send_count < self.commUi.frequenceSB.value():
								for i in range(len(self.server_pool)):
									if self.server_pool[top_row][0].conn_pool[child_row][1] == \
											self.server_pool[top_row][-1]:
										sever_index = i
										break
								info = [time.time(), self.server_pool[top_row][0].conn_pool[child_row][3],
								        self.server_pool[top_row][0].conn_pool[child_row][4], sever_index,
								        self.server_pool[top_row][0].conn_pool[child_row][5],
								        self.server_pool[top_row][0].conn_pool[child_row][6],
								        self.server_pool[top_row][0].conn_pool[child_row][8], len(data), data]
								# self.logger.debug(info)
								self.server_pool[top_row][0].server_signal.send_data_done.emit(info, "send_data_done")
								send_count += 1
							self.commUi.sendBtn.setDisabled(False)

						self.t = threading.Thread(target=send_date_handle)
						self.t.start()
					else:
						self.commUi.sendBtn.setDisabled(False)
						self.messageBox4.show()
				else:
					self.commUi.sendBtn.setDisabled(False)
					self.messageBox4.show()
			else:
				self.commUi.sendBtn.setDisabled(False)
				self.messageBox4.show()
		else:
			self.commUi.sendBtn.setDisabled(False)
			self.messageBox8.setText("请输入正确的字节数据！当前字符数%d个！" % len(self.commUi.sendDataHexEdit.toPlainText()))
			self.messageBox8.exec_()

	def input_data(self):
		sd: QTextEdit
		sd = self.sender()
		if sd.objectName() == "sendDataHexEdit" and sd == QApplication.focusWidget():
			if len(sd.toPlainText()) % 2 == 0:
				data = self.commUi.sendDataHexEdit.toPlainText().encode("utf-8")
				self.commUi.sendDataAscEdit.setText(self.convert_hex_to_ASCII(data, False))
		# else:

		if sd.objectName() == "sendDataAscEdit" and sd == QApplication.focusWidget():
			data_s = sd.toPlainText().encode("utf-8").hex()
			self.commUi.sendDataHexEdit.setText(data_s)

	def convert_hex_to_ASCII(self, b_ah: bytes, b):
		"""
		将bytes字节流的数据转换为ASC码，无法转换的字节显示"?"
		比如：当b=True时，b"12\88"，转换为"12?"
			 当b=False时，b"3131\88"，转换为"12?"
		:param b_ah: 字节流
		:param b: bool，True时为ASC表示的字节流，False时为16进制表示的字节流
		:return: ASC码
		"""
		s_a = ""
		if b:
			s = b_ah.hex()
		else:
			s = b_ah.decode(encoding="utf-8")
		if len(s) % 2 == 0:
			for i in range(int(len(s) / 2)):
				b1 = bytes.fromhex(s[i * 2:i * 2 + 2])
				try:
					s1 = b1.decode("utf-8")
				except UnicodeDecodeError as e:
					s_a = s_a + "?"
				else:
					s_a = s_a + s1
		else:
			s_a = ""
		return s_a

	def clear_data(self):
		self.messageBox7.setText("确定要清除%d条通信数据吗？" % len(self.info_pool))
		ret = self.messageBox7.exec_()
		if ret == 16384:
			self.commUi.overViewTree.clear()
			self.commUi.receiveDataHexEdit.clear()
			self.commUi.receiveDataAscEdit.clear()
			self.info_No = 1

	def calculate_the_time_difference(self, item: QTreeWidgetItem, column):
		check_state = item.checkState(0)
		current_row = self.commUi.overViewTree.indexFromItem(item).row()
		# self.logger.debug(current_row)
		if check_state == 2:
			if len(self.checked_pool) < 2:
				if len(self.checked_pool) == 0:
					self.checked_pool.append([item, current_row, check_state])
				else:
					if current_row < self.checked_pool[0][1]:
						self.checked_pool.insert(0, [item, current_row, check_state])
					if current_row > self.checked_pool[0][1]:
						self.checked_pool.append([item, current_row, check_state])
			else:
				if current_row < self.checked_pool[0][1]:
					self.checked_pool[0][0].setCheckState(0, False)
					self.checked_pool[0] = [item, current_row, check_state]
				if current_row > self.checked_pool[1][1]:
					self.checked_pool[1][0].setCheckState(0, False)
					self.checked_pool[1] = [item, current_row, check_state]
				if self.checked_pool[0][1] < current_row < self.checked_pool[1][1]:
					self.checked_pool[1][0].setCheckState(0, False)
					self.checked_pool[1] = [item, current_row, check_state]
		# self.logger.debug(self.checked_pool)
		else:
			if len(self.checked_pool) != 0:
				for i in self.checked_pool:
					if i[1] == current_row:
						self.checked_pool.remove(i)
		if len(self.checked_pool) == 2:
			subtrahend = self.info_pool[self.checked_pool[0][1]][1]
			minuend = self.info_pool[self.checked_pool[1][1]][1]
			difference = (minuend - subtrahend) * 1000
			print(difference)
			self.commUi.differenceLab.setText("时间差：{0:.3f}ms".format(difference))


# def closeEvent(self, a0: QCloseEvent):


class KeyPressEster(QObject):
	def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
		if a1.type() == QEvent.KeyPress:
			if a1.text() in string.hexdigits:
				# a0.setText(a1.text())
				a0.textCursor().insertText(a1.text())
			if a1.key() == 16777219:  # 退格键
				a0.textCursor().deletePreviousChar()
			return True
		else:
			return QObject.eventFilter(self, a0, a1)


class Signals(QObject):
	a: pyqtBoundSignal
	start_lis = pyqtSignal(str)


if __name__ == "__main__":
	logging.config.fileConfig("./log/logging.conf")
	app = QApplication(argv)
	win = CommWidgetUi()
	win.show()
	exit(app.exec_())
