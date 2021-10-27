import pickle
import os.path

from ListaClienti.Model.ListaClienti import ListaClienti


class ControlloreListaClienti():
    def __init__(self):
        super(ControlloreListaClienti, self).__init__()
        self.model = ListaClienti()
        if os.path.isfile('ListaClienti/data/listaClientiSalvata.pickle'):
            print("esiste")
            with open('ListaClienti/data/listaClientiSalvata.pickle', 'rb') as f:
                listaClientiSalvata = pickle.load(f)
            self.model = listaClientiSalvata

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)
        with open('ListaClienti/data/listaClientiSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_dei_clienti(self):
        return self.model.get_lista_clienti()

    def get_cliente_by_index(self, index):
        return self.model.get_cliente_by_index(index)

    def elimina_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)
        with open('ListaClienti/data/listaClientiSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('ListaClienti/data/listaClientiSalvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)