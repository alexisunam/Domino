from dominio.ObjetoJuego import ObjetoJuego


class Ficha(ObjetoJuego):

    def __init__(self, izq, der):
        self.izq: str = izq
        self.der: str = der

    def is_mula(self):
        return self.izq == self.der

    def muestra_valor(self):
        pass
    # def __str__(self):
    #     return f"cara1: {self.cara1}, cara2: {self.cara2}"
