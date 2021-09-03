import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWindowFormLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWindowFormLayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())