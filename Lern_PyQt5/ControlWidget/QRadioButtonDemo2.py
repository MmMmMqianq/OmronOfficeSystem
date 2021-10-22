#  -*- coding:utf-8 -*-
"""
作者：钱少青
文件名：QRadioButton.py
时间：2021/09/23
"""
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout
import sys


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.setWindowTitle("这是一个QRadioButton案例")
        self.resize(200, 200)

        self.radio_button_1 = QRadioButton(self)
        self.radio_button_1.setText("单选按钮1")
        self.radio_button_1.setCheckable(True)
        self.radio_button_1.toggled.connect(lambda: self.radio_button_toggle(self.radio_button_1))

        self.radio_button_2 = QRadioButton(self)
        self.radio_button_2.setText("单选按钮2")
        self.radio_button_2.setCheckable(True)
        self.radio_button_2.toggled.connect(lambda: self.radio_button_toggle(self.radio_button_2))

        self.v_layout = QVBoxLayout(self)
        self.v_layout.addWidget(self.radio_button_1)
        self.v_layout.addWidget(self.radio_button_2)

    def radio_button_toggle(self, radio_button: QRadioButton):
        radio_button_sender = self.sender()
        if radio_button.isChecked():
            print(radio_button_sender.text() + ">被选中")
        else:
            print(radio_button_sender.text() + ">未被选中")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QRadioButtonDemo()
    widget.show()
    sys.exit(app.exec_())
