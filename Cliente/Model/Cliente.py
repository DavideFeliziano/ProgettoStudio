

class Cliente():
    def __init__(self, id, nome, cognome, email, cellulare):
        super(Cliente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.cellulare = cellulare

