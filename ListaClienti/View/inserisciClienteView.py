# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inserisciClienteGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(933, 823)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1401, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/testBackground/sfondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 10, 611, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 1, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 660, 321, 65))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QLineEdit: pressed\n"
"{\n"
"    border: 5px solid rgb(255, 239, 14);\n"
"    background-color: rgb(255, 170, 0)\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Inserisci Cliente"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Cognome"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Mail"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Nome"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Cellulare"))
        self.pushButton.setText(_translate("Form", "CREA"))
import testqrc_rc