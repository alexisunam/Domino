class TableroDomino:
    def __init__(self):
        self.tablero = []

    def is_jugable(self, ficha):
        if not self.tablero:
            if ficha.is_mula():
                if ficha.izq == 6 and ficha.der == 6:
                    return True
        izq_fin = self.tablero[0].izq
        der_fin = self.tablero[-1].der
        return ficha.izq in (izq_fin, der_fin) or ficha.der in (izq_fin, der_fin)
