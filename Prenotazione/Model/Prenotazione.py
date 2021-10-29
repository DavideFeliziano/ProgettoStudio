

class PrenotazioneClasse():
    def __init__(self, data, oraInizio, oraFine, tipo, cliente):
        super(PrenotazioneClasse, self).__init__()
        self.data = data
        self.oraInizio = oraInizio
        self.oraFine = oraFine
        self.tipo = tipo
        self.cliente = cliente