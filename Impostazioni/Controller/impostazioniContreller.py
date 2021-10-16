import pickle
import os.path
import json

#from Impostazioni.Model.impostazioniModel import ModelImpostazioni

#se ci metto i campi non funziona se uso l'eredità nemmeno
#io boh
#se uso un riferimento non funziona
#BASTA eredità non funziona mo basta fanculo lo vedo domani
class ImpostazioniController():
    def __init__(self):
        self.apertura = 0
        self.chiusura = 0
        self.sale = 0
        self.tariffa = 0
        self.incisione = 0
        self.mix = 0
        #tolto l'if visto che da solo problemi e non riesco a prendere i campi dal model
        # #super(ImpostazioniController, self).__init__()
        # #self.model = ModelImpostazioni() #crasha non ho capito perchè
        #
        # if os.path.isfile('Impostazioni/Data/impostazioniModificate.pickle'):
        #     print("esiste")
        #     with open('Impostazioni/Data/impostazioniModificate.pickle', 'rb') as f:
        #         impostazioniSalvate = pickle.load(f)
        #     print(impostazioniSalvate)
        #     # test = ModelImpostazioni(impostazioniSalvate['orarioApertura'], impostazioniSalvate['orarioChiusura'], impostazioniSalvate['numeroSale'], 15,20, 30)
        #     # print("TI PREGO FUNZIONA", test)
        # else:
        print("non esiste")
        with open('Impostazioni/Data/impostazioniStandard.json') as f:
            self.impostazioniIniziali = json.load(f)

        print("IMPOSTAZIONI INIZIALI LETTE", self.impostazioniIniziali)
        print("TEST STAMPA", str(self.impostazioniIniziali['orarioApertura']))

        self.apertura = self.impostazioniIniziali['orarioApertura']
        self.chiusura = self.impostazioniIniziali['orarioChiusura']
        self.sale = self.impostazioniIniziali['numeroSale']
        self.tariffa = self.impostazioniIniziali['tariffaSala']
        self.incisione = self.impostazioniIniziali['tariffaIncisione']
        self.mix = self.impostazioniIniziali['tariffaMix']

        print("stampo a pertura ", self.apertura, " ", self.chiusura, " ", self.sale, " ", self.tariffa, " ", self.incisione, " ", self.mix)

        #     Servizio(servizio["id"], servizio["nome"], servizio["tipo"], servizio["posizione"], servizio["prezzo"]))

        #Non serve più a niente creare il file pickle
        # with open('Impostazioni/Data/impostazioniModificate.pickle', 'wb') as handle:
        #     pickle.dump(self.impostazioniIniziali, handle, pickle.HIGHEST_PROTOCOL)

    def getApertura(self):
        return self.apertura

    def getChiusura(self):
        return self.chiusura

    def getNumeroSale(self):
        return self.sale

    def getTariffaSala(self):
        return self.tariffa

    def getTariffaIncisione(self):
        return self.incisione

    def getTariffaMix(self):
        return self.mix
