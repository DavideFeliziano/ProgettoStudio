# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaDipendentiGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel

import Dipendente.View.visualizzaDipendente
import ListaDipendenti.View.inserisciDipendenteView
from Dipendente.View.visualizzaDipendente import Ui_Form
from ListaDipendenti.Controller.ControllerListaDipendenti import ControlloreListaDipendenti
from ListaDipendenti.View.inserisciDipendenteView import Ui_Form



class ListaDipendentiUi_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(928, 782)
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(500, 20, 331, 301))
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
"QLineEdit: pressed\n"
"{\n"
"border: 5px solid rgb(255, 239, 14);\n"
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
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
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 20, 401, 741))
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
"background-color: rgb(255, 170, 0)\n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"}\n"
"")
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.goToInserisciDipendente)

        # CODICE PER LA LISTVIEW  ------------------------------------------------------------------------------------
        self.listview_model = QStandardItemModel(self.listView)
        self.controller = ControlloreListaDipendenti()
        # self.listView.show()

        for dipendente in self.controller.get_lista_dei_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(36)
            item.setFont(font)
            self.listview_model.appendRow(item)

        self.listView.setModel(self.listview_model)

        self.pushButton_2.clicked.connect(self.goToDipendenteView)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lista Dipendenti"))
        self.pushButton.setText(_translate("Form", "Nuovo"))
        self.pushButton_2.setText(_translate("Form", "Visualizza"))

    def goToInserisciDipendente(self):
        # self.inserisciClienteView = Ui_Form(self.controller, self.update_ui)
        # self.inserisciClienteView.show()
        self.Form = QtWidgets.QMainWindow()
        self.ui = ListaDipendenti.View.inserisciDipendenteView.Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def goToDipendenteView(self):
        selected = self.listView.selectedIndexes()[0].row()
        dipendenteSelected = self.controller.get_dipendente_by_index(selected)
        print("INDICE: " + str(selected))
        print("dipendente selezionato " + str(dipendenteSelected.nome) + str(dipendenteSelected.cognome))

        self.Form2 = QtWidgets.QMainWindow()
        # self.ui2 = Dipendente.View.visualizzaDipendente.Ui_Form(dipendenteSelected)
        self.ui2 = Dipendente.View.visualizzaDipendente.Ui_Form(dipendenteSelected)
        self.ui2.setupUi(self.Form2)
        self.Form2.show()


#import ListaDipendenti.View.clientiqrc_rc
