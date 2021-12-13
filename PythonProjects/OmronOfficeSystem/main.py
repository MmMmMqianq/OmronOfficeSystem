import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import Ui
import taxi_ui


class MainWin(QMainWindow):
	def __init__(self):
		super(MainWin, self).__init__()
		self.ui = Ui.Ui_MainWindow()
		self.ui.setupUi(self)

		# self.widget1 = QWidget()
		# self.p = QPushButton("asdas", self.widget1)
		# self.ui.stackedWidget.addWidget(self.widget1)
		# self.ui.stackedWidget.setCurrentIndex(0)
		self.taxiUi = taxi_ui.Ui_Taxi()
		self.taxiUi.setupUi()


app = QApplication(sys.argv)
win = MainWin()
win.show()
sys.exit(app.exec_())