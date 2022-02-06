"""
数据库账号：omron
密码：omron@2021
"""
from sys import argv
from sys import exit
from sys import path
from os import getcwd

ph = getcwd()
path.append(ph + "/communication")

from PyQt5.QtWidgets import QApplication, QMainWindow
import logging
import logging.config
import Ui
import TaxiWidgetFunction
import communication.CommWidgetFunction


class MainWin(QMainWindow):
	def __init__(self):
		super(MainWin, self).__init__()
		self.logger = logging.getLogger("applog")
		# 加载主界面
		self.ui = Ui.Ui_MainWindow()
		self.ui.setupUi(self)
		# 导入子界面
		self.importWidget()
		# 主界面设置
		self.setupUi()

	def setupUi(self):
		self.ui.taxiButton.clicked.connect(self.selectWidget)
		self.ui.taxiButton.clicked.connect(lambda: self.taxiUi.startWorkThread(1, 22))

		self.ui.commBtn.clicked.connect(self.selectWidget)

	# self.taxiUi.defSignal.get_data_done.connect(lambda: self.ui.statusbar.showMessage("获取数据耗时："+str(self.taxiUi.get_total_time)))
	# self.taxiUi.defSignal.insert_data_done.connect(lambda: self.ui.statusbar.showMessage("插入数据耗时："+str(self.taxiUi.insert_total_time)))

	def importWidget(self):
		# 将taxi功能页面添加到主界面的栈容器中
		self.taxiUi = TaxiWidgetFunction.TaxiWidgetUi()
		self.ui.stackedWidget.addWidget(self.taxiUi)
		# 将communication功能页面添加到主界面的栈容器中
		self.commUi = communication.CommWidgetFunction.CommWidgetUi()
		self.ui.stackedWidget.addWidget(self.commUi)

		self.ui.stackedWidget.setCurrentWidget(self.commUi)

	def selectWidget(self):
		self.s = self.sender()
		self.logger.debug(self.s)
		if self.s.objectName() == self.ui.taxiButton.objectName():
			self.ui.stackedWidget.setCurrentWidget(self.taxiUi)
		if self.s.objectName() == self.ui.commBtn.objectName():
			self.ui.stackedWidget.setCurrentWidget(self.commUi)


logging.config.fileConfig(ph+"/log/logging.conf")
app = QApplication(argv)
win = MainWin()
win.show()
exit(app.exec_())
