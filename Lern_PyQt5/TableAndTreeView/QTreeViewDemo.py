import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QModelIndex


class QTreeViewDemo(QMainWindow):
	def __init__(self):
		super(QTreeViewDemo, self).__init__()

		self.setWindowTitle("这是一个QTreeView实例")
		self.resize(500, 500)

		# 创建item
		self.root1 = QStandardItem()
		self.root1.setText("根节点1")

		self.root2 = QStandardItem()
		self.root2.setText("根节点2")

		self.child1 = QStandardItem()
		self.child1.setText("子节点1")
		self.child2 = QStandardItem()
		self.child2.setText("子节点2")
		self.child3 = QStandardItem()
		self.child3.setText("子节点3")
		self.child4 = QStandardItem()
		self.child4.setText("子节点4")
		self.child5 = QStandardItem()
		self.child5.setText("子节点5")

		# 创建标准item模型
		self.model = QStandardItemModel()
		self.model.setColumnCount(3)
		self.model.setRowCount(3)
		self.model.setHorizontalHeaderLabels(["A", "B", "C"])
		self.model.setVerticalHeaderLabels(["a", "b", "c"])

		# 将根节点添加到模型中，
		self.model.setItem(0, 0, self.root1)
		self.model.setItem(1, 0, self.root2)
		# 将子节点添加到根节点
		self.root1.setChild(0, 0, self.child1)
		self.root1.setChild(1, 0, self.child2)
		self.root2.setChild(0, 0, self.child3)
		self.root2.setChild(1, 0, self.child4)
		self.child1.setChild(0, 0, self.child5)

		# 创建树
		self.treeView = QTreeView()
		# 将模型设置到树
		self.treeView.setModel(self.model)
		self.treeView.setWindowTitle("树显示")
		# self.treeView.setHeaderHidden(True)  # 隐藏标题
		self.treeView.setColumnWidth(0, 120)
		self.treeView.resizeColumnToContents(1)  # 将列的宽度根据文本长度自动设置
		self.treeView.resizeColumnToContents(2)

		self.centralwidget = QWidget()
		self.vLayout = QVBoxLayout(self.centralwidget)
		self.vLayout.addWidget(self.treeView)
		self.setCentralWidget(self.centralwidget)

		self.treeView.collapsed.connect(self.treeCollapsed)
		self.treeView.expanded.connect(self.treeExpanded)
		self.treeView.pressed.connect(self.treePressed)

	def treeCollapsed(self, index: QModelIndex):  # index为根节点的坐标
		sender = self.sender()
		print("1. sender = ", sender)
		print("2. %s 产生了一个树被收起的信号" % sender.windowTitle())
		print("3. 被展开节点坐标为(%d, %d)：" % (index.row(), index.column()))

	def treeExpanded(self, index: QModelIndex):
		sender = self.sender()
		print("1. ", sender)
		print("2. %s 产生了一个树被展开的信号" % sender.windowTitle())
		print("3. 被展开节点坐标为(%d, %d)：" % (index.row(), index.column()))

	def treePressed(self, index: QModelIndex):
		# sender = self.sender()
		# print("1. sender = ", sender)
		# print("3. 被展开节点坐标为(%d, %d)：" % (index.row(), index.column()))
		print(self.treeView.selectedIndexes())


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QTreeViewDemo()
	window.show()
	sys.exit(app.exec_())
