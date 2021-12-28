import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget, \
	QTableWidgetItem, QMessageBox, QMenu, QAction, QTableWidgetSelectionRange, QPushButton, QLineEdit, QSpacerItem, \
	QSizePolicy
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QBrush


class TableWidget(QWidget):
	def __init__(self):
		super(TableWidget, self).__init__()

		self.setWindowTitle("这是一个TableWidget实例")
		self.resize(500, 500)

		# 创建QTableWidget
		self.table = QTableWidget()
		self.table.setColumnCount(4)
		self.table.setRowCount(15)
		self.table.setHorizontalHeaderLabels(["ID", "姓名", "绰号", "年龄"])

		# 创建QTableWidgetItem
		tableWidgetItemList = []  # 将所有(row, column, item)元祖放到一个列表里
		for i in range(0, 15):
			for ii in range(0, self.table.columnCount()):
				tableWidgetItemList.append((i, ii, QTableWidgetItem(self.table.tr("(%d, %d)" % (i, ii)))))
				self.table.setItem(*tableWidgetItemList[self.table.columnCount() * i + ii])
				tableWidgetItemList[self.table.columnCount() * i + ii][2].setTextAlignment(Qt.AlignCenter)

		# 设置上下文菜单
		self.table.setContextMenuPolicy(Qt.CustomContextMenu)
		self.mousePosition = QPoint(100, 10)
		self.table.customContextMenuRequested.connect(self.getContextMenu)

		# 设置行高度和列宽度根据设置文本长度自适应
		self.table.resizeColumnsToContents()
		self.table.resizeRowsToContents()

		# 合并单元格
		self.table.insertRow(14)
		self.table.insertRow(15)
		self.table.setSpan(14, 0, 2, 2)

		self.hLayout = QHBoxLayout(self)
		self.vLayout = QVBoxLayout()

		self.gLayout = QGridLayout()
		self.findButton = QPushButton("查找")
		self.findButton.clicked.connect(lambda: self.findContent(self.table, self.lineEdit))  # table的查找功能
		self.lineEdit = QLineEdit()
		self.lineEdit.setPlaceholderText("输入查找的文本")
		self.gLayout.addWidget(self.lineEdit, 0, 0, 1, 2)
		self.gLayout.addWidget(self.findButton, 1, 1, 1, 1)
		self.spacerItem1 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
		self.vLayout.addLayout(self.gLayout)
		self.vLayout.addItem(self.spacerItem1)

		self.hLayout.addWidget(self.table)
		self.hLayout.addLayout(self.vLayout)

	def getContextMenu(self, mousePosition: QPoint):
		"""
		显示上下文菜单
		:param mousePosition: 鼠标当前位置, 由QTableWidget.customContextMenuRequested信号自动传入
		:return: None
		"""
		# self.mousePosition = mousePosition
		self.isSelectedLines, self.lineNumberList, self.selectedItemsRowNumberList = self.getLineNumber(self.table)
		globalMousePos = self.table.mapToGlobal(mousePosition)  # 坐标转换
		contextMenu = QMenu()
		insertLineUpAction = QAction("向上插入一行")
		insertLineDownAction = QAction("向下插入一行")
		removeLinesAction = QAction("删除")
		contextMenu.addActions([insertLineUpAction, insertLineDownAction, removeLinesAction])
		contextMenu.move(globalMousePos)  # 将上下文菜单移动到鼠标位置

		insertLineUpAction.triggered.connect(lambda: self.insertLinesUp(self.table))
		insertLineDownAction.triggered.connect(lambda: self.insertLinesDown(self.table))
		removeLinesAction.triggered.connect(lambda: self.removeLines(self.table))
		contextMenu.exec_()

	def insertLinesUp(self, table: QTableWidget):
		"""
		向上插入一行
		:return: None
		"""
		if self.isSelectedLines:
			table.insertRow(self.lineNumberList[0])
			table.setRowHeight(self.lineNumberList[0], table.rowHeight(self.lineNumberList[0] + 1))
		else:
			messageBox = QMessageBox()
			messageBox.setText("请选择整行！")
			messageBox.setWindowModality(Qt.ApplicationModal)
			self.ret = messageBox.exec_()
			if self.ret == 1024:
				allRowNumber = self.removeSameItemFromList(self.selectedItemsRowNumberList)
				table.setRangeSelected(QTableWidgetSelectionRange(allRowNumber[0], 0,
				                                                  allRowNumber[-1], table.columnCount() - 1), True)

	def insertLinesDown(self, table: QTableWidget):
		"""
		向下插入一行
		:return: None
		"""
		if self.isSelectedLines:
			table.insertRow(self.lineNumberList[-1] + 1)
			table.setRowHeight(self.lineNumberList[-1] + 1, table.rowHeight(self.lineNumberList[-1]))
		else:
			messageBox = QMessageBox()
			messageBox.setText("请选择整行！")
			messageBox.setWindowModality(Qt.ApplicationModal)
			self.ret = messageBox.exec_()
			if self.ret == 1024:
				allRowNumber = self.removeSameItemFromList(self.selectedItemsRowNumberList)
				table.setRangeSelected(QTableWidgetSelectionRange(allRowNumber[0], 0,
				                                                  allRowNumber[-1], table.columnCount() - 1), True)

	def removeLines(self, table: QTableWidget):
		"""
		删除选中的行
		:return: None
		"""
		if self.isSelectedLines:
			self.lineNumberList.reverse()
			for i in self.lineNumberList:
				table.removeRow(i)
		else:
			messageBox = QMessageBox()
			messageBox.setText("请选择整行！")
			messageBox.setWindowModality(Qt.ApplicationModal)
			self.ret = messageBox.exec_()
			if self.ret == 1024:
				allRowNumber = self.removeSameItemFromList(self.selectedItemsRowNumberList)
				table.setRangeSelected(QTableWidgetSelectionRange(allRowNumber[0], 0,
				                                                  allRowNumber[-1], table.columnCount() - 1), True)

	def getLineNumber(self, table: QTableWidget):
		"""
		判断选中的是否为整行
		:param table: QTableView
		:return: False或者True，如果tableView选择的不是一个完整的行则返回False，如果选择的是完整的行则返回True；
				selectedLineNumberList:被选择完整行的行号组成的列表；
				rowNumberList: 所有被选中的item所在的行号列表
		"""
		selectedItem = table.selectedIndexes()
		rowNumberList = []  # 被选中的所有items的行号组成的列表
		columnNumberList = []  # 被选中的所有items的列号组成的列表
		for item in selectedItem:
			rowNumberList.append(item.row())
			columnNumberList.append(item.column())
			if (table.rowSpan(item.row(), item.column()) != 1) | \
					(table.columnSpan(item.row(), item.column()) != 1):
				for i1 in range(1, table.rowSpan(item.row(), item.column())):
					for i3 in range(item.column(), table.columnSpan(item.row(), item.column())):
						columnNumberList.append(i3)
						rowNumberList.append(item.row() + i1)
				for i2 in range(1, table.columnSpan(item.row(), item.column())):
					columnNumberList.append(item.column() + i2)
					rowNumberList.append(item.row())
		rowNumberList.sort(reverse=False)
		columnNumberList.sort(reverse=False)

		selectedLineNumberList = []
		if len(rowNumberList) % table.columnCount() == 0:
			for i in range(0, int(len(rowNumberList) / table.columnCount())):
				for rowNumber in rowNumberList[i * table.columnCount():table.columnCount() * (i + 1)]:
					if rowNumber != rowNumberList[i * table.columnCount()]:
						return False, [], rowNumberList
				selectedLineNumberList.append(rowNumberList[i * table.columnCount()])
		else:
			return False, [], rowNumberList
		return True, selectedLineNumberList, rowNumberList

	def removeSameItemFromList(self, originalList: list):
		"""
		剔除给定列表中重复的选项并返回
		:param originalList:
		:return:返回的列表中没有重复的元素,元素从小到大一次排列
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

	def findContent(self, table: QTableWidget, lineEdit: QLineEdit):
		findItemsList = table.findItems(lineEdit.text(), Qt.MatchContains)
		for item in findItemsList:
			item.setBackground(QBrush(Qt.cyan))  # 被查找的item背景色设置为cyan
		self.table.verticalScrollBar().setSliderPosition(findItemsList[0].column())  # 将垂直滚动条移动到第一个被查找到的item处


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TableWidget()
	window.show()
	sys.exit(app.exec_())
