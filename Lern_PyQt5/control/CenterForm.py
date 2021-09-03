import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
	def __init__(self):
		super(CenterForm, self).__init__()

		# 设置主窗口标标题
		self.setWindowTitle("This is FirstMainWindow")

		# 设置主窗口大小
		self.resize(500, 400)

		# 居中
		self.center()

	def center(self):
		# 获取屏幕坐标系
		screen_geo = QDesktopWidget().screenGeometry()
		# 获取主窗口坐标器系
		main_win_geo = self.geometry()
		# 计算居中坐标
		size_left = (screen_geo.width()-main_win_geo.width()) / 2
		size_top = (screen_geo.height()-main_win_geo.height()) / 2
		# 移动窗口
		self.move(size_left, size_top)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = CenterForm()
	main.show()
	sys.exit(app.exec_())