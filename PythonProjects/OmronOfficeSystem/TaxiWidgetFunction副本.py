from PyQt5.QtCore import QThread, pyqtSignal, pyqtBoundSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QErrorMessage, QWidget, QApplication, QTableWidgetItem,QHBoxLayout
from PyQt5.QtCore import QObject
import DatabaseOperation
import sys
import pymysql
import time
import TaxiUi
import logging
import logging.config
import threading


class WorkTread(QThread):
	# 读取数据库数据的线程
	get_data_done: pyqtBoundSignal
	conn_error: pyqtBoundSignal
	get_data_done = pyqtSignal()
	conn_error = pyqtSignal()

	def __init__(self, start_line=1, end_line=22):
		super(WorkTread, self).__init__()
		self.logger = logging.getLogger("applogger")
		self.start_line = start_line
		self.end_line = end_line

	def run(self):
		try:
			t_stamp1 = time.time()
			conn, cursor = DatabaseOperation.connect_db()
			self.conn_time = (time.time() - t_stamp1) * 1000
			# self.logger.debug(f"登录服务器耗时{self.conn_time}ms")
		except pymysql.err.OperationalError as e:
			self.conn_error.emit()
			self.logger.exception(e)
		except Exception as e:
			self.logger.exception(e)
		else:
			try:
				self.max_id = DatabaseOperation.get_max_id(cursor)
				t_stamp2 = time.time()
				self.data = DatabaseOperation.get_contents_of_table(cursor, self.start_line, self.end_line)
				self.get_data_time = (time.time()-t_stamp2)*1000
				# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
			except Exception as e:
				self.logger.exception(e)
			else:
				self.total_time = (time.time() - t_stamp1) * 1000
				self.get_data_done.emit()
			finally:
				DatabaseOperation.close(conn, cursor)
				# self.logger.debug(f"总耗时{self.total_time}ms")
				self.logger.debug("数据库获取数据完成！")


