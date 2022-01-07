from PyQt5.QtCore import QThread, pyqtSignal, pyqtBoundSignal
from PyQt5.QtWidgets import QErrorMessage
import DatabaseOperation
import pymysql
import time
import TaxiUi
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
				# self.logger.debug("数据库获取数据完成！")

def previousAndNextButtonShow(taxi_ui: TaxiUi.Ui_Taxi, max_id):
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




