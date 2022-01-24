from PyQt5.QtCore import pyqtSignal, pyqtBoundSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QErrorMessage, QWidget, QApplication, QTableWidgetItem, QTableWidget, \
	QMessageBox, QTableWidgetSelectionRange, QMenu, QAction, QLabel, QProgressBar, QPushButton, QFileDialog, QInputDialog, \
	QDateEdit, QComboBox
from PyQt5.QtCore import QObject, Qt, QPoint
import DatabaseOperation
import ExcelWrite
import sys
import pymysql
import time
import calendar
import TaxiUi
import logging
import logging.config
import threading
import random


class TaxiWidgetUi(QWidget):
	total_time = 0

	def __init__(self):
		super(TaxiWidgetUi, self).__init__()
		self.logger = logging.getLogger("applog")

		self.taxiUi = TaxiUi.Ui_Taxi()
		self.taxiUi.setupUi(self)
		self.setupUi()

	def setupUi(self):
		self.defSignal = Signals()

		# 设置上下文菜单
		self.taxiUi.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.taxiUi.tableWidget.customContextMenuRequested.connect(self.getContextMenu)

		# 给pageNumberEdit设置校验器，只能输入整数
		self.int_validator = QIntValidator(self)
		self.int_validator.setBottom(1)
		self.int_validator.setTop(999999)
		self.taxiUi.pageNumberEdit.setValidator(self.int_validator)

		# 初始化控件的状态
		self.taxiUi.previousBtn.setEnabled(False)
		self.taxiUi.pageNumberEdit.setEnabled(False)
		self.taxiUi.nextBtn.setEnabled(False)

		# 信号和槽的绑定
		self.taxiUi.refreshBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		self.taxiUi.previousBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		self.taxiUi.nextBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		self.taxiUi.pageNumberEdit.returnPressed.connect(lambda: self.getPageNumberAndStartWorkThread(s1=None))
		self.taxiUi.browseBtn.clicked.connect(self.showFileDialog)
		self.taxiUi.exportBtn.clicked.connect(self.excel_write)

		self.taxiUi.okButton.clicked.connect(self.update_db_data)
		self.taxiUi.saveBtn.clicked.connect(self.backup_db_data)
		self.taxiUi.addNameBtn.clicked.connect(self.insert_db_data)

		self.taxiUi.okButton.clicked.connect(lambda: self.showProgressBar(True, True, self.taxiUi.okButton))
		self.defSignal.update_data_done.connect(lambda: self.showProgressBar(False, True, self.taxiUi.okButton))
		self.taxiUi.saveBtn.clicked.connect(lambda: self.showProgressBar(True, False, self.taxiUi.saveBtn))
		self.defSignal.backup_data_done.connect(lambda: self.showProgressBar(False, False, self.taxiUi.saveBtn))

		self.defSignal.insert_data_done.connect(self.getPageNumberAndStartWorkThread)  # 表格中显示新添加的内容
		self.defSignal.delete_data_done.connect(self.getPageNumberAndStartWorkThread)
		self.defSignal.update_data_done.connect(self.getPageNumberAndStartWorkThread)
		self.defSignal.backup_data_done.connect(lambda: self.taxiUi.saveBtn.setEnabled(True))
		self.defSignal.conn_error.connect(lambda: self.showErrorMessage("数据库连接错误，请检查网络！"))  # 连接数据库错误时弹出错误提示框
		self.defSignal.conn_error.connect(lambda: self.buttonShow(self.taxiUi, 0))

	def startWorkThread(self, start_line=1, end_line=22):
		# 在读取数据前禁用翻页键和刷新键
		self.taxiUi.previousBtn.setEnabled(False)
		self.taxiUi.pageNumberEdit.setEnabled(False)
		self.taxiUi.nextBtn.setEnabled(False)
		self.taxiUi.refreshBtn.setEnabled(False)
		# 启动线程开始获取数据库数据
		self.work_thread1 = threading.Thread(target=self.get_db_data, args=(start_line, end_line))
		self.work_thread1.start()
		# 数据湖数据获取完成后发射信号执行表数据写入
		self.defSignal.get_data_done.connect(self.setTableWidgetItem)

	def get_db_data(self, start_line, end_line):
		try:
			t_stamp1 = time.time()
			conn, cursor = DatabaseOperation.connect_db()
			self.conn_time = (time.time() - t_stamp1) * 1000
		# self.logger.debug(f"登录服务器耗时{self.conn_time}ms")
		except pymysql.err.OperationalError as e:
			self.defSignal.conn_error.emit("conn_error")
			self.logger.exception(e)
		except Exception as e:
			self.logger.exception(e)
		else:
			try:
				self.max_id = DatabaseOperation.get_max_id(cursor)
				t_stamp2 = time.time()
				self.data = DatabaseOperation.get_contents_of_table(cursor, start_line, end_line)
				self.get_data_time = (time.time() - t_stamp2) * 1000
			# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
			except Exception as e:
				self.logger.exception(e)
			else:
				self.defSignal.get_data_done.emit("get_data_done")
			finally:
				DatabaseOperation.close(conn, cursor)
				self.get_total_time = (time.time() - t_stamp1) * 1000
				self.logger.debug(f"总耗时{self.get_total_time}ms")
				self.logger.debug("数据库获取数据完成！")

	def setTableWidgetItem(self):
		# 在状态显示读取数据所消耗时间，只显示3秒
		# self.ui.statusbar.showMessage("获取数据总耗时：{} ms".format(self.work_thread1.total_time))

		# 将数据库的数据写入到table widget，建议将用tr()，字符串国际化
		index = 0
		# self.logger.debug(self.data)
		for dic in self.data:
			self.taxiUi.tableWidget.setItem(index, 0, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(dic["name"]))))
			self.taxiUi.tableWidget.setItem(index, 1, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(dic["amount"]))))
			self.taxiUi.tableWidget.setItem(index, 2, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(dic["number"]))))
			index += 1
		if len(self.data) < 22:
			for index2 in range(index, 23):
				self.taxiUi.tableWidget.setItem(index2, 0, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(""))))
				self.taxiUi.tableWidget.setItem(index2, 1, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(""))))
		self.taxiUi.yeLabel.setText("页/共%d条" % self.max_id)
		# 数据读完后启用翻页键和刷新键self.ui.statusbar.showMessage
		self.buttonShow(self.taxiUi, self.max_id)

	def getPageNumberAndStartWorkThread(self, s1):
		"""
		1. 获取self.taxiUi.pageNumberEdit的值并且转换为整型，如果输入的值为空时会有错误弹窗；
		2. 如果输入的值可转换为整型则从数据库获取数据并显示在表中；
		"""
		try:
			pageNumber = int(self.taxiUi.pageNumberEdit.text())
		except ValueError as e:
			self.showErrorMessage("页码输入框内容不能为空！")
			self.logger.exception(e)
		else:
			# self.logger.debug(self.sender())
			# self.logger.debug(s1)
			s = self.sender().objectName()
			if s == self.taxiUi.previousBtn.objectName():
				self.startWorkThread((pageNumber - 2) * 22, (pageNumber - 1) * 22)
				self.taxiUi.pageNumberEdit.setText(str(pageNumber - 1))
			elif s == self.taxiUi.nextBtn.objectName():
				self.startWorkThread(pageNumber * 22, (pageNumber + 1) * 22 - 1)
				self.taxiUi.pageNumberEdit.setText(str(pageNumber + 1))
			elif s == self.taxiUi.refreshBtn.objectName() or s1 == "update_data_done" or s1 == "insert_data_done" \
					or s1 == "delete_data_done":
				self.startWorkThread((pageNumber - 1) * 22, pageNumber * 22)
			elif s == self.taxiUi.pageNumberEdit.objectName():
				self.startWorkThread((pageNumber - 1) * 22, pageNumber * 22)

	def buttonShow(self, taxi_ui, max_id):
		"""
		1. taxi ui界面的上下翻页，刷新按钮在未加载数据库数据时这个按钮需要设置为不可用
		2. 当页码输入框为空时其他按钮也要设置为无效
		3. 当前页页码为1时，上一页按钮要设置为不可用，页码为最大时下一页按钮要设置为不可用
		:param taxi_ui:
		:param max_id:数据库总行数
		"""
		self.taxiUi.okButton.setEnabled(True)
		if taxi_ui.pageNumberEdit.text() != '':
			taxi_ui.refreshBtn.setEnabled(True)
			taxi_ui.pageNumberEdit.setEnabled(True)
			if int(taxi_ui.pageNumberEdit.text()) == 1:
				taxi_ui.previousBtn.setEnabled(False)
			else:
				taxi_ui.previousBtn.setEnabled(True)
			if int(taxi_ui.pageNumberEdit.text()) == max_id // 22 + 1:
				taxi_ui.nextBtn.setEnabled(False)
			else:
				taxi_ui.nextBtn.setEnabled(True)
			if int(taxi_ui.pageNumberEdit.text()) > max_id // 22 + 1:
				taxi_ui.pageNumberEdit.setText(str(max_id // 22 + 1))

	def insert_db_data(self):
		def workThread1():
			try:
				t_stamp3 = time.time()
				conn, cursor = DatabaseOperation.connect_db()
				self.conn_time = (time.time() - t_stamp3) * 1000
			# self.logger.debug(f"登录服务器耗时{self.conn_time}ms")
			except pymysql.err.OperationalError as e:
				self.defSignal.conn_error.emit("conn_error")
				self.logger.exception(e)
			except Exception as e:
				self.logger.exception(e)
			else:
				try:
					t_stamp4 = time.time()
					DatabaseOperation.insert_data(cursor, conn, self.taxiUi.nameLineEdit.text(), "0")
					self.insert_data_time = (time.time() - t_stamp4) * 1000
					self.max_id = DatabaseOperation.get_max_id(cursor)
				# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
				except Exception as e:
					self.logger.exception(e)
				else:
					self.insert_total_time = (time.time() - t_stamp3) * 1000
					self.defSignal.insert_data_done.emit("insert_data_done")
					# 插入数据后更新总页面码label的内容，刷新表格内容的显示
					self.taxiUi.yeLabel.setText("页/共%d条" % self.max_id)
				finally:
					DatabaseOperation.close(conn, cursor)
					# self.logger.debug(f"总耗时{self.total_time}ms")
					self.logger.debug("数据库数据插入完成！")

		if self.taxiUi.nameLineEdit.text() == "":
			self.showErrorMessage("添加的姓名不能为空！")
		else:
			self.t5 = threading.Thread(target=workThread1)
			self.t5.start()

	def delete_db_data(self, table: QTableWidget):
		"""
		删除选中的行
		:return: None
		"""
		if self.isSelectedLines:
			self.ret1 = self.showMessageBox("删除数据库数据！", "确定永久删除被选中的数据？")
			if self.ret1 == 16384:
				# self.logger.debug(self.ret1)
				self.lineNumberList.reverse()
				self.logger.debug(self.lineNumberList)
				# for i in self.lineNumberList:
				# 	table.removeRow(i)
				id_list = list()
				for i in self.lineNumberList:
					id_list.append(str(self.data[i]["id"]))
				self.logger.debug(id_list)

				def workThread2():
					try:
						t_stamp1 = time.time()
						conn, cursor = DatabaseOperation.connect_db()
						self.conn_time = (time.time() - t_stamp1) * 1000
					# self.logger.debug(f"登录服务器耗时{self.conn_time}ms")
					except pymysql.err.OperationalError as e:
						self.defSignal.conn_error.emit("conn_error")
						self.logger.exception(e)
					except Exception as e:
						self.logger.exception(e)
					else:
						try:
							t_stamp2 = time.time()
							self.data = DatabaseOperation.delete_data(cursor, conn, id_list)
							self.get_data_time = (time.time() - t_stamp2) * 1000
							# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
							self.max_id = DatabaseOperation.get_max_id(cursor)
						except Exception as e:
							self.logger.exception(e)
						else:
							self.get_total_time = (time.time() - t_stamp1) * 1000
							self.defSignal.delete_data_done.emit("delete_data_done")
							# 插入数据后更新总页面码label的内容
							self.taxiUi.yeLabel.setText("页/共%d条" % self.max_id)
					finally:
						DatabaseOperation.close(conn, cursor)
						# self.logger.debug(f"总耗时{self.total_time}ms")
						self.logger.debug("数据库数据删除完成！")

				self.t6 = threading.Thread(target=workThread2)
				self.t6.start()
		else:
			self.ret2 = self.showMessageBox("请选中整行数据！", "想要选中整行吗？")
			# self.logger.debug(self.ret2)
			if self.ret2 == 16384:
				allRowNumber = self.removeSameItemFromList(self.selectedItemsRowNumberList)
				table.setRangeSelected(QTableWidgetSelectionRange(allRowNumber[0], 0,
				                                                  allRowNumber[-1], table.columnCount() - 1), True)

	def getContextMenu(self, mousePosition: QPoint):
		"""
		显示上下文菜单
		:param mousePosition: 鼠标当前位置, 由QTableWidget.customContextMenuRequested信号自动传入
		:return: None
		"""
		# self.mousePosition = mousePosition
		self.isSelectedLines, self.lineNumberList, self.selectedItemsRowNumberList = self.getLineNumber(
			self.taxiUi.tableWidget)
		globalMousePos = self.taxiUi.tableWidget.mapToGlobal(mousePosition)  # 坐标转换
		contextMenu = QMenu()

		removeLinesAction = QAction("删除")
		removeLinesAction.setObjectName("deleteBtn")
		contextMenu.addActions([removeLinesAction])
		contextMenu.move(globalMousePos)  # 将上下文菜单移动到鼠标位置

		removeLinesAction.triggered.connect(lambda: self.delete_db_data(self.taxiUi.tableWidget))
		contextMenu.exec_()

	def getLineNumber(self, table: QTableWidget):
		"""
		判断选中的是否为整行
		:param table: QTableView
		:return: False或者True，如果tableView选择的不是一个完整的行则返回False，如果选择的是完整的行则返回True；
				selectedLineNumberList:被选择完整行的行号组成的列表；
				rowNumberList: 所有被选中的item所在的行号列表
		"""
		selectedItem = table.selectedIndexes()
		rowNumberList = []  # 被选中的所有items的行号组成的列表
		columnNumberList = []  # 被选中的所有items的列号组成的列表
		for item in selectedItem:
			rowNumberList.append(item.row())
			columnNumberList.append(item.column())
			if (table.rowSpan(item.row(), item.column()) != 1) | \
					(table.columnSpan(item.row(), item.column()) != 1):
				for i1 in range(1, table.rowSpan(item.row(), item.column())):
					for i3 in range(item.column(), table.columnSpan(item.row(), item.column())):
						columnNumberList.append(i3)
						rowNumberList.append(item.row() + i1)
				for i2 in range(1, table.columnSpan(item.row(), item.column())):
					columnNumberList.append(item.column() + i2)
					rowNumberList.append(item.row())
		rowNumberList.sort(reverse=False)
		columnNumberList.sort(reverse=False)

		selectedLineNumberList = []
		if len(rowNumberList) % table.columnCount() == 0:
			for i in range(0, int(len(rowNumberList) / table.columnCount())):
				for rowNumber in rowNumberList[i * table.columnCount():table.columnCount() * (i + 1)]:
					if rowNumber != rowNumberList[i * table.columnCount()]:
						return False, [], rowNumberList
				selectedLineNumberList.append(rowNumberList[i * table.columnCount()])
		else:
			return False, [], rowNumberList
		return True, selectedLineNumberList, rowNumberList

	def removeSameItemFromList(self, originalList: list):
		"""
		剔除给定列表中重复的选项并返回
		:param originalList:
		:return:返回的列表中没有重复的元素,元素从小到大一次排列
		"""
		OriginalListCopy = originalList.copy()
		originalList.sort(reverse=False)
		noRepetitionItemList = []
		if len(originalList) != 1:
			for i in range(0, len(originalList) - 1):
				if i == 0:
					if originalList[i] == originalList[i + 1]:
						noRepetitionItemList.append(originalList[i + 1])
					else:
						noRepetitionItemList.append(originalList[i])
						noRepetitionItemList.append(originalList[i + 1])
				else:
					if originalList[i] != originalList[i + 1]:
						noRepetitionItemList.append(originalList[i + 1])
			return noRepetitionItemList
		else:
			noRepetitionItemList = originalList
			return noRepetitionItemList

	def random_number(self, l, lower_limit=350, upper_limit=400):
		"""
		生成和数据库总行数大小相同的随机数列表
		:param l: 生成随机数的总个数
		:param upper_limit: 随机上限值
		:param lower_limit: 随机下限值
		:return: numList随机数列表
		"""
		numList = list()
		for i in range(l):
			money = random.randint(lower_limit, upper_limit)
			numList.append(money)

		return numList

	def update_db_data(self):
		def workThread():
			# self.logger.debug(self.sender())
			# 计算数据并将数据写到数据过程okButton按钮时不能点的
			self.taxiUi.okButton.setEnabled(False)
			try:
				t_stamp3 = time.time()
				conn, cursor = DatabaseOperation.connect_db()
				self.conn_time = (time.time() - t_stamp3) * 1000
			# self.logger.debug(f"登录服务器耗时{self.conn_time}ms")
			except pymysql.err.OperationalError as e:
				self.defSignal.conn_error.emit("conn_error")
				self.logger.exception(e)
			except Exception as e:
				self.logger.exception(e)
			else:
				try:
					t_stamp4 = time.time()
					id_list1, id_list2, l1, l2 = DatabaseOperation.get_segment_data(cursor, 360, 400)
					num_List1 = self.random_number(l1, 361, int(self.taxiUi.maxValueSpinBox.text()))
					num_List2 = self.random_number(l2, int(self.taxiUi.minValueSpinBox.text()),
					                               int(self.taxiUi.maxValueSpinBox.text()))
					id_amount1 = list()
					for i, ii in zip(num_List1, id_list1):
						id_amount1.append((i, ii["id"]))
					id_amount2 = list()
					for i1, ii1 in zip(num_List2, id_list2):
						id_amount2.append((i1, ii1["id"]))
					# self.logger.debug(id_amount1)
					# self.logger.debug(id_amount2)
					DatabaseOperation.update_data(cursor, conn, id_amount1)
					DatabaseOperation.update_data(cursor, conn, id_amount2)
					self.update_data_time = (time.time() - t_stamp4) * 1000
				# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
				except Exception as e:
					self.logger.exception(e)
				else:
					self.defSignal.update_data_done.emit("update_data_done")
				finally:
					DatabaseOperation.close(conn, cursor)
					self.update_total_time = (time.time() - t_stamp3) * 1000
					self.logger.debug(f"更新数据总耗时{self.update_total_time}ms")
					self.logger.debug("数据库数据更新完成！")

		self.t4 = threading.Thread(target=workThread)
		self.t4.start()

	def backup_db_data(self):
		def workThread1():
			self.taxiUi.saveBtn.setEnabled(False)
			try:
				t_stamp3 = time.time()
				conn, cursor = DatabaseOperation.connect_db()
				self.conn_time = (time.time() - t_stamp3) * 1000
			# self.logger.debug(f"登录服务器耗时{self.conn_time}ms")
			except pymysql.err.OperationalError as e:
				self.defSignal.conn_error.emit("conn_error")
				self.logger.exception(e)
			except Exception as e:
				self.logger.exception(e)
			else:
				try:
					t_stamp4 = time.time()
					DatabaseOperation.backup_data(cursor, conn)
					self.insert_data_time = (time.time() - t_stamp4) * 1000
				# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
				except Exception as e:
					self.logger.exception(e)
				else:
					self.defSignal.backup_data_done.emit("backup_data_done")
				finally:
					DatabaseOperation.close(conn, cursor)
					self.backup_total_time = (time.time() - t_stamp3) * 1000
					# self.logger.debug(f"总耗时{self.total_time}ms")
					self.logger.debug("数据库数据备份完成！")

		self.ret3 = self.showMessageBox("数据保存到数据库，原有数据将会被覆盖！", "确定要保存吗？")
		if self.ret3 == 16384:
			self.taxiUi.saveBtn.setEnabled(False)
			self.t6 = threading.Thread(target=workThread1)
			self.t6.start()

	def excel_write(self):
		# dataDialog = QDialog()
		# dataDialog.resize(200, 80)
		# dataDialog.setWindowTitle("请选择月份")
		# dataDialog.setModal(True)
		#
		# dataInput = QComboBox(dataDialog)
		# dataInput.move(35, 10)
		# dataInput.addItems(["--请选择月份--", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
		# acceptBtn = QPushButton(dataDialog)
		# acceptBtn.setText("确定")
		# acceptBtn.move(110, 40)
		#
		# cancelBtn = QPushButton(dataDialog)
		# cancelBtn.setText("取消")
		# cancelBtn.move(20, 40)
		dataDialog = QInputDialog()
		dataDialog.setInputMode(QInputDialog.IntInput)
		dataDialog.setWindowTitle("输入月份")
		dataDialog.setCancelButtonText("取消")
		dataDialog.setOkButtonText("确定")
		dataDialog.setLabelText("请输入月份：")

		dataDialog.setIntRange(1, 12)
		dataDialog.setIntStep(1)
		dataDialog.setIntValue(1)
		if dataDialog.exec_():
			month = dataDialog.intValue()
			year = int(time.strftime("%Y"))
			# print(dataDialog.intValue())
			# print(time.strftime("%Y"))

			ca = calendar.Calendar()
			d_l = list()
			if month != 1:
				d_iter1 = ca.itermonthdays2(year, month - 1)
				d_iter2 = ca.itermonthdays2(year, month)
				print(d_iter1)
				for d in d_iter1:
					self.logger.debug(list(d).append(year))  # 返回None
					if d[0] > 20:
						print(d)
					d_l.append(list(d).append(year))
				print(d_l)
			else:
				d_iter3 = ca.itermonthdays2(year - 1, 12)
				for aa in d_iter3:
					print(aa)
				pass
			return
			try:
				t_stamp1 = time.time()
				conn, cursor = DatabaseOperation.connect_db()
				self.conn_time = (time.time() - t_stamp1) * 1000
			# self.logger.debug(f"登录服务器耗时{self.conn_time}ms")
			except pymysql.err.OperationalError as e:
				self.defSignal.conn_error.emit("conn_error")
				self.logger.exception(e)
			except Exception as e:
				self.logger.exception(e)
			else:
				try:
					self.max_id = DatabaseOperation.get_max_id(cursor)
					t_stamp2 = time.time()
					self.allData = DatabaseOperation.get_contents_of_table(cursor, 0, self.max_id)
					self.get_data_time = (time.time() - t_stamp2) * 1000
				# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
				except Exception as e:
					self.logger.exception(e)
				else:
					self.defSignal.get_all_date_done.emit("get_all_date_done")
				finally:
					DatabaseOperation.close(conn, cursor)
					self.get_total_time = (time.time() - t_stamp1) * 1000
					self.logger.debug(f"总耗时{self.get_total_time}ms")
					self.logger.debug("数据库获取数据完成！")
			# self.logger.debug(self.allData)
			# 获取时间数据写到Excel里
			datetime.datetime

			name_l = list()
			for dic in self.allData:
				n_l, total, minimum = ExcelWrite.random_number(dic["number"], dic["amount"], 100)
				self.logger.debug(n_l)
				if dic["name"] not in name_l:
					ExcelWrite.excel_write(dic["number"], n_l, dic["name"])
					name_l.append(dic["name"])
				else:
					# 重名时生成的文件名处理
					i = 1
					while 1:
						if dic["name"] + str(i) in name_l:
							i += 1
						else:
							ExcelWrite.excel_write(dic["number"], n_l, dic["name"] + str(i))
							name_l.append(dic["name"] + str(i))
							break

			print(123)

	def showSaveSuccessMessage(self):
		"""
		按下保存按钮后，数据保存成功显示提示信息
		:return:
		"""
		self.successLabel = QLabel("数据保存成功!", self)
		self.successLabel.setProperty("name", "successLabel")
		self.setStyleSheet("""
		QLabel[name="successLabel"]{
		color: red;
		}
		""")
		position = self.taxiUi.saveBtn.geometry()
		# self.logger.debug(position)
		self.successLabel.move(position.x() + 22, position.y() + position.height() - 10)
		self.successLabel.show()
		self.t7 = threading.Timer(2, self.successLabel.close)
		self.t7.start()

	def showErrorMessage(self, message: str):
		errorMessage = QErrorMessage()
		errorMessage.setModal(True)
		errorMessage.showMessage(message)
		result = errorMessage.exec_()
		return result

	def showMessageBox(self, text, infoText):
		"""
		:param text:消息窗口文本
		:param infoText: 消息窗口提示信息
		:return: 返回按钮的枚举值
		"""
		messageDialog = QMessageBox()
		messageDialog.setWindowModality(Qt.ApplicationModal)
		messageDialog.setText(text)
		messageDialog.setInformativeText(infoText)
		messageDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		result = messageDialog.exec_()
		return result

	def showProgressBar(self, b1: bool, b2: bool, btn: QPushButton):
		"""
		显示进度条
		:param b1: True表示显示进度条，False表示关闭进度条
		:param b2: True表示在元件的上方显示进度条，False表示在元件的下方显示进度条
		:param btn: 进度条依附的按钮
		"""
		if b1:
			self.progressBar = QProgressBar(self)
			self.progressBar.setRange(0, 0), self.taxiUi.okButton
			position = btn.geometry()
			# self.logger.debug(position)\
			if b2:
				self.progressBar.move(position.x() + 8, position.y() - 20)
			else:
				self.progressBar.move(position.x() + 8, position.y() + 20)
			self.progressBar.show()
		else:
			self.progressBar.close()
			del self.progressBar

	def showFileDialog(self):
		fileDialog = QFileDialog(None, "选择文件保存的位置",
		                         "/Users/qianshaoqing/Documents/Python/PythonProjects/OmronOfficeSystem/taxi_file")

		fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
		fileDialog.setOption(True, QFileDialog.ShowDirsOnly)

		if fileDialog.exec_():
			self.savePath = fileDialog.directory().path()
			self.logger.debug(self.savePath)


class Signals(QObject):
	get_data_done: pyqtBoundSignal
	conn_error: pyqtBoundSignal
	insert_data_done: pyqtBoundSignal
	delete_data_done: pyqtBoundSignal
	update_data_done: pyqtBoundSignal
	backup_data_done: pyqtBoundSignal
	get_all_date_done: pyqtBoundSignal
	get_data_done = pyqtSignal(str)
	conn_error = pyqtSignal(str)
	insert_data_done = pyqtSignal(str)
	delete_data_done = pyqtSignal(str)
	update_data_done = pyqtSignal(str)
	backup_data_done = pyqtSignal(str)
	get_all_date_done = pyqtSignal(str)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	logging.config.fileConfig("log/logging.conf")
	win = TaxiWidgetUi()
	win.show()
	sys.exit(app.exec_())
