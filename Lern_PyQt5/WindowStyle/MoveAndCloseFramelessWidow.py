import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QMenu, QAction
from PyQt5.QtGui import QImage, QMouseEvent
from PyQt5.QtCore import Qt


class MoveAndCloseFramelessWidow(QMainWindow):
    def __init__(self):
        super(MoveAndCloseFramelessWidow, self).__init__()

        self.setWindowTitle("移动和关闭无边框窗口")
        self.resize(500, 500)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setProperty("name", "FramelessWindow")
        self.setObjectName("FramelessWindow")
        self.setStyleSheet("""
                            QWidget[name="FramelessWindow"]{
                                border-image:url(images/22.jpg);
                                }
                            """)
        # 窗口居中
        self.screen = QDesktopWidget()
        self.move(int((self.screen.width()-self.size().width())/2), int((self.screen.height()-self.height())/2))

    # 使用鼠标事件实现窗口的移动
    def mousePressEvent(self, a0: QMouseEvent):
        self.mouseButton = a0.button()
        self.previousMousePos = a0.globalPos()

        # 右键关闭窗口
        if self.mouseButton == 2:
            menu = QMenu(self)
            closeAction = QAction("关闭窗口")
            menu.addActions([closeAction])
            menu.move(self.previousMousePos.x(), self.previousMousePos.y())
            menu.triggered.connect(self.menuAction)
            # closeAction.triggered.connect(self.closeWindow)
            menu.exec_()

    def mouseMoveEvent(self, a0: QMouseEvent):
        # 移动窗口
        self.nextMousePos = a0.globalPos()
        if self.mouseButton == 1:  # 只有左键按住时才能拖动窗口。由于QMouseMoveEvent.button()返回的NoButton，所以得用QMousePressEvent.button()来判断            self.nextMousePos = a0.globalPos()  # 如果用鼠标事件来移动小部件，请使用 globalPos() 返回的全局位置来避免晃动。
            self.move(self.pos().x()+self.nextMousePos.x()-self.previousMousePos.x(),
                      self.pos().y()+self.nextMousePos.y()-self.previousMousePos.y())
            self.previousMousePos = self.nextMousePos

    def menuAction(self, action: QAction):
        """
        关闭窗口
        :return:None
        """
        if action.text() == "关闭窗口":
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoveAndCloseFramelessWidow()
    window.show()
    sys.exit(app.exec_())
