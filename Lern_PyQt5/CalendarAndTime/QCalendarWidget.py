import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate, Qt


class QCalendarWidgetDemo(QWidget):
	def __init__(self):
		super(QCalendarWidgetDemo, self).__init__()

		self.setWindowTitle("这是一个QCalendarWidget实例")
		self.resize(600, 500)

		self.calendarWidget = QCalendarWidget(self)
		self.calendarWidget.setDateRange(QDate(1990, 1, 1), QDate(2100, 12, 30))
		self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
		self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
		self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
		self.calendarWidget.setSelectionMode(True)
		self.calendarWidget.setGridVisible(True)
		self.calendarWidget.setNavigationBarVisible(True)

		self.label = QLabel(self)
		self.label.resize(600, 30)
		self.label.move(10, 470)
		self.label.setText("ISO 8601扩展规范表示日期和时间的格式为：yyyy-MM-dd，选中的日期为："+self.calendarWidget.selectedDate().toString("yyyy-MM-dd"))

		self.label2 = QLabel(self)
		self.label2.resize(600, 30)
		self.label2.move(10, 450)
		self.label2.setText("默认日期和时间的格式为：Sat May 20 1995，选中的日期为：" + self.calendarWidget.selectedDate().toString())

		self.calendarWidget.selectionChanged.connect(self.labelText)

	def labelText(self):
		self.label.setText("ISO 8601扩展规范表示日期和时间的格式为：yyyy-MM-dd，选中的日期为："+self.calendarWidget.selectedDate().toString("yyyy-MM-dd"))
		self.label2.setText("默认日期和时间的格式为：Sat May 20 1995，选中的日期为："+self.calendarWidget.selectedDate().toString())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainWindow = QCalendarWidgetDemo()
	mainWindow.show()
	sys.exit(app.exec_())
