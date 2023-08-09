class Carta:
    Corazon = 'pinta/corazon'
    Diamante = 'pinta/diamante'
    Pica = 'pinta/pica'
    Trebol = 'pinta/trebol'

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta = Carta(9, Carta.Trebol)

print(carta.valor)
print(carta.pinta)
