# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizzaImpostazioni.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Impostazioni.Controller import impostazioniContreller
from Impostazioni.Controller.impostazioniContreller import ImpostazioniController


class ImpostazioniUi_Form(object):
    def setupUi(self, ImpostazioniForm):
        ImpostazioniForm.setObjectName("ImpostazioniForm")
        ImpostazioniForm.resize(1423, 777)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        ImpostazioniForm.setFont(font)
        ImpostazioniForm.setStyleSheet("QLineEdit{\n"
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
        self.label = QtWidgets.QLabel(ImpostazioniForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 1431, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/clientprefix/sfondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(ImpostazioniForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(632, 640, 751, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.salvaButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.salvaButton.setFont(font)
        self.salvaButton.setStyleSheet("QPushButton\n"
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
        self.salvaButton.setObjectName("salvaButton")
        self.gridLayout.addWidget(self.salvaButton, 1, 0, 1, 1)
        self.ripristinaButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.ripristinaButton.setFont(font)
        self.ripristinaButton.setStyleSheet("QPushButton\n"
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
        self.ripristinaButton.setObjectName("ripristinaButton")
        self.gridLayout.addWidget(self.ripristinaButton, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(ImpostazioniForm)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1291, 611))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tariffaMixLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.tariffaMixLabel.setFont(font)
        self.tariffaMixLabel.setStyleSheet("QLabel\n"
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
        self.tariffaMixLabel.setObjectName("tariffaMixLabel")
        self.gridLayout_2.addWidget(self.tariffaMixLabel, 8, 0, 1, 1)
        self.OrarioAperturaLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.OrarioAperturaLabel.setFont(font)
        self.OrarioAperturaLabel.setStyleSheet("QLabel\n"
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
        self.OrarioAperturaLabel.setObjectName("OrarioAperturaLabel")
        self.gridLayout_2.addWidget(self.OrarioAperturaLabel, 2, 0, 1, 1)
        self.OrarioAperturaLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.OrarioAperturaLineEdit.setFont(font)
        self.OrarioAperturaLineEdit.setObjectName("OrarioAperturaLineEdit")
        self.gridLayout_2.addWidget(self.OrarioAperturaLineEdit, 2, 1, 1, 1)
        self.OrarioChiusuraLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.OrarioChiusuraLabel.setFont(font)
        self.OrarioChiusuraLabel.setStyleSheet("QLabel\n"
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
        self.OrarioChiusuraLabel.setObjectName("OrarioChiusuraLabel")
        self.gridLayout_2.addWidget(self.OrarioChiusuraLabel, 3, 0, 1, 1)
        self.tariffaSalaProveLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.tariffaSalaProveLabel.setFont(font)
        self.tariffaSalaProveLabel.setStyleSheet("QLabel\n"
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
        self.tariffaSalaProveLabel.setObjectName("tariffaSalaProveLabel")
        self.gridLayout_2.addWidget(self.tariffaSalaProveLabel, 5, 0, 1, 1)
        self.OrarioChiusuraLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.OrarioChiusuraLineEdit.setFont(font)
        self.OrarioChiusuraLineEdit.setObjectName("OrarioChiusuraLineEdit")
        self.gridLayout_2.addWidget(self.OrarioChiusuraLineEdit, 3, 1, 1, 1)
        self.tariffaSalaProveLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.tariffaSalaProveLineEdit.setFont(font)
        self.tariffaSalaProveLineEdit.setObjectName("tariffaSalaProveLineEdit")
        self.gridLayout_2.addWidget(self.tariffaSalaProveLineEdit, 5, 1, 1, 1)
        self.tariffaMixLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.tariffaMixLineEdit.setFont(font)
        self.tariffaMixLineEdit.setObjectName("tariffaMixLineEdit")
        self.gridLayout_2.addWidget(self.tariffaMixLineEdit, 8, 1, 1, 1)
        self.tariffaIncisioneLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.tariffaIncisioneLabel.setFont(font)
        self.tariffaIncisioneLabel.setStyleSheet("QLabel\n"
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
        self.tariffaIncisioneLabel.setObjectName("tariffaIncisioneLabel")
        self.gridLayout_2.addWidget(self.tariffaIncisioneLabel, 6, 0, 1, 1)
        self.tariffaIncisioneLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.tariffaIncisioneLineEdit.setFont(font)
        self.tariffaIncisioneLineEdit.setObjectName("tariffaIncisioneLineEdit")
        self.gridLayout_2.addWidget(self.tariffaIncisioneLineEdit, 6, 1, 1, 1)
        self.NumeroSaleLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.NumeroSaleLineEdit.setFont(font)
        self.NumeroSaleLineEdit.setObjectName("NumeroSaleLineEdit")
        self.gridLayout_2.addWidget(self.NumeroSaleLineEdit, 4, 1, 1, 1)
        self.NumeroSaleLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.NumeroSaleLabel.setFont(font)
        self.NumeroSaleLabel.setStyleSheet("QLabel\n"
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
        self.NumeroSaleLabel.setObjectName("NumeroSaleLabel")
        self.gridLayout_2.addWidget(self.NumeroSaleLabel, 4, 0, 1, 1)

        self.retranslateUi(ImpostazioniForm)
        QtCore.QMetaObject.connectSlotsByName(ImpostazioniForm)


        self.controller = ImpostazioniController()


    def retranslateUi(self, ImpostazioniForm):
        _translate = QtCore.QCoreApplication.translate
        ImpostazioniForm.setWindowTitle(_translate("ImpostazioniForm", "Impostazioni"))
        self.salvaButton.setText(_translate("ImpostazioniForm", "Salva Modifiche"))
        self.ripristinaButton.setText(_translate("ImpostazioniForm", "Ripristina"))
        self.tariffaMixLabel.setText(_translate("ImpostazioniForm", "Tariffa Oraria Mix e Master: "))
        self.OrarioAperturaLabel.setText(_translate("ImpostazioniForm", "Orario Apertura: "))
        self.OrarioChiusuraLabel.setText(_translate("ImpostazioniForm", "Orario Chiusura: "))
        self.tariffaSalaProveLabel.setText(_translate("ImpostazioniForm", "Tariffa Oraria Sala Prove: "))
        self.tariffaIncisioneLabel.setText(_translate("ImpostazioniForm", "Tariffa Oraria Incisione: "))
        self.NumeroSaleLabel.setText(_translate("ImpostazioniForm", "Numero Sale Disponibili: "))

        contr = impostazioniContreller.ImpostazioniController()

        apertura = contr.getApertura()
        chiusura = contr.getChiusura()
        sale = contr.getNumeroSale()
        tariffa = contr.getTariffaMix()
        incisione = contr.getTariffaIncisione()
        mix = contr.getTariffaMix()
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA STAMPO LA STRINGA", apertura, chiusura,sale, tariffa, incisione, mix)
        # NOTA: questa funzione del cazzo prende solo stringhe come parametro, per convertire qualsiasi cosa in stringa: str(qualsiasicosa)
        self.OrarioAperturaLineEdit.setText(str(apertura))
        self.OrarioChiusuraLineEdit.setText(str(chiusura))
        self.NumeroSaleLineEdit.setText(str(sale))
        self.tariffaSalaProveLineEdit.setText(str(tariffa))
        self.tariffaIncisioneLineEdit.setText(str(incisione))
        self.tariffaMixLineEdit.setText(str(mix))
        #funziona ma adesso devo capire come portarmi questi numeri nelle altre classi

import Impostazioni.View.clientiqrc_rc
