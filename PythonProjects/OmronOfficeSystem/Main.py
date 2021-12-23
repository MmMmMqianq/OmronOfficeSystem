"""
数据库账号：omron
密码：omron@2021
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTableWidgetItem
from PyQt5.QtGui import QIntValidator
import Ui
import TaxiUi
import TaxiWidgetFunction


class MainWin(QMainWindow):
	def __init__(self):
		super(MainWin, self).__init__()
		self.ui = Ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.importWidget()

		self.int_validator = QIntValidator(self)
		self.int_validator.setBottom(1)
		self.int_validator.setTop(999999)
		self.taxiUi.pageNumberLineEdit.setValidator(self.int_validator)

		self.taxiUi.previousPageButton.setEnabled(False)
		self.taxiUi.pageNumberLineEdit.setEnabled(False)
		self.taxiUi.nextPageButton.setEnabled(False)
		self.b = QPushButton("asdas", self)

		self.ui.taxiButton.clicked.connect(lambda: self.startWorkThread(1, 22))
		self.ui.taxiButton.clicked.connect(lambda: self.taxiUi.pageNumberLineEdit.setText("1"))
		self.taxiUi.refreshButton.clicked.connect(lambda: self.startWorkThread(
			(int(self.taxiUi.pageNumberLineEdit.text()) - 1) * 22 + 1, int(self.taxiUi.pageNumberLineEdit.text()) * 22
			))
		self.taxiUi.pageNumberLineEdit.editingFinished.connect(lambda: self.startWorkThread(
			(int(self.taxiUi.pageNumberLineEdit.text())-1)*22+1, int(self.taxiUi.pageNumberLineEdit.text())*22
			))
		self.taxiUi.previousPageButton.clicked.connect(lambda: self.startWorkThread(
			(int(self.taxiUi.pageNumberLineEdit.text())-2)*22+1, (int(self.taxiUi.pageNumberLineEdit.text())-1)*22
			))
		self.taxiUi.previousPageButton.clicked.connect(lambda: self.taxiUi.pageNumberLineEdit.setText(
			str(int(self.taxiUi.pageNumberLineEdit.text())-1)
			))
		self.taxiUi.nextPageButton.clicked.connect(lambda: self.startWorkThread(
			(int(self.taxiUi.pageNumberLineEdit.text())) * 22 + 1, (int(self.taxiUi.pageNumberLineEdit.text())+1) * 22
			))
		self.taxiUi.nextPageButton.clicked.connect(lambda: self.taxiUi.pageNumberLineEdit.setText(
			str(int(self.taxiUi.pageNumberLineEdit.text()) + 1)
			))

		self.taxiUi.pageNumberLineEdit.textChanged.connect(self.previousAndNextButtonShow)

		# self.taxiUi.pageNumberLineEdit.cursorPositionChanged.connect(lambda: self.taxiUi.refreshButton.setEnabled(False))

	def importWidget(self):
		# 将功能页面添加到主界面的栈容器中
		self.taxiUi = TaxiUi.Ui_Taxi()
		self.taxiUi.setupUi(self.ui.taxiPage)

	def startWorkThread(self, start_line=1, end_line=22):
		print(1)
		# 在读取数据前禁用翻页键和刷新键
		self.taxiUi.previousPageButton.setEnabled(False)
		# self.taxiUi.pageNumberLineEdit.setEnabled(False)
		self.taxiUi.nextPageButton.setEnabled(False)
		self.taxiUi.refreshButton.setEnabled(False)
		# 启动线程开始获取数据库数据
		self.work_thread1 = TaxiWidgetFunction.WorkTread(start_line, end_line)
		self.work_thread1.start()
		self.work_thread1.get_data_done.connect(self.setTableWidgetItem)

	def setTableWidgetItem(self):
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
		# 数据读完后启用翻页键和刷新键
		self.taxiUi.pageNumberLineEdit.setEnabled(True)
		self.taxiUi.refreshButton.setEnabled(True)
		self.previousAndNextButtonShow()

		print("写入完成")

	def previousAndNextButtonShow(self):
		if self.taxiUi.pageNumberLineEdit.text() != '':
			if int(self.taxiUi.pageNumberLineEdit.text()) == 1:
				self.taxiUi.previousPageButton.setEnabled(False)
			else:
				self.taxiUi.previousPageButton.setEnabled(True)
			if int(self.taxiUi.pageNumberLineEdit.text()) == self.max_id//22 + 1:
				self.taxiUi.nextPageButton.setEnabled(False)
			else:
				self.taxiUi.nextPageButton.setEnabled(True)
			if int(self.taxiUi.pageNumberLineEdit.text()) > self.max_id//22+1:
				self.taxiUi.pageNumberLineEdit.setText(str(self.max_id//22+1))
		else:
			# 当输入框为空时，刷新键不能使用，否则会报错
			self.taxiUi.refreshButton.setEnabled(False)


app = QApplication(sys.argv)
win = MainWin()
win.show()
sys.exit(app.exec_())