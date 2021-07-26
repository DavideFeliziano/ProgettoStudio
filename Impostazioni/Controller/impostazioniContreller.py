import pickle
import os.path
import json

from Impostazioni.Model.impostazioniModel import ModelImpostazioni


class ImpostazioniController():
    def __init__(self):
        super(ImpostazioniController, self).__init__()
        # self.model = ModelImpostazioni()

        if os.path.isfile('Impostazioni/Data/impostazioniModificate.pickle'):
            print("esiste")
            with open('Impostazioni/Data/impostazioniModificate.pickle', 'rb') as f:
                impostazioniSalvate = pickle.load(f)
            print(impostazioniSalvate)
            # self.model = impostazioniSalvate
        else:
            print("non esiste")
            with open('Impostazioni/Data/impostazioniStandard.json') as f:
                impostazioniIniziali = json.load(f)
                print(impostazioniIniziali)

            # QUA C'E' DA LEGGERE IL FILE E SCRIVERE I DATI MA PRIMA DEVO LEGGERE IL FILE
            # for servizio in impostazioniIniziali:
            #NON SERVE IL METODO perchè non abbiamo una lista, basta che leggiamo i campi ma adesso non so come fare
            # self.model.tariffaMix = ["tariffaMix"]
            # self.model.numeroSale = ["numeroSale"]
                # self.model.aggiungi_servizio(
                #     Servizio(servizio["id"], servizio["nome"], servizio["tipo"], servizio["posizione"], servizio["prezzo"]))
            with open('Impostazioni/Data/impostazioniModificate.pickle', 'wb') as handle:
                pickle.dump(impostazioniIniziali, handle, pickle.HIGHEST_PROTOCOL)



    def getApertura(self):
        return self.model.orarioApertura

    def getChiusura(self):
        return self.model.orarioChiusura

    def getNumeroSale(self):
        return self.model.numeroSale

    def getTariffaSala(self):
        return self.model.tariffaSala

    def getTariffaIncisione(self):
        return self.model.tariffaIncisione

    def getTariffaMix(self):
        return self.model.tariffaMix

