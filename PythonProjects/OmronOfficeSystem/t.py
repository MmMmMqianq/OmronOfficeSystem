from PyQt5.QtCore import QThread, pyqtSignal, pyqtBoundSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QErrorMessage, QWidget, QApplication, QTableWidgetItem, QHBoxLayout, QTableWidget, \
	QMessageBox, QTableWidgetSelectionRange, QMenu, QAction, QPushButton
from PyQt5.QtCore import QObject, Qt, QPoint
import DatabaseOperation
import sys
import pymysql
import time
import TaxiUi
import logging
import logging.config
import threading
import random


class Slots(QObject):
	get_data_done: pyqtBoundSignal
	conn_error: pyqtBoundSignal
	insert_data_done: pyqtBoundSignal
	delete_data_done: pyqtBoundSignal
	update_data_done: pyqtBoundSignal
	get_data_done = pyqtSignal()
	conn_error = pyqtSignal(str)
	insert_data_done = pyqtSignal(str)
	delete_data_done = pyqtSignal(str)
	update_data_done = pyqtSignal(str)


class TaxiWidgetUi(QWidget):
	sId = None
	def __init__(self):
		super(TaxiWidgetUi, self).__init__()
		self.slot = Slots()
		self.button = QPushButton("asd", self)
		self.button.clicked.connect(self.a)
		self.slot.conn_error.connect(self.b)
		self.slot.update_data_done.connect(self.b)

	def a(self):
		self.slot.conn_error.emit("qqqq")
		self.slot.update_data_done.emit("aaa")

	def b(self, a):
		print(a)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	logging.config.fileConfig("log/logging.conf")
	win = TaxiWidgetUi()
	win.show()
	sys.exit(app.exec_())