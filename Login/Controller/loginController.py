
import Login.Model.Utente

import pickle
import os.path


#per fare più di un utente serve un'altra classe con una lista....


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from Login.View import loginView

class Login()#QDialog):
    def __init__(self):
        super(Login,self).__init__()
        #loadUi("login.ui",self)
        self.pushButton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):

        user=self.lineEdit_3.text()
        password=self.lineEdit_2.text()
        print(user)
        print(password)
        print("Successfully logged in with email: ", user, "and password:", password)


#app=QApplication(sys.argv)
#mainwindow=Login()
#widget=QtWidgets.QStackedWidget()
#widget.addWidget(mainwindow)
#widget.setFixedWidth(480)
#widget.setFixedHeight(620)
#widget.show()

#app.exec_()


