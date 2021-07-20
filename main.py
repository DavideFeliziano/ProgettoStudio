import sys
import self as self

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from Home.View.homeView import Ui_Form
from Login.View.loginView import Ui_MainWindow


class LoginClass(QMainWindow):
    def __init__(self):
        super(LoginClass, self).__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

# class homeClass(object):
#     def __init__(self):
#         super(homeClass, self).__init__()
#         self.win = Ui_Form()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self.win)

if __name__ == '__main__':
    # self.loginwindow= Ui_MainWindow()
    # self.loginwindow.show()

    app  = QApplication(sys.argv)
    self.diobestia = LoginClass()

    self.diobestia.window.show()
    # mainwin = QMainWindow()
    # Form = QtWidgets.QWidget()
    # ui = Ui_MainWindow()
    # ui.setupUi(mainwin)
    # mainwin.show()
    sys.exit(app.exec_())