class TaxiWidgetUi(QWidget):
	def __init__(self):
		super(TaxiWidgetUi, self).__init__()
		self.logger = logging.getLogger("applog")

		self.taxiUi = TaxiUi.Ui_Taxi()
		self.taxiUi.setupUi(self)

		self.setupUi()

	def setupUi(self):
		"""
		初始化self.taxiUi页面中的控件并将信号和槽绑定
		"""
		self.work_thread1 = WorkTread(1, 22)
		self.logger.debug(self.work_thread1)
		# 给pageNumberEdit设置校验器，只能输入整数
		self.int_validator = QIntValidator(self)
		self.int_validator.setBottom(1)
		self.int_validator.setTop(999999)
		self.taxiUi.pageNumberEdit.setValidator(self.int_validator)

		self.taxiUi.previousBtn.setEnabled(False)
		self.taxiUi.pageNumberEdit.setEnabled(False)
		self.taxiUi.nextBtn.setEnabled(False)

		self.taxiUi.refreshBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		self.taxiUi.previousBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		self.taxiUi.nextBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		self.taxiUi.pageNumberEdit.returnPressed.connect(self.getPageNumberAndStartWorkThread)

	def startWorkThread(self, start_line=1, end_line=22):
		# 在读取数据前禁用翻页键和刷新键
		self.taxiUi.previousBtn.setEnabled(False)
		self.taxiUi.pageNumberEdit.setEnabled(False)
		self.taxiUi.nextBtn.setEnabled(False)
		self.taxiUi.refreshBtn.setEnabled(False)
		# 启动线程开始获取数据库数据
		self.work_thread1 = WorkTread(start_line, end_line)
		self.logger.debug(self.work_thread1)
		self.work_thread1.start()
		# 连接数据库错误时弹出错误提示框
		self.work_thread1.conn_error.connect(lambda: self.showErrorMessage("数据库连接错误，请检查网络！"))
		# 数据湖数据获取完成后发射信号执行表数据写入
		self.work_thread1.get_data_done.connect(self.setTableWidgetItem)

	def setTableWidgetItem(self):
		# 在状态显示读取数据所消耗时间，只显示3秒
		# self.ui.statusbar.showMessage("获取数据总耗时：{} ms".format(self.work_thread1.total_time))

		# 将数据库的数据写入到table widget，建议将用tr()，字符串国际化
		index = 0
		for dic in self.work_thread1.data:
			self.taxiUi.tableWidget.setItem(index, 0, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(dic["name"]))))
			self.taxiUi.tableWidget.setItem(index, 1, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(dic["amount"]))))
			index += 1
		if len(self.work_thread1.data) < 22:
			for index2 in range(index, 23):
				self.taxiUi.tableWidget.setItem(index2, 0, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(""))))
				self.taxiUi.tableWidget.setItem(index2, 1, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(""))))
		self.taxiUi.yeLabel.setText("页/共%d条" % self.work_thread1.max_id)
		self.max_id = self.work_thread1.max_id
		# 数据读完后启用翻页键和刷新键self.ui.statusbar.showMessage
		self.previousAndNextButtonShow(self.taxiUi, self.work_thread1.max_id)

	def getPageNumberAndStartWorkThread(self):
		"""
		1. 获取self.taxiUi.pageNumberEdit的值并且转换为整型，如果输入的值为空时会有错误弹窗；
		2. 如果输入的值可转换为整型则从数据库获取数据并显示在表中；
		"""
		try:
			pageNumber = int(self.taxiUi.pageNumberEdit.text())
			print(pageNumber)
		except ValueError as e:
			self.showErrorMessage("页码输入框内容不能为空！")
			self.logger.exception(e)
		else:
			s = self.sender().objectName()
			if s == self.taxiUi.previousBtn.objectName():
				self.startWorkThread((pageNumber-2)*22+1, (pageNumber-1)*22)
				self.taxiUi.pageNumberEdit.setText(str(pageNumber-1))
			elif s == self.taxiUi.nextBtn.objectName():
				self.startWorkThread(pageNumber*22+1, (pageNumber+1)*22)
				self.taxiUi.pageNumberEdit.setText(str(pageNumber+1))
			elif s == self.taxiUi.refreshBtn.objectName():
				self.startWorkThread((pageNumber-1)*22+1, pageNumber*22)
			elif s == self.taxiUi.pageNumberEdit.objectName():
				self.startWorkThread((pageNumber-1)*22+1, pageNumber*22)

	def previousAndNextButtonShow(self, taxi_ui, max_id):
		"""
		1. taxi ui界面的上下翻页，刷新按钮在未加载数据库数据时这个按钮需要设置为不可用
		2. 当页码输入框为空时其他按钮也要设置为无效
		3. 当前页页码为1时，上一页按钮要设置为不可用，页码为最大时下一页按钮要设置为不可用
		:param taxi_ui:
		:param max_id:数据库总行数
		"""
		if taxi_ui.pageNumberEdit.text() != '':
			taxi_ui.refreshBtn.setEnabled(True)
			taxi_ui.pageNumberEdit.setEnabled(True)
			if int(taxi_ui.pageNumberEdit.text()) == 1:
				taxi_ui.previousBtn.setEnabled(False)
			else:
				taxi_ui.previousBtn.setEnabled(True)
			if int(taxi_ui.pageNumberEdit.text()) == max_id//22 + 1:
				taxi_ui.nextBtn.setEnabled(False)
			else:
				taxi_ui.nextBtn.setEnabled(True)
			if int(taxi_ui.pageNumberEdit.text()) > max_id//22+1:
				taxi_ui.pageNumberEdit.setText(str(max_id // 22 + 1))

	def showErrorMessage(self, message: str):
		errorMessage = QErrorMessage()
		errorMessage.setModal(True)
		errorMessage.showMessage(message)
		errorMessage.exec_()


# class Signals(QObject):
# 	get_data_done: pyqtBoundSignal
# 	get_data_done = pyqtSignal


if __name__ == "__main__":
	app = QApplication(sys.argv)
	logging.config.fileConfig("log/logging.conf")
	win = TaxiWidgetUi()
	win.show()
	sys.exit(app.exec_())





