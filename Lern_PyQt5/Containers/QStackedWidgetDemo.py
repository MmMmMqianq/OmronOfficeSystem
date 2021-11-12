import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QHBoxLayout, QVBoxLayout


class StackedWidget(QWidget):
    def __init__(self):
        super(StackedWidget, self).__init__()

        self.setWindowTitle("这是一个StackedWidget实例")
        self.resize(500, 500)

        # 创建一个QStackedWidget容器
        self.stack = QStackedWidget()

        # 创建容器内页面
        self.widget1 = QWidget()
        self.hLayout2 = QHBoxLayout(self.widget1)
        self.button1 = QPushButton("widget1")
        self.hLayout2.addWidget(self.button1)

        self.widget2 = QWidget()
        self.hLayout3 = QHBoxLayout(self.widget2)
        self.button2 = QPushButton("widget2")
        self.hLayout3.addWidget(self.button2)

        self.widget3 = QWidget()
        self.hLayout4 = QHBoxLayout(self.widget3)
        self.button3 = QPushButton("widget3")
        self.hLayout4.addWidget(self.button3)

        self.widget4 = QWidget()
        self.hLayout5 = QHBoxLayout(self.widget4)
        self.button4 = QPushButton("widget4")
        self.hLayout5.addWidget(self.button4)

        # 将widget添加到容器内
        self.stack.addWidget(self.widget1)
        self.stack.addWidget(self.widget2)
        self.stack.addWidget(self.widget3)
        self.stack.addWidget(self.widget4)

        self.hLayout1 = QHBoxLayout()
        self.setLayout(self.hLayout1)

        self.vLayout = QVBoxLayout()

        self.button5 = QPushButton("显示widget1")
        self.button6 = QPushButton("显示widget2")
        self.button7 = QPushButton("显示widget3")
        self.button8 = QPushButton("显示widget4")
        self.buttonList = [self.button5, self.button6, self.button7, self.button8]

        self.vLayout.addWidget(self.button5)
        self.vLayout.addWidget(self.button6)
        self.vLayout.addWidget(self.button7)
        self.vLayout.addWidget(self.button8)

        self.hLayout1.addLayout(self.vLayout)
        self.hLayout1.addWidget(self.stack)

        self.button5.clicked.connect(self.showWidget)
        self.button6.clicked.connect(self.showWidget)
        self.button7.clicked.connect(self.showWidget)
        self.button8.clicked.connect(self.showWidget)

    def showWidget(self):
        s = self.sender()
        for btn in self.buttonList:
            if s == btn:
                self.stack.setCurrentIndex(self.buttonList.index(btn))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StackedWidget()
    window.show()
    sys.exit(app.exec_())