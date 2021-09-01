import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWindowBuddy

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWindowBuddy.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())