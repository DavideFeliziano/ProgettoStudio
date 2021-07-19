
import Login.Model.Utente

import pickle
import os.path


#per fare più di un utente serve un'altra classe con una lista....


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from Login.View import loginView
from Login.View.loginView import Ui_MainWindow

class LoginController():#QDialog):
    def __init__(self):
        super(Login,self).__init__()
        #loadUi("login.ui",self)
        #self.loginButton.clicked.connect(self.loginfunction)
        self.loginButton.clicke.connect(self.test())
       # self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.createaccbutton.clicked.connect(self.gotocreate)

        prova = Login.View.loginView.passwordLineEdit

    def test(self):
        user = self.userLineEdit.text()
        password = self.passwordLineEdit.text()
        print("hai scritto: ", user, " ",password)


    def loginfunction(self):

        user=self.userLineEdit.text()
        password=self.passwordLineEdit.text()
        print(user)
        print(password)
        print("Successfully logged in with email: ", user, "and password:", password)





