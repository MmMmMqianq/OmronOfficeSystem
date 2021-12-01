from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout, QDateTimeEdit, QCalendarWidget, QPushButton
from PyQt5.QtCore import QTime, QDate

class GetDateAndTime(QDialog):
	def __init__(self):
		super(GetDateAndTime, self).__init__()

		self.setWindowTitle("获取时间")

		self.dateTime = QDateTimeEdit()
		self.dateTime.setTime(QTime.currentTime())
		self.dateTime.setDate(QDate.currentDate())

		self.date = QCalendarWidget()
		self.date.clicked.connect(self.getDate)

		self.okButton = QPushButton("ok")
		self.cancelButton = QPushButton("cancel")
		self.okButton.clicked.connect(self.accept)
		self.cancelButton.clicked.connect(self.reject)

		self.hLayout = QHBoxLayout()
		self.hLayout.addWidget(self.okButton)
		self.hLayout.addWidget(self.cancelButton)

		self.vLayout = QVBoxLayout(self)
		self.vLayout.addWidget(self.dateTime)
		self.vLayout.addWidget(self.date)
		self.vLayout.addLayout(self.hLayout)

	def getDate(self, date):
		self.dateTime.setDate(date)