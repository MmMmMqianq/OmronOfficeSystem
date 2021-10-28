import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QDateTimeEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


class QDateTimeEditDemo(QWidget):
	def __init__(self):
		super(QDateTimeEditDemo, self).__init__()

		self.setWindowTitle("这是一个QDateTimeEdit实例")
		self.resize(500, 300)

		self.dateTimeEdit1 = QDateTimeEdit()
		self.dateTimeEdit1.setDateTime(QDateTime.currentDateTime())
		self.dateTimeEdit1.setDisplayFormat("yy-MM-dd hh:mm:ss")

		self.dateTimeEdit2 = QDateTimeEdit()
		self.dateTimeEdit2.setDisplayFormat("yy/MM/dd hh:mm:ss")
		# self.dateTimeEdit2.setDisplayFormat("yy/MM/dd")  # 只显示日期
		self.dateTimeEdit2.setDateTime(QDateTime.currentDateTime())
		self.dateTimeEdit2.setTimeSpec(Qt.UTC)

		self.dateTimeEdit3 = QDateTimeEdit()
		self.dateTimeEdit3.setDisplayFormat("yyyy.MM.dd hh:mm:ss")
		# self.dateTimeEdit3.setDisplayFormat("hh:mm:ss")  # 只显示时间
		self.dateTimeEdit3.setDateTime(QDateTime.currentDateTime())
		self.dateTimeEdit3.setCalendarPopup(True)
		self.dateTimeEdit3.setDateTimeRange(QDateTime(1990, 1, 1, 0, 0, 0), QDateTime(2300, 12, 30, 23, 59, 59))
		self.dateTimeEdit3.setTimeSpec(Qt.LocalTime)
		self.dateTimeEdit3.setCurrentSection(QDateTimeEdit.MinuteSection)
		self.dateTimeEdit3.dateTimeChanged.connect(self.dTChanged)
		self.dateTimeEdit3.dateChanged.connect(self.dChanged)
		self.dateTimeEdit3.timeChanged.connect(self.tChanged)

		self.button = QPushButton("按钮")
		self.button.clicked.connect(self.clickedButton)

		vLayout = QVBoxLayout(self)
		vLayout.addWidget(self.dateTimeEdit1)
		vLayout.addWidget(self.dateTimeEdit2)
		vLayout.addWidget(self.dateTimeEdit3)
		vLayout.addWidget(self.button)

	def clickedButton(self):
		print("1. QDateTimeEdit.SecondSection的值为：", self.dateTimeEdit3.sectionText(QDateTimeEdit.SecondSection))

	def dTChanged(self):
		print("日期或者时间变化的信号触发了！！！")

	def dChanged(self):
		print("日期变化的信号触发了！！！")

	def tChanged(self):
		print("时间变化的信号触发了！！！")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QDateTimeEditDemo()
	mainWindow.show()
	sys.exit(app.exec_())
