import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QWidget, QVBoxLayout, QMenu, QAction, QPushButton, \
	QMessageBox, QComboBox, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QIcon
from PyQt5.QtCore import Qt, QPoint, QModelIndex, QSize


class TableViewDemo(QMainWindow):
	def __init__(self):
		super(TableViewDemo, self).__init__()

		self.resize(600, 500)
		self.setWindowTitle("这是一个TableView实例")

		# 创建标准项目模型
		self.model = QStandardItemModel(100, 4)
		self.model.setHorizontalHeaderLabels(["ID", "姓名", "绰号", "性别"])  # 设置水平标题标签

		# 创建标准项目
		self.item00 = QStandardItem("124")
		self.item00.setTextAlignment(Qt.AlignCenter)  # 设置item对齐方式为居中
		self.item00.setBackground(QBrush(Qt.cyan))  # 设置背景色
		self.item00.setIcon(QIcon("./images/b1.ico"))  # 设置图标
		self.item01 = QStandardItem(QIcon("./images/b5.png"), "张三")
		self.item01.setTextAlignment(Qt.AlignCenter)
		self.item02 = QStandardItem("法外狂徒")
		self.item02.setTextAlignment(Qt.AlignCenter)
		self.item03 = QStandardItem()

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
		self.model.setItem(0, 3, self.item03)

		self.model.setItem(1, 0, self.item10)
		self.model.setItem(1, 1, self.item11)
		self.model.setItem(1, 2, self.item12)

		# 创建tableView
		self.tableView = QTableView()
		# 将标准项目模型设置到tableView，建议model设置完item后再将model设置带tableView,因为有些方法使用会没有效果
		self.tableView.setModel(self.model)
		self.tableView.setShowGrid(True)  # 设置是否显示网格
		self.tableView.setCornerButtonEnabled(True)  # 设置拐角处的全选按钮是否可用
		self.tableView.setSpan(2, 0, 2, 2)  # 合并单元格

		comboBox = QComboBox()
		comboBox.addItems(["-请选择-", "男", "女"])
		self.tableView.setIndexWidget(self.item03.index(), comboBox)  # 在item中插入widget

		self.tableView.setIconSize(QSize(100, 100))  # 设置图片大小
		self.tableView.resizeColumnsToContents()  # 所有列根据item中文本的长度自动调整单元格的宽度
		self.tableView.resizeRowsToContents()  # 所有行根据item中文本的长度自动调整单元格的宽度
		self.tableView.setSelectionBehavior(0)  # 设置选择的行为，默认0是选择单个item，1为选择行，2位选择列

		findItemsList = self.model.findItems("123", Qt.MatchExactly)  # 查找匹配项目并将背景色设置为黄色
		self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
		self.tableView.verticalScrollBar().setSliderPosition(findItemsList[0])  # 将纵向滚动条移动到第一个匹配项处
		for findItem in findItemsList:
			findItem.setBackground(QBrush(Qt.yellow))

		# 设置上下文菜单
		self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
		self.tableView.customContextMenuRequested.connect(self.getContextMenu)  # 返回坐标位置

		self.centralWidget = QWidget()
		self.vLayout = QVBoxLayout(self.centralWidget)
		self.button = QPushButton("按钮")
		self.vLayout.addWidget(self.tableView)
		self.vLayout.addWidget(self.button)
		self.setCentralWidget(self.centralWidget)

		# self.button.clicked.connect(lambda: print(self.getLineNumber(self.tableView, self.model)))

	def getContextMenu(self, mousePosition: QPoint):
		"""
		显示上下文菜单
		:param mousePosition: 鼠标当前位置
		:return: None
		"""
		self.isSelectedLines, self.lineNumberList, self.selectedItemsRowNumberList = self.getLineNumber(self.tableView, self.model)
		globalMousePos = self.tableView.mapToGlobal(mousePosition)  # 坐标转换
		contextMenu = QMenu()
		insertLineUpAction = QAction("向上插入一行")
		insertLineDownAction = QAction("向下插入一行")
		removeLinesAction = QAction("删除")
		removeLinesAction.setShortcut("ctrl+d")
		contextMenu.addActions([insertLineUpAction, insertLineDownAction, removeLinesAction])
		contextMenu.move(globalMousePos)  # 将上下文菜单移动到鼠标位置

		insertLineUpAction.triggered.connect(self.insertLinesUp)
		insertLineDownAction.triggered.connect(self.insertLinesDown)
		removeLinesAction.triggered.connect(self.removeLines)
		contextMenu.exec_()

	def insertLinesUp(self):
		"""
		向上插入一行
		:return: None
		"""
		if self.isSelectedLines:
			self.model.insertRow(self.lineNumberList[0])
			self.tableView.setRowHeight(self.lineNumberList[0], self.tableView.rowHeight(self.lineNumberList[0] + 1))
		else:
			messageBox = QMessageBox()
			messageBox.setText("请选择整行！")
			messageBox.setWindowModality(Qt.ApplicationModal)
			self.ret = messageBox.exec_()
			if self.ret == 1024:
				allRowNumber = self.removeSameItemFromList(self.selectedItemsRowNumberList)
				self.tableView.selectRow(allRowNumber[0])

	def insertLinesDown(self):
		"""
		向下插入一行
		:return: None
		"""
		if self.isSelectedLines:
			self.model.insertRow(self.lineNumberList[-1] + 1)
			self.tableView.setRowHeight(self.lineNumberList[-1] + 1, self.tableView.rowHeight(self.lineNumberList[-1]))
		else:
			messageBox = QMessageBox()
			messageBox.setText("请选择整行！")
			messageBox.setWindowModality(Qt.ApplicationModal)
			self.ret = messageBox.exec_()
			if self.ret == 1024:
				allRowNumber = self.removeSameItemFromList(self.selectedItemsRowNumberList)
				self.tableView.selectRow(allRowNumber[0])

	def removeLines(self):
		"""
		删除选中的行
		:return: None
		"""
		if self.isSelectedLines:
			self.lineNumberList.reverse()
			for i in self.lineNumberList:
				self.model.removeRows(i, 1)
		else:
			messageBox = QMessageBox()
			messageBox.setText("请选择整行！")
			messageBox.setWindowModality(Qt.ApplicationModal)
			self.ret = messageBox.exec_()
			if self.ret == 1024:
				allRowNumber = self.removeSameItemFromList(self.selectedItemsRowNumberList)
				self.tableView.selectRow(allRowNumber[0])

	def getLineNumber(self, tableView: QTableView, model: QStandardItemModel):
		"""
		判断选中的是否为整行
		:param tableView: QTableView
		:param model: QStandardItemModel
		:return: False或者True，如果tableView选择的不是一个完整的行则返回False，如果选择的是完整的行则返回True；
				selectedLineNumberList:被选择完整行的行号组成的列表；
				rowNumberList: 所有被选中的item所在的行号列表
		"""
		selectedItem = tableView.selectedIndexes()
		rowNumberList = []  # 被选中的所有items的行号组成的列表
		columnNumberList = []  # 被选中的所有items的列号组成的列表
		for item in selectedItem:
			rowNumberList.append(item.row())
			columnNumberList.append(item.column())
			if (self.tableView.rowSpan(item.row(), item.column()) != 1) | \
					(self.tableView.columnSpan(item.row(), item.column()) != 1):
				for i1 in range(1, self.tableView.rowSpan(item.row(), item.column())):
					for i3 in range(item.column(), self.tableView.columnSpan(item.row(), item.column())):
						columnNumberList.append(i3)
						rowNumberList.append(item.row() + i1)
				for i2 in range(1, self.tableView.columnSpan(item.row(), item.column())):
					columnNumberList.append(item.column() + i2)
					rowNumberList.append(item.row())
		rowNumberList.sort(reverse=False)
		columnNumberList.sort(reverse=False)

		selectedLineNumberlist = []
		if len(rowNumberList) % model.columnCount() == 0:
			for i in range(0, int(len(rowNumberList) / model.columnCount())):
				for rowNumber in rowNumberList[i * model.columnCount():model.columnCount() * (i + 1)]:
					if rowNumber != rowNumberList[i * model.columnCount()]:
						return False, [], rowNumberList
				selectedLineNumberlist.append(rowNumberList[i * model.columnCount()])
		else:
			return False, [], rowNumberList
		return True, selectedLineNumberlist, rowNumberList

	def removeSameItemFromList(self, originalList: list):
		"""
		剔除给定列表中重复的选项并返回
		:param originalList:
		:return:
		"""
		OriginalListCopy = originalList.copy()
		originalList.sort(reverse=False)
		noRepetitionItemList = []
		if len(originalList) != 1:
			for i in range(0, len(originalList) - 1):
				if i == 0:
					if originalList[i] == originalList[i + 1]:
						noRepetitionItemList.append(originalList[i + 1])
					else:
						noRepetitionItemList.append(originalList[i])
						noRepetitionItemList.append(originalList[i + 1])
				else:
					if originalList[i] != originalList[i + 1]:
						noRepetitionItemList.append(originalList[i + 1])
			return noRepetitionItemList
		else:
			noRepetitionItemList = originalList
			return noRepetitionItemList

	def a(self):
		pass


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TableViewDemo()
	window.show()
	sys.exit(app.exec_())
