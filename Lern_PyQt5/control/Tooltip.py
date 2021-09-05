import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QFrame, QToolTip, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont


class TooltipForm(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUi()

    def InitUi(self):
        self.resize(400, 400)
        self.move(800, 300)
        # self.setGeometry(800, 300, 400, 400)
        self.setWindowTitle("我是一个Tooltip示例窗口")
        QToolTip.setFont(QFont("SansSerif", 12))
        self.setToolTip("这是一个窗口哦！")

        self.button1 = QPushButton()
        self.button1.setText("我是一个按钮1")
        self.button1.setMaximumWidth(110)
        self.button1.setToolTip("我是一个按钮1的'Tooltip'哦！")

        self.button2 = QPushButton()
        self.button2.setText("我是一个按钮2")
        self.button2.setToolTip("我是一个按钮2的'Tooltip'哦！")

        self.layout  = QHBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TooltipForm()
    widget.show()
    sys.exit(app.exec_())
