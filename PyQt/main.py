import sys
import PyQt5.QtWidgets as QW
import MainWindow
from PyQt5 import QtGui

if __name__ == '__main__':
    a = QW.QApplication(sys.argv)
    mainWindow = MainWindow.MainWindow(None)
    mainWindow.show()
    exit(a.exec())
