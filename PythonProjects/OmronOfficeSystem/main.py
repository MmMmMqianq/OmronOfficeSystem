import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import Ui
import taxi_ui


class MainWin(QMainWindow):
	def __init__(self):
		super(MainWin, self).__init__()
		self.ui = Ui.Ui_MainWindow()
		self.ui.setupUi(self)
		self.importWidget()
		self.taxiWidgetFunction()

	def taxiWidgetFunction(self):
		pass

	def importWidget(self):
		"""
		将功能页面添加到主界面的栈容器中
		"""
		self.taxiUi = taxi_ui.Ui_Taxi()
		self.taxiUi.setupUi(self.ui.taxiPage)


app = QApplication(sys.argv)
win = MainWin()
win.show()
sys.exit(app.exec_())