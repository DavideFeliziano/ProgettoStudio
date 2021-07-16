# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1425, 896)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        Form.setFont(font)
        Form.setStyleSheet("\n"
"QLineEdit{\n"
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
"\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1431, 901))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/home/sfondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 781, 511))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMouseTracking(True)
        self.calendarWidget.setStyleSheet("QCalendarWidget QWidget\n"
"{\n"
"alternate-background-color: rgb(255, 85, 0);\n"
"border: 5px solid rgb(0, 85, 255);\n"
"color: rgb(0, 85, 255)\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled\n"
"{\n"
"color: rgb(0, 85, 255);\n"
"background-color: black;\n"
"selection-background-color: rgb(255, 255, 0);\n"
"selection-color:rgb(255, 0, 255)\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{\n"
"background-color: rgb(255, 0, 255);\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QCalendarWidget:hover\n"
"\n"
"\n"
"\n"
"{\n"
"\n"
"\n"
"\n"
"border: 5px solid rgb(255, 0, 255);\n"
"\n"
"\n"
"\n"
"background-color: rgb(255, 85, 0);\n"
"\n"
"\n"
"\n"
"}")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(820, 0, 591, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
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
"QButton:pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color:rgb(255, 255, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(180, 530, 481, 351))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
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
"QButton:pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color:rgb(255, 255, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
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
"QButton:pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color:rgb(255, 255, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
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
"QButton:pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color:rgb(255, 255, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(820, 90, 591, 791))
        self.listView.setStyleSheet("QListView\n"
"{\n"
"border: 5px solid rgb(0, 85, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QListView:hover\n"
"{\n"
"border: 5px solid rgb(255, 0, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"\n"
"QListView:pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color:rgb(255, 255, 0);\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}")
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Reheasal Room Booker Home"))
        self.pushButton.setText(_translate("Form", "Nuovo"))
        self.pushButton_4.setText(_translate("Form", "Clienti"))
        self.pushButton_2.setText(_translate("Form", "Modifica"))
        self.pushButton_3.setText(_translate("Form", "Dipendenti"))
import Home.View.home_rc
