from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal, pyqtBoundSignal
import DatabaseOperation
import time


class WorkTread(QThread):
	# 读取数据库数据的线程
	get_data_done: pyqtBoundSignal
	get_data_done = pyqtSignal()

	def __init__(self, start_line=1, end_line=22):
		super(WorkTread, self).__init__()
		self.start_line = start_line
		self.end_line = end_line

	def run(self):
		conn, cursor = DatabaseOperation.connect_db()
		self.max_id = DatabaseOperation.get_max_id(cursor)
		self.data = DatabaseOperation.get_contents_of_table(cursor, self.start_line, self.end_line)
		DatabaseOperation.close(conn, cursor)
		print(self.data, "+", self.max_id)
		self.get_data_done.emit()

