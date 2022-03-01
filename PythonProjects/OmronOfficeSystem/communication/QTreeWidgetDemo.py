import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QPushButton, QHeaderView
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QBrush, QIcon


class QTreeWidgetDemo(QMainWindow):
	def __init__(self):
		super(QTreeWidgetDemo, self).__init__()

		self.setWindowTitle("这是一个QTreeWidget实例")
		self.resize(300, 500)
		self.p = QPushButton("删除")
		self.p1 = QPushButton("增加")

		# 创建树
		self.tree = QTreeWidget()

		# 擦行间QTreeWidgetItem
		self.root1 = QTreeWidgetItem()
		self.root1.setText(0, self.tree.tr("根目录1"))
		self.root1.setText(1, self.tree.tr("根目录1详细信息"))
		self.root2 = QTreeWidgetItem()
		self.root2.setText(0, self.tree.tr("根目录2"))
		self.root2.setText(1, self.tree.tr("根目录2详细信息"))


		self.child1 = QTreeWidgetItem()
		self.child1.setText(0, self.tree.tr("子节点1"))
		self.child1.setText(1, self.tree.tr("详细信息1"))
		self.child2 = QTreeWidgetItem()
		self.child2.setText(0, self.tree.tr("子节点2"))
		self.child2.setText(1, self.tree.tr("详细信息2"))

		self.child3 = QTreeWidgetItem()
		self.child3.setText(0, self.tree.tr("子节点3"))
		self.child3.setText(1, self.tree.tr("详细信息3"))

		self.child4 = QTreeWidgetItem()
		self.child4.setText(0, self.tree.tr("子节点4"))
		self.child4.setText(1, self.tree.tr("详细信息4"))


		# 添加子项
		# self.root1.addChild(self.child1)  # 添加单个子项目
		self.root1.addChildren([self.child1, self.child2])  # 添加多个子项目
		self.root1.insertChildren(1, [self.child3])  # 在子项列表中的索引处插入多个子项。

		# 将QTreeWidgetItem添加到QTreeWidget
		# self.tree.insertTopLevelItem(0, self.root1)  # 添加单个顶层item
		self.tree.insertTopLevelItems(0, [self.root1, self.root2])  # 添加多个顶层item

		self.tree.setColumnCount(3)
		self.tree.setHeaderLabels(["节点名", "详细信息", "创建时间"])
		# print(self.root1.indexOfChild(self.child2))

		# 查找项目并将背景色改为cyan
		# foundItems = self.tree.findItems("根目", Qt.MatchContains)  # 只能搜索TopItem，不能搜索sub item;中文要用tr()方法，否则搜索不到
		# print("查找到匹配的项目列表为：", foundItems)
		# for item in foundItems:
		# 	item.setBackground(0, QBrush(Qt.cyan))

		self.centralwidget = QWidget()
		self.vLayout = QVBoxLayout(self.centralwidget)
		self.vLayout.addWidget(self.tree)
		self.vLayout.addWidget(self.p)
		self.vLayout.addWidget(self.p1)
		self.setCentralWidget(self.centralwidget)

		# self.tree.itemPressed.connect(self.pressItem)  # 返回被点击的QTreeWidgetItem和列号
		# self.tree.clicked.connect(self.c)
		self.p.clicked.connect(self.a)
		self.p1.clicked.connect(self.b)
		self.tree.currentItemChanged.connect(self.c)

		self.tree.clearSelection()
		self.root1.setSelected(True)

		self.tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.root1.setIcon(2, QIcon("./communication/images/happy2.png"))

		self.p1.setCheckable(True)

	def pressItem(self, item: QTreeWidgetItem, column):
		print("1. 被点击的QTreeWidgetItem = ", item)
		# print("2. 被点击的QTreeWidgetItem列号 = ", column)
		# print("3. %s 被点击了" % item.text(column))
		# print("4. currentColumn() = %d" % self.tree.currentColumn())
		# print("5. currentItem() = ", self.tree.currentItem())
		print(item.parent())

	def a(self):
		print("aaaaaaa")
		child_row = self.tree.indexFromItem(self.tree.currentItem()).row()
		self.tree.currentItem().parent().takeChild(child_row)

	def b(self):
		self.root1.addChildren([self.child4])
		print(self.tree.indexFromItem(self.child4))

	def c(self, i: QTreeWidgetItem, c):
		print("cccccccccc")
		# print(self.tree.indexFromItem(i.parent()).row())
		# print(self.tree.indexFromItem(i).row())
		print(self.p1.isChecked())
		self.p1.setChecked(True)
		print(self.p1.isChecked())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QTreeWidgetDemo()
	window.show()
	sys.exit(app.exec_())