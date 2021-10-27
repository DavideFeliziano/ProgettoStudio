

class ListaClienti():
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.listaClienti = []

    def aggiungi_cliente(self, cliente):
        self.listaClienti.append(cliente)

    def rimuovi_cliente_by_id(self, id):
        for cliente in self.listaClienti:
            if cliente.id == id:
                self.listaClienti.remove(cliente)
                return True
        return False

    def get_cliente_by_index(self, index):
        return self.listaClienti[index]

    def get_lista_clienti(self):
        return self.listaClienti