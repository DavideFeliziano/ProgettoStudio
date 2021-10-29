import pickle
import os.path

from ListaPrenotazioni.Model.ListaPrenotazioni import ListaPrenotazioni


class ControlloreListaPrenotazioni():
    def __init__(self):
        super(ControlloreListaPrenotazioni, self).__init__()
        self.model = ListaPrenotazioni()
        if os.path.isfile('ListaPrenotazioni/data/listaPrenotazioniSalvata.pickle'):
            print("esiste")
            with open('ListaPrenotazioni/data/listaPrenotazioniSalvata.pickle', 'rb') as f:
                listaPrenotazioniSalvata = pickle.load(f)
            self.model = listaPrenotazioniSalvata

    def aggiungiPrenotazione(self, prenotazione):
        self.model.aggiungiPrenotazione(prenotazione)
        with open('ListaPrenotazioni/data/listaPrenotazioniSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)


    def getListaPrenotazioni(self):
        return self.model.getListaPrenotazioni()

    def getPrenotazioneByIndex(self, index):
        return self.model.getPrenotazioneByIndex(index)

    def eliminaPrenotazioneByID(self, id):
        self.model.eliminaPrenotazioneByID(id)
        with open('ListaClienti/data/listaClientiSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('ListaPrenotazioni/data/listaPrenotazioniSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)