from sys import argv
from sys import exit
from PyQt5.QtWidgets import QWidget, QApplication
import CommunicationUi


class CommWidgetUi(QWidget):
	def __init__(self):
		super(CommWidgetUi, self).__init__()
		self.commUi = CommunicationUi.Ui_communication()
		self.commUi.setupUi(self)


if __name__ == "__main__":
	app = QApplication(argv)
	win = CommWidgetUi()
	win.show()
	exit(app.exec_())
