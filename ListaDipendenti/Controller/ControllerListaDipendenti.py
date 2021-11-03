import pickle
import os.path

from ListaDipendenti.Model.ListaDipendenti import ListaDipendenti


class ControlloreListaDipendenti():
    def __init__(self):
        super(ControlloreListaDipendenti, self).__init__()
        self.model = ListaDipendenti()
        if os.path.isfile('ListaDipendenti/data/listaDipendentiSalvata.pickle'):
            print("esiste")
            with open('ListaDipendenti/data/listaDipendentiSalvata.pickle', 'rb') as f:
                listaDipendentiSalvata = pickle.load(f)
            self.model = listaDipendentiSalvata

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)
        with open('ListaDipendenti/data/listaDipendentiSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_dei_dipendenti(self):
        return self.model.get_lista_dipendenti()

    def get_dipendente_by_index(self, index):
        return self.model.get_dipendente_by_index(index)

    def elimina_dipendente_by_id(self, id):
        self.model.rimuovi_dipendente_by_id(id)
        with open('ListaDipendenti/data/listaDipendentiSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('ListaDipendenti/data/listaDipendentiSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)