

class ListaPrenotazioni():
    def __init__(self):
        super(ListaPrenotazioni, self).__init__()
        self.listaPrenotazioni = []

    def aggiungiPrenotazione(self, prenotazione):
        self.listaPrenotazioni.append(prenotazione)
        

    # def eliminaPrenotazioneByID(self, cliente):       #non c'è un tasto per eliminare le prenotazioni quindi tantovale
    #     for prenotazione in self.listaPrenotazioni:
    #         if prenotazione.cliente == cliente:
    #             self.listaPrenotazioni.remove(prenotazione)
    #             return True
    #     return False

    def getPrenotazioneByIndex(self, index):
        return self.listaPrenotazioni[index]

    def getListaPrenotazioni(self):
        return self.listaPrenotazioni