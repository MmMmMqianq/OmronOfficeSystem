import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget, QMenu, QAction
from PyQt5.QtGui import QMovie, QMouseEvent
from  PyQt5.QtCore import Qt


class LoadingGif(QLabel):
	def __init__(self):
		super(LoadingGif, self).__init__()

		self.setWindowFlags(Qt.FramelessWindowHint)

		self.movie = QMovie("./images/加载-013.gif")
		self.movie.start()
		self.setMovie(self.movie)

		# 窗口居中
		self.screen = QDesktopWidget()
		self.move(int((self.screen.width() - self.size().width()) / 2), int((self.screen.height() - self.height()) / 2))

	# 使用鼠标事件实现窗口的移动
	def mousePressEvent(self, a0: QMouseEvent):
		self.mouseButton = a0.button()
		self.previousMousePos = a0.globalPos()

	def mouseMoveEvent(self, a0: QMouseEvent):
		self.nextMousePos = a0.globalPos()
		if self.mouseButton == 1:  # 只有左键按住时才能拖动窗口。由于QMouseMoveEvent.button()返回的NoButton，所以得用QMousePressEvent.button()来判断            self.nextMousePos = a0.globalPos()  # 如果用鼠标事件来移动小部件，请使用 globalPos() 返回的全局位置来避免晃动。
			self.move(self.pos().x() + self.nextMousePos.x() - self.previousMousePos.x(),
			          self.pos().y() + self.nextMousePos.y() - self.previousMousePos.y())
			self.previousMousePos = self.nextMousePos


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingGif()
    window.show()
    sys.exit(app.exec_())