"""
数据库账号：omron
密码：omron@2021
"""
import sys
import logging
import logging.config
import time
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QErrorMessage
from PyQt5.QtGui import QIntValidator
import Ui
import TaxiUi
import TaxiWidgetFunction


class MainWin(QMainWindow):
	def __init__(self):
		super(MainWin, self).__init__()
		self.logger = logging.getLogger("applogger")
		# 加载主界面
		self.ui = Ui.Ui_MainWindow()
		self.ui.setupUi(self)
		# 导入子界面
		self.importWidget()
		# 主界面设置
		self.setupUi()

	def setupUi(self):
		# self.taxiUi.work_thread1.get_data_done.connect(lambda: self.taxiUi.work_thread1.total_time
		pass

	def importWidget(self):
		# 将taxi功能页面添加到主界面的栈容器中
		self.taxiUi = TaxiWidgetFunction.TaxiWidgetUi()
		self.ui.stackedWidget.addWidget(self.taxiUi)
		self.ui.stackedWidget.setCurrentWidget(self.taxiUi)


app = QApplication(sys.argv)
logging.config.fileConfig("log/logging.conf")
win = MainWin()
win.show()
sys.exit(app.exec_())
