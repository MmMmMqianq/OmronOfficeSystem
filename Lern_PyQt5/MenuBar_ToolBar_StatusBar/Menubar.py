import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QMenuBar, QPushButton


class MenuBarDemo(QMainWindow):
    def __init__(self):
        super(MenuBarDemo, self).__init__()

        self.setWindowTitle("这是一个MenuBar实例")
        self.resize(500, 300)

        # 1. 创建menuBar对象
        self.menuBar = QMenuBar(self)
        # 2. 创建menu对象
        self.fileMenu = QMenu()
        self.fileMenu.setTitle("文件")
        # 3. 创建子菜单
        self.recentlyOpenedSubMenu = QMenu("最近打开")
        self.recentlyOpenedSubMenu.hovered.connect(self.hoverOverTheRecentlyOpenedSubMenuAction)  # 如果菜单设置QMenu.hovered，必须悬停在Action上
                                                                                                  # 才会触发QMenu上的悬停信号,QMenu没有sender().text
                                                                                                  # QMenu有sender().title()
        # 4. 创建action
        self.openAction = QAction()
        self.openAction.setText("打开")
        self.openAction.setShortcut("ctrl+o")
        self.openAction.triggered.connect(self.triggeredAction)
        self.openAction.hovered.connect(self.hoverOverTheAction)

        self.closeAction = QAction()
        self.closeAction.setText("关闭")
        self.closeAction.setShortcut("ctrl+g")
        self.closeAction.triggered.connect(self.triggeredAction)
        self.closeAction.hovered.connect(self.hoverOverTheAction)

        self.saveAction = QAction()
        self.saveAction.setText("保存")
        self.saveAction.setShortcut("ctrl+s")
        self.saveAction.triggered.connect(self.triggeredAction)
        self.saveAction.hovered.connect(self.hoverOverTheAction)

        self.saveAsAction = QAction()
        self.saveAsAction.setText("另存为...")
        self.saveAsAction.setShortcut("ctrl+a")
        self.saveAsAction.triggered.connect(self.triggeredAction)
        self.saveAsAction.hovered.connect(self.hoverOverTheAction)

        self.file1Action = QAction("文件1")
        self.file1Action.triggered.connect(self.triggeredAction)
        self.file1Action.hovered.connect(self.hoverOverTheAction)

        # 5. 将action添加到menu上，将子菜单加到主菜单上并添加分割线，注意：如果menu下没有action的话，iOS系统上是不会显示菜单的，Windows可以显示
        self.fileMenu.addAction(self.openAction)
        action1 = self.fileMenu.addSeparator()  # 写在哪个action下面，分割线就添加在哪个action下面
        self.fileMenu.addAction(self.closeAction)
        action2 = self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveAction)
        action3 = self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.saveAsAction)
        action4 = self.fileMenu.addSeparator()
        print(action1, action2, action3, action4)
        # 将子菜单加入到主菜单下
        self.fileMenu.addMenu(self.recentlyOpenedSubMenu)
        # 将action加入到子菜单下
        self.recentlyOpenedSubMenu.addAction(self.file1Action)
        # 6. 将menu添加到menuBar上
        self.menuBar.addMenu(self.fileMenu)
        # 7. 将menuBar添加到窗口上
        self.setMenuBar(self.menuBar)

        self.fileMenu.triggered.connect(self.menuBarTriggered)  # 触发QMenu.triggered信号执行槽函数时，会将被触发的action作为参数传给槽函数

    def triggeredAction(self):
        sender = self.sender()
        print("%s动作被触发了" % sender.text())

    def hoverOverTheAction(self):
        sender = self.sender()
        print("悬停在%s上" % sender.text())

    def hoverOverTheRecentlyOpenedSubMenuAction(self):
        sender = self.sender()
        print("悬停在%s上" % sender.title())

    def menuBarTriggered(self, actionTriggered: QAction):
        print("menuBar 中的 %s action被触发了" % actionTriggered.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MenuBarDemo()
    mainWindow.show()
    sys.exit(app.exec_())
