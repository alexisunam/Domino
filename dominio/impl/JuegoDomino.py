from dominio.impl.Ficha import Ficha
from dominio.JuegoMesa import JuegoMesa
from dominio.impl.JugadorDomino import JugadorDomino
from dominio.impl.TableroDomino import TableroDomino
from dominio.impl.CreadorBarajaDomino import CreadorBarajaDomino


# PAtron mediator
class JuegoDomino(JuegoMesa):

    def __init__(self):
        self.jugadores: list[JugadorDomino] = []
        self.tablero_domino: TableroDomino = TableroDomino()
        self.pozo: list[Ficha] = CreadorBarajaDomino().crear_baraja()
        self.ganador: JugadorDomino = JugadorDomino("")
        self.puntuacion_alta: float = 0.0
        self.jugador_actual: int = 0
        self.fin_del_juego: bool = False

    def repartir_baraja(self):
        for jugador in self.jugadores:
            for num in range(1, 8):
                jugador.mano.append(self.pozo.pop())

    def jugar(self):
        self.repartir_baraja()
        while not self.fin_del_juego:
            jugador = self.jugadores[self.jugador_actual]
            print(f'Es el turno de {jugador.nombre}')
            print(f'Tu mano: {jugador.mano}')
            print(f'Tablero: {self.tablero_domino.tablero}')
            fichas_validas = self.get_fichas_validas(jugador)
            if fichas_validas:
                ficha_selleccionada = jugador.seleccionar_ficha(fichas_validas)



    def get_fichas_validas(self, jugador: JugadorDomino):
        fichas_validas = []
        for ficha in jugador.mano:
            if self.tablero_domino.is_jugable(ficha):
                fichas_validas.append(ficha)
        return fichas_validas


    def escojer_ganador(self):
        for jugador in self.jugadores:
            if jugador.puntuacion > self.puntuacion_alta:
                self.puntuacion_alta = jugador.puntuacion
                self.ganador = jugador
