class ImpostazioniController():
    def __init__(self, impostazioni):
        self.model = impostazioni

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

