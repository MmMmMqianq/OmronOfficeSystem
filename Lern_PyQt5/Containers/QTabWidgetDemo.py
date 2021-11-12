import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class TabWidget(QWidget):
    def __init__(self):
        super(TabWidget, self).__init__()

        self.setWindowTitle("这是一个TabWidget实例")
        self.resize(500, 500)

        # 创建选项卡容器
        self.tabContainer = QTabWidget()

        # 创建每个选项卡对应的窗口
        self.tab1 = QWidget()
        self.hLayout2 = QHBoxLayout(self.tab1)
        self.button1 = QPushButton("切换到选项卡2")
        self.hLayout2.addWidget(self.button1)

        self.tab2 = QWidget()
        self.hLayout3 = QHBoxLayout(self.tab2)
        self.button2 = QPushButton("插入选项卡4")
        self.hLayout3.addWidget(self.button2)

        self.tab3 = QWidget()
        self.hLayout4 = QHBoxLayout(self.tab3)
        self.button3 = QPushButton("删除选项卡4")
        self.button3.setEnabled(False)
        self.hLayout4.addWidget(self.button3)

        self.tab4 = QWidget()
        self.hLayout5 = QHBoxLayout(self.tab4)
        self.button4 = QPushButton("按钮4")
        self.hLayout5.addWidget(self.button4)

        # 将选项卡添加到容器
        self.tabContainer.addTab(self.tab1, "选项卡1")
        self.tabContainer.addTab(self.tab2, "选项卡2")
        # self.tabContainer.insertTab(2, self.tab4, "选项卡4")  # 插入选项卡
        self.tabContainer.addTab(self.tab3, "选项卡3")

        print("1. tabContainer.count() = ", self.tabContainer.count())  # 获取选项卡容器的选项卡数量
        self.tabContainer.setTabIcon(1, QIcon("./images/1.ico"))  # 设置tab图标
        self.tabContainer.setDocumentMode(False)  # 设置选项卡容器是否为文档模式
        self.tabContainer.setMovable(True)  # 设置选项卡是否可移动
        self.tabContainer.setTabEnabled(0, True)  # 设置选项卡是否可用，设置为True时变为灰色不能点
        self.tabContainer.setTabPosition(QTabWidget.North)  # 设置选项卡的位置，默认为QTabWidget.North
        self.tabContainer.setTabShape(QTabWidget.Rounded)  # 设置选显卡是圆角还是直角
        self.tabContainer.setElideMode(Qt.ElideMiddle)  # 设置如果选显卡长度小于文本长度是，省略号的位置
        self.tabContainer.setTabToolTip(0, "选项卡1的tool tip")  # 设置选项卡的tool tip
        self.tabContainer.setTabToolTip(1, "选项卡2的tool tip")
        self.tabContainer.setTabToolTip(2, "选项卡3的tool tip")
        self.tabContainer.setTabsClosable(True)  # 设置选项卡是否可以被关闭，配合QTabWidget.tabCloseRequested信号和QTabWidget.removeTab()方法关闭选项卡
        self.tabContainer.setUsesScrollButtons(True)  # 设置是否只用滚动条
        self.tabContainer.setCornerWidget(QPushButton("corner"), Qt.TopLeftCorner)  # 设置一个角部件

        self.hLayout1 = QHBoxLayout(self)
        self.hLayout1.addWidget(self.tabContainer)

        self.button1.clicked.connect(self.selectTab)
        self.button3.clicked.connect(self.removeTab4)
        self.button2.clicked.connect(self.insertTab)

        self.tabContainer.currentChanged.connect(self.currentTabChanged)
        self.tabContainer.tabBarDoubleClicked.connect(self.doubleClickTabBar)
        self.tabContainer.tabBarClicked.connect(self.clickTabBar)
        self.tabContainer.tabCloseRequested.connect(self.closeTab)

    def removeTab4(self):
        if self.tabContainer.tabText(2) == "选项卡4":
            print("2. 移除了%s" % self.tabContainer.tabText(2))  # 获取指定选项卡的文本
            self.tabContainer.removeTab(2)  # 移除指定的选项卡
            self.button3.setEnabled(False)
            self.button2.setEnabled(True)

    def insertTab(self):
        if self.tabContainer.tabText(2) != "选项卡4":
            self.tabContainer.insertTab(2, self.tab4, "选项卡4")  # 插入指定的选项卡
            print("2. 插入了%s" % self.tabContainer.tabText(2))
            self.button2.setEnabled(False)
            self.button3.setEnabled(True)

    def selectTab(self):
        self.tabContainer.setCurrentIndex(1)
        print("3. 切换到%s" % self.tabContainer.tabText(1))

    def currentTabChanged(self, index):
        print("4. 触发了QTabWidget.currentChanged信号，切换到了%s" % self.tabContainer.tabText(index))

    def clickTabBar(self, index):
        print("5. 触发了QTabWidget.tabBarClicked信号，点击了%s" % self.tabContainer.tabText(index))

    def doubleClickTabBar(self, index):
        print("6. 触发了QTabWidget.doubleTabBarClicked信号，点击了%s" % self.tabContainer.tabText(index))

    def closeTab(self, index):
        self.tabContainer.removeTab(index)
        print("7. 触发了QTabWidget.tabCloseRequested信号，%s已被关闭" % self.tabContainer.tabText(index))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabWidget()
    window.show()
    sys.exit(app.exec_())