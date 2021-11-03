

class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.listaDipendenti = []

    def aggiungi_dipendente(self, dipendente):
        self.listaDipendenti.append(dipendente)

    def rimuovi_dipendente_by_id(self, id):
        for dipendente in self.listaDipendenti:
            if dipendente.id == id:
                self.listaDipendenti.remove(dipendente)
                return True
        return False

    def get_dipendente_by_index(self, index):
        return self.listaDipendenti[index]

    def get_lista_dipendenti(self):
        return self.listaDipendenti