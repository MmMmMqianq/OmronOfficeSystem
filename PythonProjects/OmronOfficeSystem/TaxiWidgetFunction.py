from PyQt5.QtCore import QThread, pyqtSignal, pyqtBoundSignal
from PyQt5.QtWidgets import QErrorMessage, QTableWidgetItem
from PyQt5.QtGui import QIntValidator
import DatabaseOperation
import pymysql
import time
import TaxiUi
import Ui
import logging


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
				self.get_data_time = (time.time() - t_stamp2) * 1000
			# self.logger.debug(f"从数据库获取一页数据耗时{self.get_data_time}ms")
			except Exception as e:
				self.logger.exception(e)
			else:
				self.total_time = (time.time() - t_stamp1) * 1000
				self.get_data_done.emit()
			finally:
				DatabaseOperation.close(conn, cursor)
			# self.logger.debug(f"总耗时{self.total_time}ms")
			# self.logger.debug("数据库获取数据完成！")


def taxiUiInitial(taxiUi: TaxiUi.Ui_Taxi, ui: Ui.Ui_MainWindow):
	"""
			初始化self.taxiUi页面中的控件并将信号和槽绑定
			"""
	# 给pageNumberEdit设置校验器，只能输入整数
	int_validator = QIntValidator()
	int_validator.setBottom(1)
	int_validator.setTop(999999)
	taxiUi.pageNumberEdit.setValidator(int_validator)

	taxiUi.previousBtn.setEnabled(False)
	taxiUi.pageNumberEdit.setEnabled(False)
	taxiUi.nextBtn.setEnabled(False)

	taxiUi.previousBtn.clicked.connect(lambda: getPageNumberAndStartWorkThread(taxiUi, ui))
	taxiUi.nextBtn.clicked.connect(lambda: getPageNumberAndStartWorkThread(taxiUi, ui))
	taxiUi.refreshBtn.clicked.connect(lambda: getPageNumberAndStartWorkThread(taxiUi, ui))
	taxiUi.pageNumberEdit.returnPressed.connect(lambda: getPageNumberAndStartWorkThread(taxiUi, ui))


def startWorkThread(self, taxiUi: TaxiUi.Ui_Taxi, start_line=1, end_line=22):
	# 在读取数据前禁用翻页键和刷新键
	taxiUi.previousBtn.setEnabled(False)
	taxiUi.pageNumberEdit.setEnabled(False)
	taxiUi.nextBtn.setEnabled(False)
	taxiUi.refreshBtn.setEnabled(False)
	# 启动线程开始获取数据库数据
	work_thread = WorkTread(start_line, end_line)
	work_thread.start()
	# 连接数据库错误时弹出错误提示框
	work_thread.conn_error.connect(lambda: showErrorMessage("数据库连接错误，请检查网络！"))
	# 数据湖数据获取完成后发射信号执行表数据写入
	work_thread.get_data_done.connect(self.setTableWidgetItem)
	return work_thread


def getPageNumberAndStartWorkThread(self, taxiUi: TaxiUi.Ui_Taxi, ui: Ui.Ui_MainWindow):
	"""
	1. 获取self.taxiUi.pageNumberEdit的值并且转换为整型，如果输入的值为空时会有错误弹窗；
	2. 如果输入的值可转换为整型则从数据库获取数据并显示在表中；
	"""
	try:
		pageNumber = int(taxiUi.pageNumberEdit.text())
	except ValueError as e:
		self.showErrorMessage("页码输入框内容不能为空！")
		self.logger.exception(e)
	else:
		s = ui.stackedWidget.sender().objectName()
		if s == taxiUi.previousBtn.objectName():
			startWorkThread(taxiUi, (pageNumber-2)*22+1, (pageNumber-1)*22)
			taxiUi.pageNumberEdit.setText(str(pageNumber-1))
		elif s == self.taxiUi.nextBtn.objectName():
			startWorkThread(taxiUi, pageNumber*22+1, (pageNumber+1)*22)
			taxiUi.pageNumberEdit.setText(str(pageNumber+1))
		elif s == self.taxiUi.refreshBtn.objectName():
			startWorkThread(taxiUi, (pageNumber-1)*22+1, pageNumber*22)
		elif s == self.taxiUi.pageNumberEdit.objectName():
			startWorkThread(taxiUi, (pageNumber-1)*22+1, pageNumber*22)


def setTableWidgetItem(self, ui: Ui.Ui_MainWindow, taxiUi: TaxiUi.Ui_Taxi, work_thread: WorkTread):
	# 在状态显示读取数据所消耗时间，只显示3秒
	ui.statusbar.showMessage("获取数据总耗时：{} ms".format(work_thread.total_time))

	# 将数据库的数据写入到table widget，建议将用tr()，字符串国际化
	index = 0
	for dic in work_thread.data:
		taxiUi.tableWidget.setItem(index, 0, QTableWidgetItem(taxiUi.tableWidget.tr(str(dic["name"]))))
		taxiUi.tableWidget.setItem(index, 1, QTableWidgetItem(taxiUi.tableWidget.tr(str(dic["amount"]))))
		index += 1
	if len(work_thread.data) < 22:
		for index2 in range(index, 23):
			taxiUi.tableWidget.setItem(index2, 0, QTableWidgetItem(taxiUi.tableWidget.tr(str(""))))
			taxiUi.tableWidget.setItem(index2, 1, QTableWidgetItem(taxiUi.tableWidget.tr(str(""))))
	self.taxiUi.yeLabel.setText("页/共%d条" % work_thread.max_id)
	# 数据读完后启用翻页键和刷新键self.ui.statusbar.showMessage
	previousAndNextButtonShow(taxiUi, work_thread.max_id)


def previousAndNextButtonShow(taxiUi: TaxiUi.Ui_Taxi, max_id):
	"""
	1. taxi ui界面的上下翻页，刷新按钮在未加载数据库数据时这个按钮需要设置为不可用
	2. 当页码输入框为空时其他按钮也要设置为无效
	3. 当前页页码为1时，上一页按钮要设置为不可用，页码为最大时下一页按钮要设置为不可用
	:param taxiUi:
	:param max_id:数据库总行数
	"""
	if taxiUi.pageNumberEdit.text() != '':
		taxiUi.refreshBtn.setEnabled(True)
		taxiUi.pageNumberEdit.setEnabled(True)
		if int(taxiUi.pageNumberEdit.text()) == 1:
			taxiUi.previousBtn.setEnabled(False)
		else:
			taxiUi.previousBtn.setEnabled(True)
		if int(taxiUi.pageNumberEdit.text()) == max_id // 22 + 1:
			taxiUi.nextBtn.setEnabled(False)
		else:
			taxiUi.nextBtn.setEnabled(True)
		if int(taxiUi.pageNumberEdit.text()) > max_id // 22 + 1:
			taxiUi.pageNumberEdit.setText(str(max_id // 22 + 1))


def showErrorMessage(self, message: str):
	errorMessage = QErrorMessage()
	errorMessage.setModal(True)
	errorMessage.showMessage(message)
	errorMessage.exec_()
