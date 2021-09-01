import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWindoeAbsoluteLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWindoeAbsoluteLayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())