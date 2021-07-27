
class PrenotazioneController():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def getDataPrenotazione(self):
        return self.model.data

    def getOraInizio(self):
        return self.model.oraInizio

    def getOraFine(self):
        return self.model.oraFine

    def getTipoPrenotazione(self):
        return self.model.tipo

    def getClientePrenotazione(self):
        return self.model.cliente