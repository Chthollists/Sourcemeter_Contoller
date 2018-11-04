'''
This is the main entry point
Author: Shawn
Date: 2018.8.11
Version: 0.1
'''

import sys
from mainUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI = QtWidgets.QMainWindow()
    MainUI = Ui_MainWindow()
    MainUI.setupUi(UI)
    UI.show()
    sys.exit(app.exec_())


