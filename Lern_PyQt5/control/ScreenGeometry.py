import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QFrame, QMainWindow


def onClick_Button():
	sender = main_window.sender()
	main_window.statusBar().showMessage(sender.text() + " 被按下了", 2000)
	print("*" * 40)
	print("main_window.x(): {0}，窗口左上角的横坐标，move移动的就是该点的横坐标；".format(main_window.x()))
	print("main_window.y(): {0}，窗口左上角的纵坐标，move移动的就是该点的纵坐标；".format(main_window.y()))
	print("main_window.width(): {0}，获取工作区的宽度；".format(main_window.width()))
	print("main_window.height(): {0}，获取工作区的高度；".format(main_window.height()))
	print("*" * 40)
	print("main_window.geometry().x(): {0}，工作区左上角的横坐标；".format(main_window.geometry().x()))
	print("main_window.geometry().y(): {0}，工作区左上角的纵坐标；".format(main_window.geometry().y()))
	print("main_window.geometry().width(): {0}，获取工作区的宽度；".format(main_window.geometry().width()))
	print("main_window.geometry().height(): {0}，获取工作区的高度；".format(main_window.geometry().height()))
	print("*" * 40)
	print("main_window.frameGeometry().x(): {0}，窗口左上角的横坐标；".format(main_window.frameGeometry().x()))
	print("main_window.frameGeometry().y(): {0}，窗口左上角的纵坐标；".format(main_window.frameGeometry().y()))
	print("main_window.frameGeometry().width(): {0}，获取窗口的宽度；".format(main_window.frameGeometry().width()))
	print("main_window.frameGeometry().height(): {0}，获取窗口的高度；".format(main_window.frameGeometry().height()))


app = QApplication(sys.argv)

main_window = QMainWindow()
main_window.setWindowTitle("我是一个MainWindow")
main_window.resize(500, 600)  # 设置的是工作区的高度；
main_window.move(600, 200)

btn = QPushButton(main_window)
btn.setText("获取屏幕尺寸和坐标")
btn.resize(200, 30)
btn.move(25, 52)
btn.clicked.connect(onClick_Button)

main_window.show()
sys.exit(app.exec_())


