import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWindoeFormLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWindoeFormLayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())