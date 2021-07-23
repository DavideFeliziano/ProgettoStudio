class ImpostazioniModel():
    def __init__(self, orarioApertura, orarioChiusura, numeroSale, tariffaSala, tariffaIncisione, tariffaMix):
        super(ImpostazioniModel, self).__init__()
        self.orarioApertura = orarioApertura
        self.orarioChiusura = orarioChiusura
        self.numeroSale = numeroSale
        self.tariffaSala = tariffaSala
        self.tariffaIncisione = tariffaIncisione
        self.tariffaMix = tariffaMix
