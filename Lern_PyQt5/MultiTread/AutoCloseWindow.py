import sys
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel


if __name__ == "__main__":
	app = QApplication(sys.argv)

	label = QLabel()
	# label.resize(500, 100)
	label.setText("该窗口将会在5秒之后自动关闭。。。")
	label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)

	timer = QTimer()
	timer.singleShot(5000, app.quit)  # 在定时时间到了自后只执行一次

	label.show()
	sys.exit(app.exec_())

