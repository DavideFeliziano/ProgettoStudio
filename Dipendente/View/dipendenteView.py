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
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
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
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 60, 631, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
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
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
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
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
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
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel\n"
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
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Visualizza Dipendente"))
        self.pushButton_2.setText(_translate("Form", "Modifica"))
        self.pushButton.setText(_translate("Form", "Elimina"))
import Dipendente.View.dipendentiqrc_rc
