import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QWidget, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem,  QMouseEvent
from PyQt5.QtCore import Qt


class TableViewDemo(QWidget):
	def __init__(self):
		super(TableViewDemo, self).__init__()

		self.resize(350, 500)
		self.setWindowTitle("这是一个TableView实例")

		# 创建标准项目模型
		self.model = QStandardItemModel(10, 3)
		self.model.setHorizontalHeaderLabels(["ID", "姓名", "绰号"])  # 设置水平标题标签

		# 创建标准项目
		self.item00 = QStandardItem("124")
		self.item00.setTextAlignment(Qt.AlignCenter)  # 设置item对齐方式为居中
		self.item01 = QStandardItem("张三")
		self.item01.setTextAlignment(Qt.AlignCenter)
		self.item02 = QStandardItem("法外狂徒")
		self.item02.setTextAlignment(Qt.AlignCenter)

		self.item10 = QStandardItem("123")
		self.item10.setTextAlignment(Qt.AlignCenter)  # 设置item对齐方式为居中
		self.item11 = QStandardItem("李四")
		self.item11.setTextAlignment(Qt.AlignCenter)
		self.item12 = QStandardItem("无法无天")
		self.item12.setTextAlignment(Qt.AlignCenter)

		# 将标准项目设置到标准模型内
		self.model.setItem(0, 0, self.item00)
		self.model.setItem(0, 1, self.item01)
		self.model.setItem(0, 2, self.item02)

		self.model.setItem(1, 0, self.item10)
		self.model.setItem(1, 1, self.item11)
		self.model.setItem(1, 2, self.item12)

		# 创建tableView
		self.tableView = QTableView()
		# 将标准项目模型设置到tableView，建议model设置完item后再将model设置带tabelView,因为有些方法使用会没有效果
		self.tableView.setModel(self.model)
		self.tableView.setShowGrid(True)  # 设置是否显示网格
		self.tableView.setCornerButtonEnabled(True)  # 设置拐角处的全选按钮是否可用
		self.tableView.setSpan(2, 0, 2, 3)  # 合并单元格
		print("1. 坐标(2,0)单元格行跨度为：", self.tableView.rowSpan(2, 0))
		print("2. 坐标(2,0)单元格列跨度为：", self.tableView.columnSpan(2, 0))
		self.tableView.resizeColumnsToContents()  # 所有列根据item中文本的长度自动调整单元格的宽度
		self.tableView.resizeRowsToContents()  # 所有行根据item中文本的长度自动调整单元格的宽度

		self.vLayout = QVBoxLayout(self)
		self.vLayout.addWidget(self.tableView)

		self.setMouseTracking(True)
		self.tableView.setMouseTracking(True)

	def mousePressEvent(self, event: QMouseEvent):
		print(event.button())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TableViewDemo()
	window.show()
	sys.exit(app.exec_())