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

		self.ui = Ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.importWidget()

		self.p = QPushButton("asd", self)
		self.p1 = QPushButton("aaa", self)
		self.p1.move(50, 50)

		self.taxiUiSetup()

	def importWidget(self):
		# 将功能页面添加到主界面的栈容器中
		self.taxiUi = TaxiUi.Ui_Taxi()
		self.taxiUi.setupUi(self.ui.taxiPage)

	def taxiUiSetup(self):
		"""
		初始化self.taxiUi页面中的控件并将信号和槽绑定
		"""
		# 给pageNumberEdit设置校验器，只能输入整数
		# self.int_validator = QIntValidator(self)
		# self.int_validator.setBottom(1)
		# self.int_validator.setTop(999999)
		# self.taxiUi.pageNumberEdit.setValidator(self.int_validator)

		# self.taxiUi.previousBtn.setEnabled(False)
		# self.taxiUi.pageNumberEdit.setEnabled(False)
		# self.taxiUi.nextBtn.setEnabled(False)

		self.ui.taxiButton.clicked.connect(lambda: TaxiWidgetFunction.startWorkThread(taxiUi=self.taxiUi, start_line=1, end_line=22))
		self.ui.taxiButton.clicked.connect(lambda: self.taxiUi.pageNumberEdit.setText("1"))

		TaxiWidgetFunction.taxiUiInitial(self.taxiUi, self.ui)



		# self.taxiUi.previousBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		# self.taxiUi.nextBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		# self.taxiUi.refreshBtn.clicked.connect(self.getPageNumberAndStartWorkThread)
		# self.taxiUi.pageNumberEdit.returnPressed.connect(self.getPageNumberAndStartWorkThread)

	# def startWorkThread(self, start_line=1, end_line=22):
	# 	# 在读取数据前禁用翻页键和刷新键
	# 	self.taxiUi.previousBtn.setEnabled(False)
	# 	self.taxiUi.pageNumberEdit.setEnabled(False)
	# 	self.taxiUi.nextBtn.setEnabled(False)
	# 	self.taxiUi.refreshBtn.setEnabled(False)
	# 	# 启动线程开始获取数据库数据
	# 	self.work_thread1 = TaxiWidgetFunction.WorkTread(start_line, end_line)
	# 	self.work_thread1.start()
	# 	# 连接数据库错误时弹出错误提示框
	# 	self.work_thread1.conn_error.connect(lambda: self.showErrorMessage("数据库连接错误，请检查网络！"))
	# 	# 数据湖数据获取完成后发射信号执行表数据写入
	# 	self.work_thread1.get_data_done.connect(self.setTableWidgetItem)

	# def getPageNumberAndStartWorkThread(self):
	# 	"""
	# 	1. 获取self.taxiUi.pageNumberEdit的值并且转换为整型，如果输入的值为空时会有错误弹窗；
	# 	2. 如果输入的值可转换为整型则从数据库获取数据并显示在表中；
	# 	"""
	# 	try:
	# 		pageNumber = int(self.taxiUi.pageNumberEdit.text())
	# 	except ValueError as e:
	# 		self.showErrorMessage("页码输入框内容不能为空！")
	# 		self.logger.exception(e)
	# 	else:
	# 		s = self.ui.stackedWidget.sender().objectName()
	# 		if s == self.taxiUi.previousBtn.objectName():
	# 			self.startWorkThread((pageNumber-2)*22+1, (pageNumber-1)*22)
	# 			self.taxiUi.pageNumberEdit.setText(str(pageNumber-1))
	# 		elif s == self.taxiUi.nextBtn.objectName():
	# 			self.startWorkThread(pageNumber*22+1, (pageNumber+1)*22)
	# 			self.taxiUi.pageNumberEdit.setText(str(pageNumber+1))
	# 		elif s == self.taxiUi.refreshBtn.objectName():
	# 			self.startWorkThread((pageNumber-1)*22+1, pageNumber*22)
	# 		elif s == self.taxiUi.pageNumberEdit.objectName():
	# 			self.startWorkThread((pageNumber-1)*22+1, pageNumber*22)

	# def setTableWidgetItem(self):
	# 	# 在状态显示读取数据所消耗时间，只显示3秒
	# 	self.ui.statusbar.showMessage("获取数据总耗时：{} ms".format(self.work_thread1.total_time))
	#
	# 	# 将数据库的数据写入到table widget，建议将用tr()，字符串国际化
	# 	index = 0
	# 	for dic in self.work_thread1.data:
	# 		self.taxiUi.tableWidget.setItem(index, 0, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(dic["name"]))))
	# 		self.taxiUi.tableWidget.setItem(index, 1, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(dic["amount"]))))
	# 		index += 1
	# 	if len(self.work_thread1.data) < 22:
	# 		for index2 in range(index, 23):
	# 			self.taxiUi.tableWidget.setItem(index2, 0, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(""))))
	# 			self.taxiUi.tableWidget.setItem(index2, 1, QTableWidgetItem(self.taxiUi.tableWidget.tr(str(""))))
	# 	self.taxiUi.yeLabel.setText("页/共%d条" % self.work_thread1.max_id)
	# 	self.max_id = self.work_thread1.max_id
	# 	# 数据读完后启用翻页键和刷新键self.ui.statusbar.showMessage
	# 	TaxiWidgetFunction.previousAndNextButtonShow(self.taxiUi, self.work_thread1.max_id)

	# def showErrorMessage(self, message: str):
	# 	errorMessage = QErrorMessage()
	# 	errorMessage.setModal(True)
	# 	errorMessage.showMessage(message)
	# 	errorMessage.exec_()


app = QApplication(sys.argv)
logging.config.fileConfig("log/logging.conf")
win = MainWin()
win.show()
sys.exit(app.exec_())
