# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizzaDipendente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(928, 782)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        Form.setFont(font)
        Form.setStyleSheet("QLineEdit{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: focus\n"
"{\n"
"border: 2px solid rgb(255, 239, 14);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton: hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1431, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/clientprefix/sfondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 600, 631, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Modifica_pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.Modifica_pushButton_2.setFont(font)
        self.Modifica_pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.Modifica_pushButton_2.setObjectName("Modifica_pushButton_2")
        self.gridLayout.addWidget(self.Modifica_pushButton_2, 1, 0, 1, 1)
        self.Elimina_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.Elimina_pushButton.setFont(font)
        self.Elimina_pushButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.Elimina_pushButton.setObjectName("Elimina_pushButton")
        self.gridLayout.addWidget(self.Elimina_pushButton, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 60, 631, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NomeDipendente_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.NomeDipendente_label.setFont(font)
        self.NomeDipendente_label.setStyleSheet("QLabel\n"
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}")
        self.NomeDipendente_label.setObjectName("NomeDipendente_label")
        self.verticalLayout.addWidget(self.NomeDipendente_label)
        self.CognomeDipendente_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.CognomeDipendente_label.setFont(font)
        self.CognomeDipendente_label.setStyleSheet("QLabel\n"
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}")
        self.CognomeDipendente_label.setObjectName("CognomeDipendente_label")
        self.verticalLayout.addWidget(self.CognomeDipendente_label)
        self.EmailDipendente_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.EmailDipendente_label.setFont(font)
        self.EmailDipendente_label.setStyleSheet("QLabel\n"
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}")
        self.EmailDipendente_label.setObjectName("EmailDipendente_label")
        self.verticalLayout.addWidget(self.EmailDipendente_label)
        self.CellulareDipendente_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.CellulareDipendente_label.setFont(font)
        self.CellulareDipendente_label.setStyleSheet("QLabel\n"
                                                     
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}")
        self.CellulareDipendente_label.setObjectName("CellulareDipendente_label")
        self.verticalLayout.addWidget(self.CellulareDipendente_label)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Visualizza Dipendente"))
        self.Modifica_pushButton_2.setText(_translate("Form", "Modifica"))
        self.Elimina_pushButton.setText(_translate("Form", "Elimina"))
        self.NomeDipendente_label.setText(_translate("Form", "Nome"))
        self.CognomeDipendente_label.setText(_translate("Form", "Cognome"))
        self.EmailDipendente_label.setText(_translate("Form", "Email"))
        self.CellulareDipendente_label.setText(_translate("Form", "Cellulare"))


import Dipendente.View.dipendentiqrc_rc
