import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush


class QTreeWidgetDemo(QMainWindow):
	def __init__(self):
		super(QTreeWidgetDemo, self).__init__()

		self.setWindowTitle("这是一个QTreeWidget实例")
		self.resize(300, 500)

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

		self.child4 = self.child3.clone()  # 克隆一个QTreeWidget

		# 添加子项
		# self.root1.addChild(self.child1)  # 添加单个子项目
		self.root1.addChildren([self.child1, self.child2])  # 添加多个子项目
		self.root1.insertChildren(1, [self.child3, self.child4])  # 在子项列表中的索引处插入多个子项。

		# 将QTreeWidgetItem添加到QTreeWidget
		# self.tree.insertTopLevelItem(0, self.root1)  # 添加单个顶层item
		self.tree.insertTopLevelItems(0, [self.root1, self.root2])  # 添加多个顶层item

		self.tree.setColumnCount(3)
		self.tree.setHeaderLabels(["节点名", "详细信息", "创建时间"])
		# print(self.root1.indexOfChild(self.child2))

		# 查找项目并将背景色改为cyan
		foundItems = self.tree.findItems("根目", Qt.MatchContains)  # 只能搜索TopItem，不能搜索sub item;中文要用tr()方法，否则搜索不到
		print("查找到匹配的项目列表为：", foundItems)
		for item in foundItems:
			item.setBackground(0, QBrush(Qt.cyan))

		self.centralwidget = QWidget()
		self.vLayout = QVBoxLayout(self.centralwidget)
		self.vLayout.addWidget(self.tree)
		self.setCentralWidget(self.centralwidget)

		self.tree.itemPressed.connect(self.pressItem)  # 返回被点击的QTreeWidgetItem和列号

	def pressItem(self, item: QTreeWidgetItem, column):
		print("1. 被点击的QTreeWidgetItem = ", item)
		print("2. 被点击的QTreeWidgetItem列号 = ", column)
		print("3. %s 被点击了" % item.text(column))
		print("4. currentColumn() = %d" % self.tree.currentColumn())
		print("5. currentItem() = ", self.tree.currentItem())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QTreeWidgetDemo()
	window.show()
	sys.exit(app.exec_())