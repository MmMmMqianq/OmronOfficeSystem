#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：QComboBoxDemo.py
时间：2021/09/24
"""
import sys

from PyQt5.QtWidgets import QWidget, QComboBox, QApplication, QHBoxLayout, QLineEdit, QAbstractItemView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.setWindowTitle("这是一个QComboBox演示")
        self.resize(300, 300)

        self.combo_box = QComboBox(self)
        self.combo_box.move(50, 50)
        # 设置最大的Item数
        self.combo_box.setMaxCount(20)
        # 将ConboBox设置为可编辑的，编辑后的CurrentText会发生变化，index不会发生变化，为编辑前的Item索引。
        line_edit = QLineEdit()
        self.combo_box.setLineEdit(line_edit)
        # 设置最小的文本长度，可以用于设定ComboBox的长度
        self.combo_box.setMinimumContentsLength(20)

        # 添加字符串列表
        item_list = ["--请选择--", "item1", "item2", "item3", "item4"]
        self.combo_box.addItems(item_list)
        # 添加图标+文本的Item
        self.combo_box.addItem(QIcon("./images/1.ico"), "item5")
        # 添加文本Item
        self.combo_box.addItem("item6")

        # # 插入字符串列表
        insert_item_list = ["insert_item2", "insert_item3"]
        self.combo_box.insertItems(2, insert_item_list)
        # 插入图标+文本的Item
        self.combo_box.insertItem(2, QIcon("./images/1.ico"), "insert_item1")
        # 插入文本Item
        self.combo_box.insertItem(2, "insert_item1")

        # 设置ComboBox里的默认Item
        self.combo_box.setCurrentIndex(0)
        self.combo_box.setEditText("-请选择-")  # 当设定了QLineEdit时，可以设置ComboBox显示的默认文本

        # 设置下拉列表中最多显示的Item数量
        self.combo_box.setMaxVisibleItems(6)
        # 当前索引变化时产生一个信号
        self.combo_box.currentIndexChanged.connect(self.combo_box_current_changed)
        # 当前文本发生变化时产生一个信号
        self.combo_box.currentTextChanged.connect(self.combo_box_current_changed)
        # Item高亮时产生一个信号
        self.combo_box.highlighted.connect(self.high_lighted)

        print("1. ", self.combo_box.count())

    def combo_box_current_changed(self):
        print("2. index = ", self.combo_box.currentIndex())
        print("3. text = ", self.combo_box.currentText())

    def high_lighted(self):
        print("4, "+"这是高亮产生的信号！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QComboBoxDemo()
    widget.show()
    sys.exit(app.exec_())