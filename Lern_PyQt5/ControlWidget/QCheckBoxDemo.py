#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：QCheckBoxDemo.py
时间：2021/09/24
"""
import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.setWindowTitle("这是一个QCheckBox演示")
        self.resize(400, 100)

        self.check_box_1 = QCheckBox()
        self.check_box_1.setText("复选框1")
        self.check_box_1.stateChanged.connect(lambda: self.check_box_changed(self.check_box_1))

        self.check_box_2 = QCheckBox()
        self.check_box_2.setCheckState(Qt.Checked)
        self.check_box_2.setText("复选框2")
        self.check_box_2.stateChanged.connect(lambda: self.check_box_changed(self.check_box_2))

        self.check_box_3 = QCheckBox()
        self.check_box_3.setText("复选框3")
        self.check_box_3.setTristate(True)
        self.check_box_3.stateChanged.connect(lambda: self.check_box_changed(self.check_box_3))

        self.h_layout = QHBoxLayout(self)
        self.h_layout.addWidget(self.check_box_1)
        self.h_layout.addWidget(self.check_box_2)
        self.h_layout.addWidget(self.check_box_3)

    def check_box_changed(self, check_box: QCheckBox):
        sender = self.sender()
        print(sender.text() + "状态发生变化")
        print(sender.text() + ": isTirState() = " + str(check_box.isTristate()))
        print(sender.text() + ": ischecked() = " + str(check_box.isChecked()))
        print(sender.text() + ": checkState() = " + str(check_box.checkState()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QCheckBoxDemo()
    widget.show()
    sys.exit(app.exec_())