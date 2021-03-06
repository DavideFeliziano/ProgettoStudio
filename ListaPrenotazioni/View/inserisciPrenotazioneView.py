# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inserisciPrenotazioneGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox

from ListaClienti.Model.ListaClienti import ListaClienti
from ListaClienti.Controller.ControllerListaClienti import ControlloreListaClienti
from Cliente.Model.Cliente import Cliente
from Cliente.Controller.ControllerCliente import ControlloreCliente
from Prenotazione.Model.Prenotazione import PrenotazioneClasse
from ListaPrenotazioni.Controller.ControllerListaPrenotazioni import ControlloreListaPrenotazioni
from Impostazioni.View.impostazioniView import ImpostazioniUi_Form




class ListaPrenotazioniUi_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1356, 823)
        self.sfondo = QtWidgets.QLabel(Form)
        self.sfondo.setGeometry(QtCore.QRect(0, 0, 1401, 831))
        self.sfondo.setText("")
        self.sfondo.setPixmap(QtGui.QPixmap(":/listaprenotazioni/sfondo.jpg"))
        self.sfondo.setScaledContents(True)
        self.sfondo.setObjectName("sfondo")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(770, 20, 551, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.incisioneRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.incisioneRadioButton.setFont(font)
        self.incisioneRadioButton.setStyleSheet("QRadioButton\n"
"{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QRadioButton:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QRadioButton:focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.incisioneRadioButton.setObjectName("incisioneRadioButton")
        self.gridLayout.addWidget(self.incisioneRadioButton, 5, 0, 1, 1)
        self.mixRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.mixRadioButton.setFont(font)
        self.mixRadioButton.setStyleSheet("QRadioButton\n"
"{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QRadioButton:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QRadioButton:focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.mixRadioButton.setObjectName("mixRadioButton")
        self.gridLayout.addWidget(self.mixRadioButton, 6, 0, 1, 1)
        self.dataSelezionataLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.dataSelezionataLabel.setFont(font)
        self.dataSelezionataLabel.setStyleSheet("QLabel\n"
"{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLabel:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"")
        self.dataSelezionataLabel.setObjectName("dataSelezionataLabel")
        self.gridLayout.addWidget(self.dataSelezionataLabel, 0, 0, 1, 1)
        self.salaRadioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.salaRadioButton.setFont(font)
        self.salaRadioButton.setStyleSheet("QRadioButton\n"
"{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QRadioButton:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QRadioButton:focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.salaRadioButton.setObjectName("salaRadioButton")
        self.gridLayout.addWidget(self.salaRadioButton, 4, 0, 1, 1)
        self.oreInizioLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.oreInizioLineEdit.setFont(font)
        self.oreInizioLineEdit.setStyleSheet("QLineEdit\n"
"{\n"
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
"QLineEdit:active\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 0, 255)\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"")
        self.oreInizioLineEdit.setObjectName("oreInizioLineEdit")
        self.gridLayout.addWidget(self.oreInizioLineEdit, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.oreFineLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.oreFineLineEdit.setFont(font)
        self.oreFineLineEdit.setStyleSheet("QLineEdit\n"
"{\n"
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
"QLineEdit:active\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 0, 255)\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"")
        self.oreFineLineEdit.setObjectName("oreFineLineEdit")
        self.gridLayout.addWidget(self.oreFineLineEdit, 2, 0, 1, 1)
        self.salvaPushButton = QtWidgets.QPushButton(Form)
        self.salvaPushButton.setGeometry(QtCore.QRect(570, 720, 321, 65))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.salvaPushButton.setFont(font)
        self.salvaPushButton.setStyleSheet("QPushButton\n"
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
        self.salvaPushButton.setObjectName("salvaPushButton")
        self.selezionaClienteListView = QtWidgets.QListView(Form)
        self.selezionaClienteListView.setGeometry(QtCore.QRect(10, 20, 651, 651))
        self.selezionaClienteListView.setStyleSheet("QListView\n"
"{\n"
"    border: 5px solid rgb(0, 85, 255);\n"
"    background-color: rgb(255, 0, 127);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QListView:hover\n"
"{\n"
"    border: 5px solid rgb(255, 0, 255);\n"
"    background-color: rgb(255, 85, 0);\n"
"    padding-left: 30px;\n"
"    padding-right: 30px;\n"
"}\n"
"\n"
"QListView:focus\n"
"{\n"
"    border: 2px solid rgb(255, 239, 14);\n"
"}")
        self.selezionaClienteListView.setObjectName("selezionaClienteListView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

#CODICE PER LA LIST VIEW --------------------------------------------------------------------------------------------
        self.listviewModel = QStandardItemModel(self.selezionaClienteListView)
        self.controller = ControlloreListaClienti()

        for cliente in self.controller.get_lista_dei_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(36)
            item.setFont(font)
            self.listviewModel.appendRow(item)

        self.selezionaClienteListView.setModel(self.listviewModel)
#-------------------------------------------------------------------------------come l'altra listview, anche questa non si aggiorna perch?? sono una persona orribile
        # print("TEST STAMPA PRENOTAZIONE" + str(self.selezionaClienteListView.selectedIndexes()))
        self.salvaPushButton.clicked.connect(self.aggiungiPrenotazione)
        self.controllerPrenotazioni =ControlloreListaPrenotazioni()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Inserisci Prenotazione"))
        self.incisioneRadioButton.setText(_translate("Form", "Incisione"))
        self.mixRadioButton.setText(_translate("Form", "Mix e Master"))
        self.dataSelezionataLabel.setText(_translate("Form", "Data"))
        self.salaRadioButton.setText(_translate("Form", "Sala Prove"))
        self.oreInizioLineEdit.setPlaceholderText(_translate("Form", "Inserisci Orario Inizio"))
        self.oreFineLineEdit.setPlaceholderText(_translate("Form", "Inserisci Orario Fine"))
        self.salvaPushButton.setText(_translate("Form", "SALVA"))

    def aggiungiPrenotazione(self):

        self.controller2 = ControlloreListaClienti()
        indice = self.selezionaClienteListView.selectedIndexes()[0].row()
        clienteSelezionato = self.controller2.get_cliente_by_index(indice)
        # print("indice " + str(indice))
        # print("Cliente Selezionato: " +str(clienteSelezionato.nome) +" "+str(clienteSelezionato.cognome))

#-------------------------------ok il cliente ce l'ho, visto che non ho messo un oggetto sul model di prenotazione, il campo "cliente" ?? solo l'id, il resto dei campi li prenod dai button
        # idSelezionato = clienteSelezionato.id
        nomeSelezionato = clienteSelezionato.nome
        cognomeSelezionato = clienteSelezionato.cognome
        id = nomeSelezionato +" "+ cognomeSelezionato
        # print("STampo ID: "+id)
        dataSelezionata = self.dataSelezionataLabel.text()
        oraInizioInserita = self.oreInizioLineEdit.text()
        oraFineInserita = self.oreFineLineEdit.text()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ qui serve qualche controllo sugli orari, usare un oggetto di Impostazioni.
        # impostazioni = ImpostazioniUi_Form()
        # aperturaDef = impostazioni.OrarioAperturaLineEdit.text()
        # chiusuraDef = impostazioni.OrarioChiusuraLineEdit.text()
        # print("test rapido @@@@@@@@@@@@@@  " + aperturaDef +" "+chiusuraDef)
#Ok per il tipo in teoria dovrei fare un metodo ma per adesso faccio solo un if
        tipoNumerico = 0
        if(self.salaRadioButton.isChecked()):
            tipoNumerico = 1
            print("SALA : " +str(tipoNumerico))
        elif(self.incisioneRadioButton.isChecked()):
            tipoNumerico = 2
            print("INCISIONE :" + str(tipoNumerico))
        elif(self.mixRadioButton.isChecked()):
            tipoNumerico = 3
            print("MIX :" +str(tipoNumerico))
#mi vergogno terribilmente di quello che sto per fare
        tipoString = ""
        if(tipoNumerico == 0):
            tipoString = "nessuno"
        elif(tipoNumerico==1):
            tipoString = "sala prove"
        elif(tipoNumerico==2):
            tipoString = "incisione"
        elif(tipoNumerico==3):
            tipoString = "mix"

        print("DATI PRENOTAZIONE: " +id +" il: "+dataSelezionata +" dalle: "+oraInizioInserita +" alle: "+ oraFineInserita +" TIPO: " +str(tipoString))

        #-------------------------------questo lo lascio in memoria delle 5 ore che ho perso perch?? l'editor non mette da solo le parentesi per?? se non le metti piange. ogio l'universo.
        # controllerLocale = ControlloreListaPrenotazioni()
        # controllerLocale.aggiungiPrenotazione(test)

        boxtest = QMessageBox()  # oggetto vuoto che per?? lo vuole per fare la finestra di errore boh ?? un miracolo che funziona

        if (id == "" or dataSelezionata == "" or oraInizioInserita == "" or oraFineInserita == "" or tipoString == "nessuno"):
            QMessageBox.critical(boxtest, 'Errore', "uno o pi?? campi vuoti", QMessageBox.Ok, QMessageBox.Ok)

        else:
            self.controllerPrenotazioni.aggiungiPrenotazione(PrenotazioneClasse(dataSelezionata,oraInizioInserita,oraFineInserita,tipoString,id))
            QMessageBox.critical(boxtest, 'GHE SBORO', "PRENOTAZIONE INSERITA!", QMessageBox.Ok, QMessageBox.Ok)

import ListaPrenotazioni.View.listaprenotazioni_rc
